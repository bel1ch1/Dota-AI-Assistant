from zenml import pipeline
from ai.pipelines.data_pipe.steps.config_parsing_step import config_parsing_step

@pipeline
def data_pipeline(
    input_file: str = "config.yaml"
):

    # 1. Parsing cfg for extracting urls
    # artifacts: extracted links
    youtube_links, other_links = config_parsing_step(input_file)


    # 2. Selecting a specific crawler

    # 3. Moves the necessary links to their queues
    # artifacts: preprocessed links for each queue

    # 4. Proccesing the links
    # artifacts: data

    # 5. Replenishes Datalake
