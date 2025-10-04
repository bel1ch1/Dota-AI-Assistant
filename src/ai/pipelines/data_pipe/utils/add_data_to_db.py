from vector_db.qdrant_client_wrapper import QdrantWrapperClient
from typing import List, Dict

# за один вызов функции должно призойти добавление только
# для данных одного заголовка внутри одной коллекции

def add_data_to_vector_db(
        collection_name: str,
        data_chunks: List[str],
        metadatas: List[Dict[str, str]],
        ):
    """
    Делает запись данных в векторную базу данных

    Args:
        collection_name: Название домена
        data_chunks: Список текстов разделенных по частям
        metadatas: Названия заголовков для добавляемых текстов

    Returns:
        bool: True если удачно, False если неудачно
    """
    client = QdrantWrapperClient()
    status = client.add_texts(
        collection_name=collection_name,
        new_texts=data_chunks,
        metadatas=metadatas
        )

    return True if status else False
