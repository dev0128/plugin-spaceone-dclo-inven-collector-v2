from typing import Generator
from spaceone.inventory.plugin.collector.lib.server import CollectorPluginServer

from src.manager.dclo_manager import COMPLIANCE_FRAMEWORKS, DcloManager

app = CollectorPluginServer()


@app.route("Collector.init")
def collector_init(params: dict) -> dict:
    return {
        "metadata": {
            "options_schema": {
                "required": ["provider", "compliance_framework"],
                "order": ["provider", "compliance_framework"],
                "type": "object",
                "properties": {
                    "provider": {
                        "title": "Provider",
                        "type": "string",
                        "default": "aws",
                        "enum": list(COMPLIANCE_FRAMEWORKS.keys()),
                        "disabled": False,
                    },
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


@app.route("Collector.verify")
def collector_verify(params: dict) -> None:
    pass


@app.route("Job.get_tasks")
def job_get_tasks(params: dict) -> dict:
    pass
