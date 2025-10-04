from zenml import step
from typing import Dict, List
from ai.pipelines.data_pipe.utils.add_data_to_db import add_data_to_vector_db
from ai.pipelines.data_pipe.utils.divide_to_chunks import get_chunks


@step
def vectorization_step(segments: List[Dict]):
    """
    Шаг делит данные на чанки и сохраняет их.

    Args:
        segments: Список словарей, где каждый словарь это данные из одного домена.
    """
    hero_mechanics_tips = []
    base_game_mechanics = []
    match_actions_tips = []
    comic_strategies = []

    # Парсинг структуры
    for segment in segments:
        if segment["domain"] == "HeroMechanicsTips":
            hero_mechanics_tips = segment["topics"]
        if segment["domain"] == "BaseGameMechanics":
            base_game_mechanics = segment["topics"]
        if segment["domain"] == "MatchActionsTips":
            match_actions_tips = segment["topics"]
        if segment["domain"] == "ComicStrategies":
            comic_strategies = segment["topics"]

    for topic in hero_mechanics_tips:
        title = topic["title"] # заголовок
        data = topic["text"]   # текст топика
        chunked_texts = get_chunks(data, 5)
        texts_count = len(chunked_texts)
        status = add_data_to_vector_db(
            collection_name="HeroMechanicsTips",
            data_chunks=chunked_texts,
            metadatas=[{"title": title}] * texts_count
        )
        print(f"The status of adding to the collection: HeroMechanicsTips by title:{title}: {status}")

    for topic in base_game_mechanics:
        title = topic["title"] # metadata
        data = topic["text"]   # data
        chunked_texts = get_chunks(data, 5)
        texts_count = len(chunked_texts)
        status = add_data_to_vector_db(
            collection_name="BaseGameMechanics",
            data_chunks=chunked_texts,
            metadatas= [{"title": title}] * texts_count
        )
        print(f"The status of adding to the collection: BaseGameMechanics by title:{title}: {status}")

    for topic in match_actions_tips:
        title = topic["title"] # metadata
        data = topic["text"]   # data
        chunked_texts = get_chunks(data, 5)
        texts_count = len(chunked_texts)
        status = add_data_to_vector_db(
            collection_name="MatchActionsTips",
            data_chunks=chunked_texts,
            metadatas=[{"title": title}] * texts_count
        )
        print(f"The status of adding to the collection: MatchActionsTips by title:{title}: {status}")

    for topic in comic_strategies:
        title = topic["title"] # metadata
        data = topic["text"]   # data
        chunked_texts = get_chunks(data, 5)
        texts_count = len(chunked_texts)
        status = add_data_to_vector_db(
            collection_name="ComicStrategies",
            data_chunks=chunked_texts,
            metadatas=[{"title": title}] * texts_count
        )
        print(f"The status of adding to the collection: ComicStrategies by title:{title}: {status}")
