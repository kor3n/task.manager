'''Title

<description>

:Authors:
    Joshua Boat,
:Version: 1.0.0
:Date: 01/01/2025
'''
import sys
from pathlib import Path

import typer

from core.config import read_config
from core.sql import init_db, destory_db

ROOT_DIR = Path(__file__).parent
app = typer.Typer()


@app.command('initi')
def init() -> None:
    '''main

    This is the main function that calls any other functions to complete its task.
    '''

    loaded_config = read_config(ROOT_DIR.joinpath('config.json'))
    database_location = ROOT_DIR.joinpath(loaded_config['database'])

    if init_db(database_location) is False:
        sys.exit('DB Exsists!')
    if destory_db(database_location) is False:
        sys.exit(1)


if __name__ == '__main__':
    app()
