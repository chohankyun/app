import json
import logging
import os

logger = logging.getLogger(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class EnvJson:
    @staticmethod
    def get(key):
        try:
            env_json = os.path.join(BASE_DIR, '../env.json')
            with open(env_json) as env:
                env_values = json.loads(env.read())
            return env_values[key]
        except Exception as e:
            logging.exception(e)
