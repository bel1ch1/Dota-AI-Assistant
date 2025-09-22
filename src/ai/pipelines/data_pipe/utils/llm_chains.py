from langchain_core.output_parsers import StrOutputParser
from ai.pipelines.data_pipe.utils.llm_prompt_templates import (
    text_summary_prompt,
    domain_segmentation_prompt
)
from ai.pipelines.data_pipe.utils.llm_model import llm


def summary_chain(input_text):
    """

    """
    chain = (
            text_summary_prompt()
            | llm
            | StrOutputParser()
        )
    return chain.invoke({"input_text": input_text})

def domen_segmentation_chain(input_text):
    """

    """
    chain = (
            domain_segmentation_prompt()
            | llm
        )
    return chain.invoke({"input_text": input_text})
