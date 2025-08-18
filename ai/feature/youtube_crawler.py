from youtube_transcript_api import YouTubeTranscriptApi

class YT_Crawler:
    """Класс для создания сборщика текстовых данных из видео из youtube"""
    def __init__(self, video_ids: list[str], languages: list[str]) -> list[str]:
        """Конструктор класса для сбора текста транскрипций из видео.
        Args:
            video_ids (list[str]): список специализированный id видео с youtube
            lang (list[str]): параметр языка. Пример ['ru']
        Returns:
            texts (list[str]): первично обработанные транскрипции из видео
        """
        # Определяем сборщик
        self.ytt_api = YouTubeTranscriptApi()
        self.video_ids = video_ids
        self.lang = languages

    def get_transcriptions(self) -> list[str]:
        """Метод для получения неотчищенных транскрипций из видео.
        Returns:
            dirty_texts (list[str]): Не отчищенные текста из видео
        """
        output = [] # result transcriptions
        if not self.video_ids:
            return print('err')
        for video_id in self.video_ids:
            transcript_list  = self.ytt_api.list(video_id)
            for transcript in transcript_list:
                if transcript.language_code in self.lang:
                    fetched_transcript = self.ytt_api.fetch(video_id, languages=self.lang)
                    if fetched_transcript:
                        output.append(transcript)
                    else:
                        print("Пустая транскрипция")
                else:
                    print("Нет транскрипции на указаннм языке")
        return output

    def clear_yt_text():
        """Метод для первичной обработки полученных текстов"""
        pass
