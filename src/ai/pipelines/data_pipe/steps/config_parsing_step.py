from zenml import step
from utils.config_parser import LinkSorter

@step
def config_parsing_step(input_yaml_file: str):
    extractor = LinkSorter()
    extractor.parse_yaml(file_path=input_yaml_file)
    return extractor.get_result()
