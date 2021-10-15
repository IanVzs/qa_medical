import json

def read_json(wrapper) -> dict:
    data = {}
    try:
        data = json.load(wrapper)
    except Exception as err:
        raise f'read_json error {err}'
    return data