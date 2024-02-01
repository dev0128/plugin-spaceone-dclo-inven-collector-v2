from src.manager.dclo_manager import COMPLIANCE_FRAMEWORKS
from src.model.plugin_info_model import PluginMetadata


class AWSPluginInfo:
    metadata: PluginMetadata = {
        "options_schema": {
            "required": ["provider", "compliance_framework"],
            "order": ["provider", "compliance_framework"],
            "type": "object",
            "properties": {
                "provider": {
                    "title": "Provider",
                    "type": "string",
                    "default": "aws",
                    "disabled": True,
                },
                "compliance_framework": {
                    "title": "Compliance Framework",
                    "type": "string",
                    "enum": list(COMPLIANCE_FRAMEWORKS["aws"].keys()),
                    "default": "D-CLO Best Practice",
                },
                # "regions": {
                #     "title": "Region Filter",
                #     "type": "array",
                #     "items": {"enum": REGIONS["aws"]},
                # },
                # 'services': {
                #     'title': 'Service',
                #     'type': 'array',
                #     'items': {
                #         'enum': list(SERVICES['aws'].keys())
                #     }
                # },
                # 'severity': {
                #     'title': 'Severity',
                #     'type': 'array',
                #     'items': {
                #         'enum': list(SEVERITIES.keys())
                #     }
                # }
            },
        },
    }


class GoogleCloudPluginInfo:
    metadata = {
        "options_schema": {
            "required": ["provider", "compliance_framework"],
            "order": ["provider", "compliance_framework"],
            "type": "object",
            "properties": {
                "provider": {
                    "title": "Provider",
                    "type": "string",
                    "default": "google_cloud",
                    "disabled": True,
                },
                "compliance_framework": {
                    "title": "Compliance Framework",
                    "type": "string",
                    "enum": list(COMPLIANCE_FRAMEWORKS["google_cloud"].keys()),
                    "default": "D-CLO Best Practice",
                },
            },
        },
    }


class AzurePluginInfo:
    metadata = {
        "options_schema": {
            "required": ["provider", "compliance_framework"],
            "order": ["provider", "compliance_framework"],
            "type": "object",
            "properties": {
                "provider": {
                    "title": "Provider",
                    "type": "string",
                    "default": "azure",
                    "disabled": True,
                },
                "compliance_framework": {
                    "title": "Compliance Framework",
                    "type": "string",
                    "default": "D-CLO Best Practice",
                    "enum": list(COMPLIANCE_FRAMEWORKS["azure"].keys()),
                },
            },
        },
    }
