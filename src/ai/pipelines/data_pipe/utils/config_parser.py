from ruamel.yaml import YAML
from urllib.parse import urlparse
from typing import Tuple, List, Any

class LinkSorter:
    def __init__(self):
        self.youtube_links: List[str] = []
        self.other_links: List[str] = []
        self.yaml = YAML()

    def _is_youtube_link(self, url: str) -> bool:
        """Проверяет, относится ли ссылка к youtube.

        Args:
            url (str): ссылка на ресурс.

        Returns:
            bool: принадлежит youtube или нет.
        """
        try:
            parsed_url = urlparse(url)

            return (
                parsed_url.netloc.endswith('www.youtube.com') or
                parsed_url.netloc.endswith('youtube.com') or
                parsed_url.netloc.endswith('youtu.be') or
                'youtube.com' in parsed_url.netloc
            )
        except:
            return False

    def _extract_links(self, data: Any) -> None:
        """Рекурсивно извлекает ссылки из YAML.

        Args:
            data (Any): данные из YAML парсера.
        """
        # Проверка данных на формат ссылок
        if isinstance(data, dict):
            for key, value in data.items():
                print(f"key = {key}, valie = {value}")
                if key == 'ref' and isinstance(value, str) and value.startswith('http'):
                    self._add_link(value)
        elif isinstance(data, list):
            for item in data:
                self._add_link(item)
        elif isinstance(data, str) and data.startswith('http'):
            self._add_link(data)

    def _add_link(self, url: str) -> None:
        """Добавляет в ссылку в свой список.

        Args:
            url (str): текущая ссылка.
        """
        if self._is_youtube_link(url):
            self.youtube_links.append(url)
        else:
            self.other_links.append(url)

    def parse_yaml(self, file_path: str) -> None:
        """Извлекает ссылки из YAML"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = self.yaml.load(f)
                self._extract_links(data)
                print("Успешно")

        except Exception as e:
            print(f"Ошибка при парсинге файла: {e}")


    def get_result(self) -> Tuple[List[str], List[str]]:
        """Возвращает результаты в двух списках."""
        return self.youtube_links, self.other_links
