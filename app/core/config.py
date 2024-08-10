import os
from dotenv import load_dotenv
import yaml

load_dotenv()

YML_PATH = os.getenv("YML_PATH")


with open(YML_PATH, 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

def get_sqlite_path():
    return config['sqlite_path']