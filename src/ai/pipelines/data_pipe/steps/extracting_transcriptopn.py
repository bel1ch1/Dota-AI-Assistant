from zenml import step
from ai.pipelines.data_pipe.utils.ytt_crawler import YT_Crawler
from typing import List

@step
def extracting_transcription(video_ids: List[str]):
    crawler = YT_Crawler(video_ids, ['ru'])
    text = crawler.get_transcriptions()
    cleared_text = crawler.clear_yt_text()
    return cleared_text
