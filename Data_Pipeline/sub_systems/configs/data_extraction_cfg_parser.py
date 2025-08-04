import yaml
from pydantic import BaseModel


class ExtractData(BaseModel):
    url: str


def load_cfg(config_name: str):
    """Parses the configuration file for extracting data.
    Args:
        config_name: str - Name of the config"""
    try:
        with open(config_name, "r", encoding="utf-8") as f:
            cfg_raw = yaml.load(f)

        return cfg_raw

    except:
        print("err")
