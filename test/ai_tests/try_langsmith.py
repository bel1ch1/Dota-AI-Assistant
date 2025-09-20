from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config.config import ai_config, trace_config
import os

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = trace_config.langsmith

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's request only based on the given context."),
    ("user", "Question: {question}\nContext: {context}")
])

llm = ChatOpenAI(
    model=ai_config.model_name,
    openai_api_key=ai_config.openai_api_key,
    openai_api_base=ai_config.openai_api_base
)
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

question = "Can you summarize this morning's meetings?"
context = "During this morning's meeting, we solved all world conflict."

chain.invoke({"question": question, "context": context})
