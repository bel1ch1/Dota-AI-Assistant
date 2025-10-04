"""функция для формирования чанков для одной темы"""


import re
from typing import List


def get_chunks(text: str, min_length: int) -> List[str]:
    """
    Функция для формирования и очистки чанков

    Args:
        text: строка с текстом относящимся к заголовку
        min_length:

    Returns:
        List[str]: Список обработанных чанков для одной темы
    """
    cleaned_text = re.sub(r'[*\n-]', ' ', text)

    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

    sentences = re.split(r'[.!?]+', cleaned_text)

    sentences = [sentence.strip() for sentence in sentences
                if sentence.strip() and len(sentence.strip()) > min_length]

    return sentences
