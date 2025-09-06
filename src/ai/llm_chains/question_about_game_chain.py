from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
    )
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from config.config import ai_config

class QuestionAboutGameChain:
    def __init__(self):
        self.llm = ChatOpenAI(
            model=ai_config.model_name,
            openai_api_key=ai_config.openai_api_key,
            openai_api_base=ai_config.openai_api_base,
            temperature=0,
            max_tokens=1000,
            timeout=30,
            max_retries=2
        )

        self.prompt = ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(
                """Ты эксперт по компьютерной игре Dota 2. Отвечай на вопросы подробно
                и понятно, используя термины и сленг игры.
                Если у тебя нет точной информации, честно скажи об этом."""
            ),
            HumanMessagePromptTemplate.from_template("{question}")
        ])


        self.chain = (
            RunnablePassthrough()
            | self.prompt
            | self.llm
            | StrOutputParser()
        )

        self.resilent_chain = self.chain.with_fallbacks([
            RunnableLambda(self._fallback_response)
        ])

    def _fallback_response(self, input_dict: dict) -> str:
        """Фолбэк ответ при ошибках"""
        question = input_dict.get("question", "Неизвестный вопрос")
        return f"""Извините, возникли временные проблемы с обработкой вашего вопроса о Dota 2:
        '{question}'. Попробуйте задать вопрос немного позже."""

    async def get_answer(self, question: str) -> str:
        try:
            response = await self.resilent_chain.ainvoke({
                "question": f"{question}\n\nОтветь на этот вопрос как эксперт по Dota 2:"
            })
            return response
        except Exception as e:
            error_msg = f"Произошла ошибка при обработке запроса: {str(e)}"
            return self._fallback_response({"question": question}) + f"\n\nТехническая информация: {error_msg}"
