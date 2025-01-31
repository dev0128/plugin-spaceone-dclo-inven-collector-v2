import json

from spaceone.core.manager import BaseManager
from spaceone.inventory.plugin.collector.lib import *
from spaceone.core.error import ERROR_INVALID_PARAMETER

from src.manager.constant import (
    COMPLIANCE_ICON,
    ISMS,
    REGION,
    SERVICES,
    ISO_27001,
    KISA_CSAP_STD,
    KISA_CSAP_SIM,
    PCI_DSS_4,
    PCI_DSS_3,
    CSP,
    NIS_GOV,
    NIS_PUB,
    NIS_SAAS,
    D_CLO,
)


from ..connector.dclo_connector import DcloConnector


COMPLIANCE_FRAMEWORKS = {
    "aws": {
        ISMS: "SET-00026100",
        ISO_27001: "SET-00026108",
        KISA_CSAP_STD: "SET-00026102",
        KISA_CSAP_SIM: "SET-00026103",
        PCI_DSS_4: "SET-00061100",
        PCI_DSS_3: "SET-00026109",
        CSP: "SET-00026104",
        NIS_GOV: "SET-00026105",
        NIS_PUB: "SET-00026106",
        NIS_SAAS: "SET-00026107",
        D_CLO: "SET-00011014",
    },
    "google_cloud": {
        ISMS: "SET-00028110",
        ISO_27001: "SET-00028114",
        KISA_CSAP_STD: "SET-00028111",
        KISA_CSAP_SIM: "SET-00028112",
        PCI_DSS_4: "SET-00061102",
        PCI_DSS_3: "SET-00028115",
        CSP: "SET-00028113",
        NIS_GOV: "SET-00028116",
        NIS_PUB: "SET-00028117",
        NIS_SAAS: "SET-00028118",
        D_CLO: "SET-00028128",
    },
    "azure": {
        ISMS: "SET-00028119",
        ISO_27001: "SET-00028123",
        KISA_CSAP_STD: "SET-00028120",
        KISA_CSAP_SIM: "SET-00028121",
        PCI_DSS_4: "SET-00028122",
        PCI_DSS_3: "SET-00061103",
        CSP: "SET-00028124",
        NIS_GOV: "SET-00028125",
        NIS_PUB: "SET-00028126",
        NIS_SAAS: "SET-00028127",
        D_CLO: "SET-00028129",
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
            yield from self.collect_cloud_service_type(options, secret_data, schema)
            yield from self.collect_cloud_service(options, secret_data, schema)
        except Exception as e:

            yield make_error_response(
                error=e,
                provider=self.provider,
                cloud_service_group=self.cloud_service_group,
                cloud_service_type=self.cloud_service_type,
            )

    def collect_cloud_service_type(self, options, secret_data, schema):
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
            labels=["Security", "Compliance", "CSPM"],
        )

        # 대쉬보드 명 지정
        dashboard = {"aws": "AWS", "azure": "Azure", "google_cloud": "Google"}
        cloud_service_type["metadata"]["query_sets"][0][
            "name"
        ] = f"D-CLO CSPM {dashboard[self.provider]} ({self.cloud_service_type})"

        # 위젯 지정
        # cloud_service_type["metadata"]["widget"] = METADATA_WIDGET

        # 컴플라이언스 아이콘
        cloud_service_type["tags"] = {
            "spaceone:icon": COMPLIANCE_ICON[self.cloud_service_type]
        }

        yield make_response(
            cloud_service_type=cloud_service_type,
            match_keys=[["name", "group", "provider"]],
            resource_type="inventory.CloudServiceType",
        )

    def collect_cloud_service(self, options, secret_data, schema):
        key_type, compliance, diag_data = self._covert_options(options, secret_data)
        compliance_results = self.dclo_connector.fetch_compliance_results(
            key_type, compliance, diag_data
        )
        account_id = compliance_results["account_id"]

        for finding in compliance_results.get("findings", []):

            # 리전명 통일 하기
            self._covert_region_name(finding)

            cloud_service = make_cloud_service(
                name=finding["code"],
                account=account_id,
                provider=self.provider,
                cloud_service_group=self.cloud_service_group,
                cloud_service_type=self.cloud_service_type,
                region_code=finding["region"],
                data=self._covert_dclo_to_spaceOne(finding),
                reference={
                    "resource_id": f'dclo:{self.provider}:{account_id}:{self.cloud_service_type}:{finding["code"]}'.lower(),
                },
            )

            yield make_response(
                cloud_service=cloud_service,
                match_keys=[
                    [
                        "reference.resource_id",
                        "provider",
                        "cloud_service_type",
                        "cloud_service_group",
                        "account",
                    ]
                ],
            )

    def _covert_region_name(self, finding):
        good_regions = set([item["region"] for item in finding["good_key"]])
        flag_regions = set([item["region"] for item in finding["flag_key"]])

        if self.provider != "azure":
            all_regions = [
                REGION[self.provider].get(region, "---")
                + (
                    f" | {region}"
                    if region not in ["globals", "AllRegions", "global"]
                    else ""
                )
                for region in good_regions | flag_regions
            ]
        else:
            all_regions = [
                (
                    region
                    if region not in ["globals", "AllRegions", "global"]
                    else "Global"
                )
                for region in good_regions | flag_regions
            ]

        if not all_regions:
            all_regions = [""]

        finding["region"] = "multiple" if len(all_regions) > 1 else all_regions[0]

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
        elif "aws_session_token" in secret_data:
            key_type = f"{selected_provider}-003"
            diag_data = {
                "arg_1": secret_data["aws_access_key_id"],
                "arg_2": secret_data["aws_secret_access_key"],
                "arg_3": secret_data["aws_session_token"],
            }
        else:
            key_type = f"{selected_provider}-001"
            diag_data = {
                "arg_1": secret_data["aws_access_key_id"],
                "arg_2": secret_data["aws_secret_access_key"],
            }

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

        return key_type, diag_data

    def _get_azr_type(self, secret_data, selected_provider):
        key_type = f"{selected_provider}-001"
        diag_data = {
            "arg_1": secret_data["client_id"],
            "arg_2": secret_data["tenant_id"],
            "arg_3": secret_data["client_secret"],
            "arg_4": secret_data["subscription_id"],
        }

        return key_type, diag_data

    def _covert_dclo_to_spaceOne(self, finding):

        # 우리꺼 데이터 백업 후
        finding["status_back"] = finding["status"]
        finding["status"] = "FAIL" if finding["flag"] == "Vuln" else "PASS"

        SEVERITIES = {
            "High": "CRITICAL",
            "Medium": "HIGH",
            "Low": "LOW",
        }

        finding["severity"] = SEVERITIES[finding["report_lv"]]
        finding["report_lv"] = SEVERITIES[finding["report_lv"]].capitalize()

        # 서비스명 정리 하기
        finding["service"] = SERVICES[self.provider].get(finding["category"], "---")
        finding["category"] = SERVICES[self.provider].get(finding["category"], "---")

        checked_items = finding["checked_items"]
        if checked_items != "-":
            vul_cnt = int(finding["flag_items"])
            tot_cnt = int(checked_items)
            sec_cnt = tot_cnt - vul_cnt

        finding["vul_cnt"] = vul_cnt if checked_items else "-"
        finding["sec_cnt"] = sec_cnt if checked_items else "-"
        finding["tot_cnt"] = tot_cnt if checked_items else "-"

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
        text = text.replace("\r\n", "")
        text = text.replace("b:", "")
        text = text.replace("b-h2:", "")
        text = text.replace("h2:", "")
        text = text.replace("h1:", "")

        return text
