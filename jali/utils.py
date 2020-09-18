import os
import yaml

from .config import BASE_PATH


def get_tags(filepath=os.path.join(BASE_PATH, 'tags.yml')) -> dict:
    with open(filepath, 'r') as f:
        result = yaml.load(f, Loader=yaml.FullLoader)
    return result


def unindent(string: str) -> str:
    return ''.join(map(str.lstrip, string.splitlines(1)))
