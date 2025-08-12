from src import file_operations as fo
import os

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)


def test1():
    print(f'path - {path}')
    result = fo.get_all_directory_files(path)
    print(f'Names: {result}')
    assert result is not []