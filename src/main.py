from typing import Generator
from spaceone.inventory.plugin.collector.lib.server import CollectorPluginServer
from src.manager.collector_manager import CollectorManager

from src.manager.dclo_manager import DcloManager

app = CollectorPluginServer()


@app.route("Collector.init")
def collector_init(params: dict) -> dict:
    """init plugin by options

    Args:
        params (dict): {
            'options': 'dict',
            'domain_id': 'str'

    Returns:
        plugin_data (dict)
    """

    options = params.get("options", {})

    collector_mgr = CollectorManager()
    return collector_mgr.init_response(options)


@app.route("Collector.collect")
def collector_collect(params: dict) -> Generator[dict, None, None]:
    options = params["options"]
    secret_data = params["secret_data"]
    schema = params.get("schema")

    dclo_mgr = DcloManager()

    return dclo_mgr.collect_resources(options, secret_data, schema)
