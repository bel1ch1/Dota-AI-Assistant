from langchain_core.output_parsers import StrOutputParser
from ai.pipelines.data_pipe.utils.llm_prompt_templates import (
    text_summary_prompt,
    domain_segmentation_prompt
)
from ai.pipelines.data_pipe.utils.llm_model import llm
from ai.pipelines.data_pipe.utils.structured_output_parser import segmentation_parser


def summary_chain(input_text: str):
    """
    Цепочка для суммаризации и очистки текста.
    """
    chain = (
            text_summary_prompt()
            | llm
            | StrOutputParser()
        )
    return chain.invoke({"input_text": input_text})

def domen_segmentation_chain(text: str):
    """
    Цепочка для сегментации текста на домены.

    Returns:
        chain.model_dump()
    """
    chain = (
            domain_segmentation_prompt()
            | llm
            | segmentation_parser
        )
    res = chain.invoke({"text": text})
    return res.model_dump()
