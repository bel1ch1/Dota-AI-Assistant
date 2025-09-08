from ruamel.yaml import YAML
from urllib.parse import urlparse, parse_qs
from typing import List
from zenml import step

@step
def extract_youtube_video_ids(yaml_file: str) -> List[str]:
    """
    Функция для извлечения id видео из YAML-файла.

    Args:
        yaml_file (str): YAML-файл с ссылками на видео.

    Returns:
        List[str]: Список id видео.
    """
    yaml = YAML()
    with open(yaml_file, 'r', encoding='utf-8') as f:
        urls = yaml.load(f) or []

    video_ids = []
    for url in urls:
        if 'https://www.youtube.com' in url:
            parsed = urlparse(url)
            params = parse_qs(parsed.query)
            if 'v' in params:
                video_ids.append(params['v'][0])

    return video_ids

# res = extract_youtube_video_ids("data_ref.YAML")
# print(res)
