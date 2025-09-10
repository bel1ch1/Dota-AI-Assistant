from youtube_transcript_api import YouTubeTranscriptApi
from  typing import List
import re

class YT_Crawler:
    """Класс для создания сборщика текстовых данных из видео из youtube"""
    def __init__(self, video_ids: List[str], languages: List[str] = ['ru']) -> List[str]:
        """Конструктор класса для сбора текста транскрипций из видео.
        Args:
            video_ids (list[str]): список специализированный id видео с youtube
            lang (list[str]): параметр языка. Пример ['ru']
        """
        # Определяем сборщик
        self.ytt_api = YouTubeTranscriptApi()
        self.video_ids = video_ids
        self.lang = languages
        self.transcriptions = [] # result transcriptions


    def get_transcriptions(self) -> List[str]:
        """Метод для получения неочищенных транскрипций для каждого video_id.
        Returns:
            dirty_texts (list[str]): Не очищенные текста из видео
        """
        if not self.video_ids:
            print('err: Нет переданных video_ids')
            return []

        for video_id in self.video_ids:
            print(f"Processing video: {video_id}")

            fetched_transcript = self.ytt_api.fetch(video_id, self.lang)
            transcript_text = " ".join([snippet.text for snippet in fetched_transcript])
            if transcript_text:
                self.transcriptions.append(transcript_text)

        return self.transcriptions

    def clear_yt_text(self) -> List[str]:
        """
        Метод для первичной обработки полученных текстов

        Returns:
            List[str]: Список из первично обработанных транскрипций видео.
        """
        processed_transcriptions = []
        patterns = [
            r'\([^()]*\)',  # Круглые скобки
            r'\{[^{}]*\}',  # Фигурные скобки
            r'\[[^\[\]]*\]'  # Квадратные скобки
        ]

        for transcript in self.transcriptions:
            cleaned_text = transcript
            for pattern in patterns:
                cleaned_text = re.sub(pattern, '', cleaned_text)
            # Убираем лишние пробелы
            cleaned_text = ' '.join(cleaned_text.split())
            processed_transcriptions.append(cleaned_text)

        return processed_transcriptions

# ids = ["0pDq24BRxO8"]
# crawler = YT_Crawler(ids, ['ru'])
# text = crawler.get_transcriptions()
# print(len(text[0]))
# cleared_text = crawler.clear_yt_text()
# print(cleared_text)
# print(len(cleared_text[0]))
