from config.config import ai_config
from pydantic import BaseModel, Field
from typing import List
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    PromptTemplate
)
import os
from config.config import trace_config


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

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = trace_config.langsmith

# Парсер на основе Pydantic модели
segmentation_parser = PydanticOutputParser(pydantic_object=DomainSegmentation)


llm = ChatOpenAI(
    model=ai_config.model_name,
    openai_api_key=ai_config.openai_api_key,
    openai_api_base=ai_config.openai_api_base,
    temperature=0,
    max_tokens=4000,        # Максимальное количество токенов
    timeout=30,             # Таймаут в секундах
    max_retries=2           # Количество попыток повтора
)

system_prompt ="""
Ты - эксперт по анализу и структурированию текстовой информации, специализирующийся на
тематике Dota 2.

Твоя задача:
1. Определить область знаний (домен), к которому относится часть текста
2. В каждом домене выделить отдельные топики.
3. Для каждой темы придумать заголовок, который описывает ее содержание и принадлежность. Например,
если часть текста относится к HeroMechanicsTips или к варианту MatchActionsTips, в котором
описываются советы по действиям при игре за героя, то в заголовке должна быть указана информация
о том, к какому герою относятся эти советы.

Всего возможно 4 домена:
1. HeroMechanicsTips
   Сюда относится информация, связанная с героями Dota 2:
   - сборки предметов
   - прокачка способностей
   - особенности героев и их механики

2. MatchActionsTips
   Сюда относится стратегическая информация о действиях в матчах:
   - тактические советы
   - стиль игры
   - принятие решений для достижения победы

3. BaseGameMechanics
   Сюда относится общая информация об игре, не относящаяся к героям или стратегиям:
   - количество и расположение объектов на карте
   - оптимальные маршруты фарма
   - преимущества от контроля над целевыми объектами

4. ComicStrategies
   Сюда относятся шуточные или нестандартные стратегии, не направленные на победу, а на развлечение.

Формируй информацию в topics так, чтобы она была

---

Требования к сегментации:
- Каждый сегмент должен принадлежать строго одному домену.
- Если часть текста не относится ни к одному домену, её можно игнорировать.
- Сегменты не должны пересекаться и должны покрывать только релевантные куски текста.

Формат вывода для каждого сегмента:
- domain: выбранный домен
- topics: список тем относящихся к домену

Формат вывода для каждого топика:
- title: заголовок описывающий тему
- text: текст относящийся к теме

---

Формат вывода должен строго соответствовать следующей схеме:
{format_instructions}

Текст для анализа:
{text}
"""


text = """Earthshaker (Эхослэм) в новом патче получил изменения в аспектах:
- Врождённая способность теперь наносит урон и отталкивает врагов/крипов при убийстве цели
- Левый аспект увеличивает радиус авторшока на 40 за каждый уровень эхослема
- Правый аспект добавляет фиссуре волны хаслема с 60% урона

Скилы:
1. Фиссура - урон, стан и создает преграду
2. Тотем - усиливает белый урон (от статов)
3. Авторшок - стан и урон, работает со всеми скилами
4. Эхослем - массовый урон и контроль

Билд:
- Основные предметы: блинк, кая, шардик
- Агоним усиливает тотем (добавляет прыжок и сплэш 40%)
- Шард усиливает фиссуру (добавляет стан через авторшок)

Раскачка:
- Офлейн: максимизация фиссуры → тотем
- Мид: максимизация тотема → пассивка → фиссура
- Таланты: левый-левый-правый-правый (на 25 уровне оба варианта viable)

Стратегия:
- Герой-прокастер с контролем
- Эффективен против групп врагов
- Требует правильного позиционирования и использования комбо (блинк → эхослем → авторшок)"""

prompt = PromptTemplate(
    template=system_prompt,
    input_variables=["text"],
    partial_variables={"format_instructions": segmentation_parser.get_format_instructions()}
)

chain = (
    prompt
    | llm
    | segmentation_parser
)

res = chain.invoke({"text": text})

segments = res.model_dump()


hero_mechanics_tips = []
match_actions = []
base_game_mechanics = []
comic_strats = []
error_counter = 0
# parsing model output
# for segment in segments["segments"]:
#     if segment["domain"] == 'HeroMechanicsTips':
#         segment["topic"]

#     elif segment["domain"] == 'MatchActionsTips':
#         match_actions.append(segment["text"])

#     elif segment["domain"] == 'BaseGameMechanics':
#         base_game_mechanics.append(segment["text"])

#     elif segment["domain"] == 'ComicStrategies':
#         comic_strats.append(segment["text"])

#     else:
#         error_counter += 1
#         continue

# print(hero_mechanics_tips[0])
