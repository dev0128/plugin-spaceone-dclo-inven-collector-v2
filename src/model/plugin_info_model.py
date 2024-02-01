from pydantic import BaseModel


class PluginMetadata(BaseModel):
    options_schema: dict


class PluginInfo(BaseModel):
    metadata: PluginMetadata
