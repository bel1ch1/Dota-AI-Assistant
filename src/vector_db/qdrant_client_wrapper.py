"""
Код для взаимодействия с векторной базой данных Qdrant
"""


from qdrant_client import QdrantClient
from config.config import vector_db_config
from langchain_qdrant import QdrantVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from typing import List, Optional, Dict


class QdrantWrapperClient:
    def __init__(self):
        """
        Класс-Обертка для работы с векторной базой данных Qdrant через LangChain.
        Класс позволяет использовать возможности LangChain, при работе с векторной базой данных
        Qdrant.
        """
        self.db_path: str = vector_db_config.qdrant_path
        self.embedding_model: str = vector_db_config.embedder
        self.url: str = vector_db_config.qdrant_url
        self.client = QdrantClient(
            path=vector_db_config.qdrant_path
        )
        self.embedder = HuggingFaceEmbeddings(
            model_name=vector_db_config.embedder
        )

    def _check_collection_exists(self, collection_name: str) -> bool:
        """
        Проверка, существует ли коллекция в базе данных

        Args:
            collection_name (str): название коллекции

        Returns:
            bool: True - коллекция существует, False - коллекеция не существует
        """
        try:
            self.client.get_collection(collection_name)
            return True
        except Exception:
            return False

    def get_vectorstore(self, collection_name: str) -> QdrantVectorStore:
        """
        Метод для получения экземпляра класса LangChain VectorStore для конкретной коллекции.
        Если коллекции нет, то вернется исключение.

        Args:
            collection_name (str): название коллекции, для которой нужно получить эекземпляр клиента

        Returns:
            QdrantVectorStore: Экземпляр класса обертки над клиентом qdrant
        """
        if not self._check_collection_exists(collection_name):
            raise ValueError(f"Collection {collection_name} does not exist")
        return QdrantVectorStore(
            client=self.client,
            collection_name=collection_name,
            embedding=self.embedder
        )

    def add_texts(
            self,
            collection_name: str,
            new_texts: List[str],
            metadatas: Optional[List[Dict]] = None,
        ) -> bool:
        """
        Метод для добавления новых данных в существующую коллекцию.
        Если коллекции нет, то вернется исключение.

        Args:
            collection_name (str): название коллекции
            new_texts List[str]: текста, которые нужно добавить в индекс векторного хранилища
            metadatas List[Dict]: дополнительная информация для передаваемых текстов

        Returns
            bool: True - если удачно, False - если неудачно
        """
        try:
            vectorstore = self.get_vectorstore(collection_name)
            vectorstore.add_texts(
                texts=new_texts,
                metadatas=metadatas
            )
            self.client_close()

            return True
        except Exception as e:
            print(f"Error when adding data: {e}")
            self.client_close()
            return False

    def similarity_search(
            self,
            collection_name: str,
            query: str,
            k: int = 3,
        ):
        """
        Метод выполняет поиск по существующей коллекции.
        Если коллекции нет, то вернется исключение.

        Args:
            collection_name (str): название коллекции
            query (str): Запрос, на основе которого нужно провести поиск
            k (int): Количество релевантных документов, которое будет возвращено

        Returns:
            List: список результатов в количестве k
        """
        vectorstore = self.get_vectorstore(collection_name)
        return vectorstore.similarity_search(query=query, k=k)

    def client_close(self) -> None:
        """
        Корректное отключение клиента.
        """
        if self.client:
            self.client.close()
        else:
            print("Сlient is already closed")

# Usage Example ----------------------------------------------------------------------------------#
# Add new documents
# client = QdrantWrapperClient()
# status = client.add_texts(
#     collection_name="ComicStrategies",
#     new_texts=["Эмблемы дают больше баллов, чем титулы.","Эмблемы важнее, чем титулы."],
#     metadatas=[
#         {
#             "title": "Ограничения и оптимальные наборы"
#         }
#     ]
# )
# print(status)
# client.client_close()

# Vector Search
# client = QdrantWrapperClient()
# resoult = client.similarity_search(
#     collection_name="ComicStrategies",
#     query="Эмблемы и былы или титулы",
#     k=1
# )
# client.client_close()
# print(resoult)
# ------------------------------------------------------------------------------------------------#
# qdrant_client = QdrantClient()

# qdrant_client.add_texts(
#     collection_name="collection",
#     new_texts=["example"],
#     metadatas=[
#         {
#             "title":"example",
#         }
#     ]
# )
# res = qdrant_client.similarity_search(
#     collection_name="collection",
#     query="example"
# )
# for doc in res:
#     print(f"Text: {doc.page_content}, Metadata: {doc.metadata}")
# end of usage example ---------------------------------------------------------------------------#
