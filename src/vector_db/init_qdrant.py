"""
Код для инициализации локального векторного хранилища Qdrant, с 4 коллекциями.
"""


from config.config import vector_db_config
from qdrant_client import QdrantClient, models
from typing import List


class QdrantInitializer:
    def __init__(self):
        self.db_path = vector_db_config.qdrant_path
        self.client = None
        self.embedder = vector_db_config.embedder
        self.vector_size = vector_db_config.vector_size
        self.vector_stores = {}

    def initialize_client(self):
        """
        Инициализация клиента Qdrant

        Returns:
            bool: True - если удачно, False - если неудачно
        """
        try:
            self.client = QdrantClient(path=self.db_path)
            print("✓ Qdrant client has been initialized!")
            return True
        except Exception as e:
            print(f"✗ Error of Initialization: {e}")
            return False

    def create_collection(self, collection_name: str) -> bool:
        """
        Создание новой коллекции

        Args:
            collection_name (str): Название коллекции для создания.

        Returns:
            bool: True - если удачно, False - если неудачно
        """
        try:
            self.client.recreate_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(
                    size=self.vector_size,
                    distance=models.Distance.COSINE
                )
            )
            print(f"✓ Collection {collection_name} has been created")
            return True
        except Exception as e:
            print(f"✗ Error of collection creation: {e}")
            return False

    def setup_base_collections(self) -> List[str]:
        """
        Создание базовых коллекций для разных доменов

        Returns:
            List[str] - список созданных коллекций
        """
        domains = ["HeroMechanicsTips", "MatchActionsTips", "BaseGameMechanics", "ComicStrategies"]

        for domain in domains:
            self.create_collection(domain)

        print("✓ Collections was created")
        return domains

    def client_close(self):
        if self.client:
            self.client.close()
        else:
            print("Сlient is already closed")


if __name__ == "__main__":
    initializer = QdrantInitializer()

    if initializer.initialize_client():
        domains = initializer.setup_base_collections()
        print(f"Domains created: {domains}")
    initializer.client_close()
