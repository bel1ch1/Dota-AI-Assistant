from zenml import pipeline
from ai.pipelines.data_pipe.steps.url_extract_step import extract_youtube_video_ids
from ai.pipelines.data_pipe.steps import extracting_transcriptopn

@pipeline()
def data_pipeline(yaml_file_path):

    # 1. Read all urls
    video_ids = extract_youtube_video_ids(yaml_file_path)

    # 2. Extracting text from transcriptions
    #    Simple processing of extracted text
    transcriptions = extracting_transcriptopn(video_ids)

    # 3. LLM Summarization and clearing
    #    Dividing texts into domain knowledge

    # 4. Dividing each domain into topics that have only one main idea
    #    and extracting names of each topics

    # 5. Checking topics for collisions and contradictions

    # 6. Vectorization of relevant topics

    # 7. Loading vectors to the vector Data Base with (tags: domains, metadata: topic name)
