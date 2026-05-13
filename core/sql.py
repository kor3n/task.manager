'''Task.Manager -> sql

Author:
 - Kor3n
'''
import sqlite3
from pathlib import Path
from contextlib import ExitStack


class _SQLCursor:
    def __init__(self, sql_connection: sqlite3.Connection):
        self.sql_connection: sqlite3.Connection = sql_connection
        self.sql_cursor: sqlite3.Cursor

    def __enter__(self):
        self.sql_cursor: sqlite3.Cursor = self.sql_connection.cursor()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.sql_connection.commit()

    def execute(self, command: str | tuple) -> None:
        '''Docstring'''
        if isinstance(command, str):
            self.sql_cursor.execute(command)
        if isinstance(command, tuple):
            pass  # self.sql_cursor.execute()


class SQLDatabase:
    '''Docsstring'''

    def __init__(self, database_name: Path) -> None:
        self.db_name: Path = database_name
        self._exit_stack = ExitStack()
        self._connection: sqlite3.Connection

    def __enter__(self):
        '''Docstring'''
        self._connection: sqlite3.Connection = sqlite3.connect(self.db_name)
        return self._exit_stack.enter_context(_SQLCursor(self._connection))

    def __exit__(self, exc_type, exc, tb):
        '''Docstring'''
        self._exit_stack.__exit__(exc_type, exc, tb)
        self._connection.close()


def init_db(data_base_name: Path) -> bool:
    '''Docstring'''
    if data_base_name.exists():
        return False
    with SQLDatabase(data_base_name) as db:
        db.execute('CREATE TABLE IF NOT EXISTS Archive (name TEXT, age INTERGER)')
        db.execute('CREATE TABLE IF NOT EXISTS TODO (name TEXT, age INTERGER)')
    return True


def destory_db(data_base_name: Path) -> bool:
    '''Title

    <Description>
    '''
    if data_base_name.exists():
        data_base_name.unlink()
        return True
    return False


if __name__ == '__main__':
    print(init_db(Path('test.db')))
    # print(destory_db(Path('test.db')))
