import json

import requests


def get_data_from_url(url, as_json=True):
    response = requests.get(url)
    data = response.text
    if as_json:
        return json.loads(data)
    return data
        