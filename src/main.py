from typing import Generator
from spaceone.inventory.plugin.collector.lib.server import CollectorPluginServer

from src.manager.dclo_manager import COMPLIANCE_FRAMEWORKS, DcloManager

app = CollectorPluginServer()


@app.route("Collector.init")
def collector_init(params: dict) -> dict:
    return {
        "metadata": {
            "options_schema": {
                "required": ["compliance_framework"],
                "order": ["compliance_framework"],
                "type": "object",
                "properties": {
                    "compliance_framework": {
                        "title": "Compliance Framework",
                        "type": "string",
                        "enum": list(COMPLIANCE_FRAMEWORKS["aws"].keys()),
                        "default": "D-CLO Best Practice",
                    },
                },
            },
        }
    }


@app.route("Collector.collect")
def collector_collect(params: dict) -> Generator[dict, None, None]:
    options = params["options"]
    secret_data = params["secret_data"]
    schema = params.get("schema")

    dclo_mgr = DcloManager()

    return dclo_mgr.collect_resources(options, secret_data, schema)
