from zenml import pipeline
from steps.url_extract_step import extract_youtube_video_ids
from steps.extracting_transcriptopn import extracting_transcription
from steps.summarization_step import summarization_step # Проблема тут


@pipeline(enable_cache=False)
def data_pipeline(yaml_file_path: str):

    # 1. Read all urls
    video_ids = extract_youtube_video_ids(yaml_file_path)

    # 2. Extracting text from transcriptions
    #    Simple processing of extracted text
    transcriptions = extracting_transcription(video_ids)

    # 3. LLM Summarization and clearing
    summary_texts = summarization_step(transcriptions)
    print(summary_texts)
    # 4. Dividing texts into domain knowledge

    # 5. Standardization of text by slang

    # 6. Dividing each domain into topics that have only one main idea
    #    and extracting names of each topics

    # 7. Checking topics for collisions and contradictions

    # 8. Vectorization of relevant topics

    # 9. Loading vectors to the vector Data Base with (tags: domains, metadata: topic name)

if __name__ == "__main__":
    path_to_yaml = "C:/work/Dota-AI-Assistant/scripts/data_ref.YAML"
    data_pipeline(path_to_yaml)
