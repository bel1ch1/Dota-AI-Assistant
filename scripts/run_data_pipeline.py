# Тут запуск готового пайплайна
from src.ai.pipelines.data_pipe.data_pipe import data_pipeline

if __name__ == "__main__":
    path_to_yaml = "C:/work/Dota-AI-Assistant/scripts/data_ref.YAML"
    data_pipeline(yaml_file_path=path_to_yaml)
