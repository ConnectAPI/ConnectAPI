import os
import pathlib

ROOT_PATH = '/var/lib'
DATA_DIR_NAME = "/connectapi_data"


def get_root() -> pathlib.Path:
    """Returns the path to the root data dir"""
    data_path = ROOT_PATH + DATA_DIR_NAME
    if not os.path.isdir(data_path):
        # TODO: chack premissions
        os.mkdir(data_path)
    return pathlib.Path(data_path)
