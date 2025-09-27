from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List


class Topic(BaseModel):
    title: str = Field(description="Название темы")
    text: str = Field(description="Текст темы")

class Domain(BaseModel):
    domain: str = Field(description="Домен к которому относится сегмент")
    topics: List[Topic] = Field(
        description="Список тем относящихся к определенному домену"
    )

class DomainSegmentation(BaseModel):
    segments: List[Domain] = Field(
        description="Список доменов, содержащих топики"
    )

# class TopicSegment(BaseModel):
#     title: str = Field(description="Короткое название темы")
#     text: str = Field(description="Текст сегмента")

# class TopicSegmentation(BaseModel):
#     segments: List[TopicSegment] = Field(
#         description="Список сегментов текста с названиями тем"
#     )

# Парсер на основе Pydantic модели
domain_segmentation_parser = PydanticOutputParser(pydantic_object=DomainSegmentation)
# topic_segmentation_parser = PydanticOutputParser(pydantic_object=TopicSegmentation)

# example of using a structured output parser #####################################################
# chain = (
#     prompt
#     | model
#     | parser
# )

# result = chain.invoke({
#     "text": text,
#     "format_instructions": parser.get_format_instructions()
# })

# print(result.model_dump_json()) # json str
# pring(result.model_dump()) # python.dict
