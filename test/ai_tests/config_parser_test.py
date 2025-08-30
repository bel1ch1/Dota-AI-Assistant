from ai.pipelines.data_pipe.utils.config_parser import LinkSorter


path_2_yaml = "C:/work/Dota-AI-Assistant/test/ai_tests/data_ref.YAML"
parser = LinkSorter()
parser.parse_yaml(path_2_yaml)
l1, l2 = parser.get_result()
print(f"Ytt: {l1}")
print("=============")
print(f"Other: {l2}")
