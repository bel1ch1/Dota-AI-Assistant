"""
Модуль для работы с моделями.
"""


from langchain_openai import ChatOpenAI
from config.config import ai_config


llm = ChatOpenAI(
    model=ai_config.model_name,
    openai_api_key=ai_config.openai_api_key,
    openai_api_base=ai_config.openai_api_base,
    temperature=0,
    max_tokens=4000,        # Максимальное количество токенов
    timeout=30,             # Таймаут в секундах
    max_retries=2           # Количество попыток повтора
)
