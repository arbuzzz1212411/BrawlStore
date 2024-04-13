import json
import os


current_directory = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_directory, 'responses.json')


def get_responses(key: str):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        responses = json.load(file)

    return responses[key]


