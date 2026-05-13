'''Task.Manager [main]

:Authors:
    Kor3n,
:Version: 1.0.0
:Date: 14/05/2026
'''
from pathlib import Path


from core.config import read_config
from core.sql import init_db

ROOT_DIR = Path(__file__).parent


def main() -> None:
    '''main

    This is the main function that calls any other functions to complete its task.
    '''

    loaded_config = read_config(ROOT_DIR.joinpath('config.json'))
    database_location = ROOT_DIR.joinpath(loaded_config['database'])

    init_db(database_location)


if __name__ == '__main__':
    main()
