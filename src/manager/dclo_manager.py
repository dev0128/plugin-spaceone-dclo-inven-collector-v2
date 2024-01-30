import logging
import hashlib
import json

from spaceone.core.manager import BaseManager
from spaceone.inventory.plugin.collector.lib import *
from spaceone.core.error import ERROR_INVALID_PARAMETER


from ..connector.dclo_connector import DcloConnector


_LOGGER = logging.getLogger("cloudforet")


COMPLIANCE_FRAMEWORKS = {
    "aws": {
        "D-CLO Best Practice": "SET-00011014",
        "ISMS": "SET-00026100",
        "KISA-CSAP(표준)": "SET-00026102",
        "KISA-CSAP(간편)": "SET-00026103",
        "CSP 안전성 평가": "SET-00026104",
        "NIS-국가·공공 기관": "SET-00026105",
        "NIS-민간 기관": "SET-00026106",
        "NIS-SaaS": "SET-00026107",
        "ISO-27001": "SET-00026108",
        "PCI-DSS 3.2.1": "SET-00026109",
    },
    "google_cloud": {
        "D-CLO Best Practice": "SET-00028128",
        "ISMS": "SET-00028110",
        "KISA-CSAP(표준)": "SET-00028111",
        "KISA-CSAP(간편)": "SET-00028112",
        "CSP 안전성 평가": "SET-00028113",
        "ISO-27001": "SET-00028114",
        "PCI-DSS 3.2.1": "SET-00028115",
        "NIS-국가·공공 기관": "SET-00028116",
        "NIS-민간 기관": "SET-00028117",
        "NIS-SaaS": "SET-00028118",
    },
    "azure": {
        "D-CLO Best Practice": "SET-00028129",
        "ISMS": "SET-00028119",
        "KISA-CSAP(표준)": "SET-00028120",
        "KISA-CSAP(간편)": "SET-00028121",
        "CSP 안전성 평가": "SET-00028122",
        "ISO-27001": "SET-00028123",
        "PCI-DSS 3.2.1": "SET-00028124",
        "NIS-국가·공공 기관": "SET-00028125",
        "NIS-민간 기관": "SET-00028126",
        "NIS-SaaS": "SET-00028127",
    },
}


