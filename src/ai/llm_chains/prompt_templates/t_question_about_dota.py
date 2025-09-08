from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

def question_about_dota_prompt():
    """Просто промт с интеграцией запроса пользователя."""
    prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(
                """Ты эксперт по компьютерной игре Dota 2. Отвечай на вопросы подробно
                и понятно, используя термины и сленг игры.
                Если у тебя нет точной информации, честно скажи об этом."""
            ),
            HumanMessagePromptTemplate.from_template("{question}")
    ])
    return prompt


def qa_with_retriever():
    """Промпт с дополнительным контекстом на основе данных из ретривера."""
    prompt = ChatPromptTemplate([
        SystemMessagePromptTemplate.from_template(
            """Ты Coach для игры Dota 2. Отвечай на вопрос на основе данных из базы знаний.

            Context: {context}

            Инструкции:
            1. Если с помощью переданного контекста можно ответить на вопрос пользователя,
            то дай четкий и аккуратный ответ на его основе.
            2. Если контекста не хватает для ответа, скажи, что на данный момент не знаешь ответа.
            """
        ),
        HumanMessagePromptTemplate.from_template("{question}"),
    ])
    return prompt
