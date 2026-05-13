'''Task.Manager -> config

Author:
 - Kor3n
'''
import json
from pathlib import Path


def read_config(file_name: Path) -> dict:
    '''Title

    <Description>
    '''
    with Path(file_name).open('r', encoding='utf-8') as config_file:
        return json.load(config_file)


def init_config() -> bool:
    '''Title

    <Description>
    '''

    return True


def main() -> None:
    '''main

    This is the main function that calls any other functions to complete its task.
    '''
    a = read_config(Path('config.json'))
    print(type(a))


if __name__ == '__main__':
    main()