class DcloManager(BaseManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.dclo_connector = DcloConnector()

        self.cloud_service_group = "D-CLO"
        self.cloud_service_type = None
        self.provider = None
        self.metadata_path = "metadata/dclo/dclo.yaml"

    def collect_resources(self, options, secret_data, schema):
        try:
            yield from self.collect_cloud_service_type(options)
            yield from self.collect_cloud_service(options, secret_data, schema)
        except Exception as e:
            yield make_error_response(
                error=e,
                provider=self.provider,
                cloud_service_group=self.cloud_service_group,
                cloud_service_type=self.cloud_service_type,
            )

    def collect_cloud_service_type(self, options):
        self.cloud_service_type = options["compliance_framework"]
        self.provider = options["provider"]
        self._check_compliance_framework()

        cloud_service_type = make_cloud_service_type(
            name=self.cloud_service_type,
            group=self.cloud_service_group,
            provider=self.provider,
            metadata_path=self.metadata_path,
            is_primary=True,
            is_major=True,
        )

        yield make_response(
            cloud_service_type=cloud_service_type,
            match_keys=[["name", "group", "provider"]],
            resource_type="inventory.CloudServiceType",
        )

    def collect_cloud_service(self, options, secret_data, schema):
        key_type, compliance, diag_data = self._covert_options(options, secret_data)
        diag_id, compliance_results = self.dclo_connector.fetch_compliance_results(
            key_type, compliance, diag_data
        )

        for finding in compliance_results.get("findings", []):
            cloud_service = make_cloud_service(
                name=finding["code"],
                account=diag_id,
                cloud_service_type=self.cloud_service_type,
                cloud_service_group=self.cloud_service_group,
                provider=self.provider,
                data=self._covert_dclo_to_spaceOne(finding),
            )
            yield make_response(
                cloud_service=cloud_service,
                match_keys=[
                    [
                        "name",
                        "reference.resource_id",
                        "account",
                        "provider",
                        "cloud_service_type",
                        "cloud_service_group",
                    ]
                ],
            )

    def _check_compliance_framework(self):
        all_compliance_frameworks = list(COMPLIANCE_FRAMEWORKS[self.provider].keys())
        if self.cloud_service_type not in all_compliance_frameworks:
            raise ERROR_INVALID_PARAMETER(
                key="options.compliance_framework",
                reason=f"Not supported compliance framework. "
                f"(compliance_frameworks = {all_compliance_frameworks})",
            )

    def _covert_options(self, options, secret_data):
        selected_provider = {"aws": "AWS", "google_cloud": "GCP", "azure": "AZR"}.get(
            self.provider
        )

        key_type, diag_data = self._get_key_type(secret_data, selected_provider)

        selected_compliance = options["compliance_framework"]
        compliance = COMPLIANCE_FRAMEWORKS[self.provider][selected_compliance]

        return key_type, compliance, diag_data

    def _get_key_type(self, secret_data, selected_provider):
        if selected_provider == "AWS":
            return self._get_aws_type(secret_data, selected_provider)
        elif selected_provider == "GCP":
            return self._get_gcp_type(secret_data, selected_provider)
        elif selected_provider == "AZR":
            return self._get_azr_type(secret_data, selected_provider)

    def _get_aws_type(self, secret_data, selected_provider):
        if "role_arn" in secret_data:
            key_type = f"{selected_provider}-002"
            diag_data = {
                "arg_1": secret_data["role_arn"],
                "arg_2": secret_data["external_id"],
            }
            diag_data["diag_id"] = hashlib.md5(
                secret_data["role_arn"].encode()
            ).hexdigest()
        else:
            key_type = f"{selected_provider}-001"
            diag_data = {
                "arg_1": secret_data["aws_access_key_id"],
                "arg_2": secret_data["aws_secret_access_key"],
            }
            diag_data["diag_id"] = hashlib.md5(
                secret_data["aws_access_key_id"].encode()
            ).hexdigest()

        return key_type, diag_data

    def _get_gcp_type(self, secret_data, selected_provider):
        key_type = f"{selected_provider}-001"
        key = {
            "auth_provider_x509_cert_url": secret_data["auth_provider_x509_cert_url"],
            "auth_uri": secret_data["auth_uri"],
            "client_email": secret_data["client_email"],
            "client_id": secret_data["client_id"],
            "client_x509_cert_url": secret_data["client_x509_cert_url"],
            "private_key": secret_data["private_key"],
            "private_key_id": secret_data["private_key_id"],
            "project_id": secret_data["project_id"],
            "token_uri": secret_data["token_uri"],
            "type": secret_data["type"],
        }
        diag_data = {
            "arg_1": json.dumps(key),
        }
        diag_data["diag_id"] = hashlib.md5(
            secret_data["auth_provider_x509_cert_url"].encode()
        ).hexdigest()

        return key_type, diag_data

    def _get_azr_type(self, secret_data, selected_provider):
        key_type = f"{selected_provider}-001"
        diag_data = {
            "arg_1": secret_data["client_id"],
            "arg_2": secret_data["tenant_id"],
            "arg_3": secret_data["client_secret"],
            "arg_4": secret_data["subscription_id"],
        }
        diag_data["diag_id"] = hashlib.md5(
            secret_data["client_id"].encode()
        ).hexdigest()

        return key_type, diag_data

    # def _make_compliance_results(self, check_result):
    #     results = []

    #     account_id = check_result.get("diag_id")
    #     payload = check_result.get("payload", {})

    #     findings = payload.get("findings")
    #     for finding in findings:
    #         code = {
    #             "account": account_id,
    #             "name": finding["code"],
    #             "reference": {
    #                 "resource_id": self.cloud_service_type,
    #             },
    #             "data": self._covert_description_to_markdown(finding),
    #             "metadata": {
    #                 "view": {
    #                     "sub_data": {
    #                         "reference": {
    #                             "resource_type": "inventory.CloudServiceType",
    #                             "options": {
    #                                 "provider": self.provider,
    #                                 "cloud_service_group": self.cloud_service_group,
    #                                 "cloud_service_type": self.cloud_service_type,
    #                             },
    #                         }
    #                     }
    #                 }
    #             },
    #             "provider": self.provider,
    #             "cloud_service_group": self.cloud_service_group,
    #             "cloud_service_type": self.cloud_service_type,
    #             "region_code": "global",
    #         }

    #         results.append(code)

    #     return results

    def _covert_dclo_to_spaceOne(self, finding):
        # severity = report_lv
        # service = category
        # ok = stats.checks.fail
        # ok = stats.checks.pass
        # ok = stats.checks.info
        # ok = stats.findings.fail
        # ok = stats.findings.pass
        # ok = stats.findings.info
        # ok = stats.score.fail
        # ok = stats.score.pass

        # 우리꺼 데이터 백업 후
        finding["status_back"] = finding["status"]  # CLEAR | NA 등등
        finding["status"] = (
            "PASS" if finding["flag"] == "Secure" else "FAIL"
        )  # FAIL | PASS
        finding["severity"] = finding["report_lv"].upper()  # MEDIUM | HIGH | LOW
        finding["service"] = finding["category"]

        finding["findings_cnt"] = (
            f"{finding['flag_items']} / {finding['checked_items']}"
            if finding["checked_items"]
            else "-"
        )

        for key in finding:
            if key in [
                "compliance_decs",
                "rule_standard",
                "action_plan",
            ]:
                finding[key] = self._format_text_and_json(finding[key])
            if key in ["flag_key", "good_key"]:
                finding[key] = [
                    {
                        "region": row["region"],
                        "id": row["id"],
                        "name": row["name"],
                        "resource_type": row["resource_type"],
                        "detail": row["detail"],
                        "popup_data": json.dumps(
                            row["findings"], indent=4, separators=(",", ": ")
                        ),
                    }
                    for row in finding[key]
                ]

        return finding

    def _format_text_and_json(self, text):
        text = text.replace("\r\n", " ")
        text = text.replace("b:", "")
        text = text.replace("b-h2:", "")
        text = text.replace("h2:", "")
        text = text.replace("h1:", "")

        return text
