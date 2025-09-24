from config.config import ai_config
from pydantic import BaseModel, Field
from typing import List
from langchain_core.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    PromptTemplate
)


class Segment(BaseModel):
    domain: str = Field(description="Домен к которому относится сегмент")
    text: str = Field(description="Текст сегмента")


class DomainSegmentation(BaseModel):
    segments: List[Segment] = Field(
        description="Список сегментов текста с названиями доменов"
    )

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
Раздели следующий текст на сегменты по следующим доменам:

1. HeroMechanicsTips
   Сюда относится информация, связанная с игрой за конкретных героев Dota 2:
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

---

Требования к сегментации:
- Каждый сегмент должен принадлежать строго одному домену.
- Если часть текста не относится ни к одному домену, её можно игнорировать.
- Сегменты не должны пересекаться и должны покрывать только релевантные куски текста.

Формат вывода (для каждого сегмента):
- domain: выбранный домен
- text: текст сегмента

---

Текст для анализа:
{text}

Формат вывода:
{format_instructions}"""


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
for segment in segments["segments"]:
    if segment["domain"] == 'HeroMechanicsTips':
        hero_mechanics_tips.append(segment["text"])

    elif segment["domain"] == 'MatchActionsTips':
        match_actions.append(segment["text"])

    elif segment["domain"] == 'BaseGameMechanics':
        base_game_mechanics.append(segment["text"])

    elif segment["domain"] == 'ComicStrategies':
        comic_strats.append(segment["text"])

    else:
        error_counter += 1
        continue

print(hero_mechanics_tips[0])
