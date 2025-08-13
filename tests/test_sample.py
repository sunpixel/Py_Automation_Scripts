from src import file_operations as fo
from src import settings
import os

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)



def test1():
    print(f'path - {path}')
    result = fo.get_all_directory_files(path)
    print(f'Names: {result}')
    print(len(result))
    assert result is not []

def test2():
    result = settings.read_config()
    print(f'Result: {result}')
    assert result is not {}

def test3():
    assert settings.write_config()