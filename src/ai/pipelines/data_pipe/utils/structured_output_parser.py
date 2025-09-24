from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List


class Segment(BaseModel):
    domain: str = Field(description="Домен к которому относится сегмент")
    text: str = Field(description="Текст сегмента")


class DomainSegmentation(BaseModel):
    segments: List[Segment] = Field(
        description="Список сегментов текста с названиями доменов"
    )

# Парсер на основе Pydantic модели
segmentation_parser = PydanticOutputParser(pydantic_object=DomainSegmentation)

# example of using a structured output parser
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
