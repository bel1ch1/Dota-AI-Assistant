from zenml import step
from ai.pipelines.data_pipe.utils.ytt_crawler import YT_Crawler
from typing import List

@step
def extracting_transcription(video_ids: List[str]) -> List[str]:
    """
    Извлекает транскрипции из видео по переданным id.
    Проводит отчистку текста от системного мусора.

    Args:
        video_ids (List[str]): Список id видео

    Returns:
        List[str]: Список транскрипций, которые получилось извлечь.
    """
    crawler = YT_Crawler(video_ids, ['ru'])
    text = crawler.get_transcriptions()
    cleared_text = crawler.clear_yt_text()
    return cleared_text
