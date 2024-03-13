import logging
from spaceone.core.error import *

from src.model.dclo.collector import (
    AWSPluginInfo,
    AzurePluginInfo,
    GoogleCloudPluginInfo,
)


class CollectorManager:
    provider = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.provider = None

    @staticmethod
    def init_response(options: dict) -> dict:
        provider = options.get("provider")
        if provider == "aws":
            response = AWSPluginInfo()
            return response.dict()
        elif provider == "azure":
            response = AzurePluginInfo()
            return response.dict()
        elif provider == "google_cloud":
            response = GoogleCloudPluginInfo()
            return response.dict()
        else:
            raise ERROR_INVALID_PARAMETER(
                key="options.provider", reason="Not supported provider."
            )
