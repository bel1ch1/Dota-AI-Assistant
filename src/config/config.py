from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class ConfigBase(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="C:/work/Dota-AI-Assistant/.env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

class TelegramConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="tg_")

    bot_token: str

class AiConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="ai_")

    openai_api_base: str
    openai_api_key: str
    model_name: str
    embedder: str

# class TraceConfig(ConfigBase):
#     model_config = SettingsConfigDict(env_prefix="trace_")

#     langsmith_api_key: str


tg_config = TelegramConfig()
ai_config = AiConfig()
# trace_config = TraceConfig()
