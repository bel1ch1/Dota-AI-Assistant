from zenml import pipeline
from steps.url_extract_step import extract_youtube_video_ids
from steps.extracting_transcriptopn import extracting_transcription
from steps.summarization_step import summarization_step
from steps.dividing_to_domains_step import dividing_to_domains_step

from config.config import trace_config
import time
import os


@pipeline(enable_cache=False)
def data_pipeline(yaml_file_path: str):

    # 1. Read all urls
    video_ids = extract_youtube_video_ids(yaml_file_path)

    # 2. Extracting text from transcriptions
    #    Simple processing of extracted text
    transcriptions = extracting_transcription(video_ids)

    # 3. LLM Summarization and clearing
    # LLM (Summarization)
    summary_texts = summarization_step(transcriptions)

    # 4. Dividing texts into domain knowledge
    # LLM (Structured output) | Parsing
    divided_texts = dividing_to_domains_step(summary_texts)

    # 5. Standardization of text by slang.Correction of incorrect terms.
    # LLM (Correction) # Testing step

    # 6. Dividing each domain into topics that have only one main idea
    #    and extracting names of each topics
    # LLM (Structured output) # Testing step

    # 7. Checking topics for collisions and contradictions
    # LLM (Correction with retrieving from db)

    # 8. Vectorization of relevant topics

    # 9. Loading vectors to the vector Data Base with (tags: domains, metadata: topic name)

if __name__ == "__main__":
    os.environ["LANGSMITH_TRACING"] = "true"
    os.environ["LANGSMITH_API_KEY"] = trace_config.langsmith
    path_to_yaml = "C:/work/Dota-AI-Assistant/scripts/data_ref.YAML" #!!! Need Automation
    data_pipeline(path_to_yaml)
