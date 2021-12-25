FILEPATH = "/usr/data/config.db"


def save_container_ids(ids: list):
    with open(FILEPATH, 'w') as file:
        file.write(','.join(ids))


def load_container_ids() -> list:
    with open(FILEPATH, 'r') as file:
        ids_str = file.read()
    return ids_str.split(",")
