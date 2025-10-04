from zenml import step
from typing import List, Dict
from ai.pipelines.data_pipe.utils.llm_chains import domen_segmentation_chain
import time


@step
def dividing_to_domains_step(summary_texts: List[str]) -> List[Dict]:
    """
    Соотносит части информации из текстов с нужными доменами.

    Args:
        summary_texts: Список суммаризированных текстов

    Retrurns:
        List[Dict]: Список словарей, где каждый словарь хранит domain и topics
    """

    time.sleep(10)
    segmented = domen_segmentation_chain(summary_texts)
    segments = [
        {"domain": data["domain"], "topics": data["topics"]}
        for data in segmented["segments"]
    ]
    return segments
