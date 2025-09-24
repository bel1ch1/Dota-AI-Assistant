from zenml import step
from ai.pipelines.data_pipe.utils.llm_chains import summary_chain
from typing import List
import time


@step()
def summarization_step(texts: List[str]) -> List[str]:
    """
    Обрабатывает несколько текстов, убирая воду и информацию не по теме.

    Args:
        texts (List[str]): Список текстов транскрипций из видео.

    Returns:
        List[str]: Список суммаризированных текстов
    """
    summary_texts = []
    for text in texts:
        if not text:
            continue
        summary_texts.append(summary_chain(text))
        time.sleep(10)

    return summary_texts
