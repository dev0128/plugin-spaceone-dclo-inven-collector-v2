import logging
import requests
import json

from time import sleep

from spaceone.core.error import (
    ERROR_REQUIRED_PARAMETER,
    ERROR_REQUEST_TIMEOUT,
    ERROR_TASK_METHOD,
)
from spaceone.core.connector import BaseConnector

_LOGGER = logging.getLogger(__name__)


PENDING_SECOND = 60
TIME_LIMIT_MINUTE = 30
DCLO_PLUGIN_URL = "https://spaceone.d-clo.com/diag"


class DcloConnector(BaseConnector):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def verify_client(self, options: dict, secret_data: dict, schema: str):
        self._check_options_data(options)
        self._check_secret_data(secret_data)

    def fetch_compliance_results(self, key_type, compliance, diag_data) -> dict:
        param = {
            **diag_data,
            "type": key_type,
            "ruleset_id": compliance,
        }

        result = {}

        res = requests.post(
            f"{DCLO_PLUGIN_URL}/request",
            headers={"Content-Type": "application/json"},
            data=json.dumps(param),
        )
        waiting_timer = 0

        while True:
            sleep(PENDING_SECOND)
            waiting_timer += PENDING_SECOND

            res = requests.get(f"{DCLO_PLUGIN_URL}/result/{diag_data['diag_id']}")
            content = json.loads(res.content)
            status = content.get("status")

            if status == "end":
                result = content.get("result", {})
                break
            if status == "error":
                raise ERROR_TASK_METHOD(
                    name="D-CLO",
                    method="fetch_compliance_results",
                    params="options.provider",
                )

            if waiting_timer > PENDING_SECOND * TIME_LIMIT_MINUTE:
                raise ERROR_REQUEST_TIMEOUT(key="options.provider")

        return diag_data["diag_id"], result

    @staticmethod
    def _check_options_data(options: dict):
        if "provider" not in options:
            raise ERROR_REQUIRED_PARAMETER(key="options.provider")

        if "compliance_framework" not in options:
            raise ERROR_REQUIRED_PARAMETER(key="options.compliance_framework")

    @staticmethod
    def _check_secret_data(secret_data: dict):
        if "aws_access_key_id" not in secret_data:
            raise ERROR_REQUIRED_PARAMETER(key="secret_data.aws_access_key_id")

        if "aws_secret_access_key" not in secret_data:
            raise ERROR_REQUIRED_PARAMETER(key="secret_data.aws_secret_access_key")
