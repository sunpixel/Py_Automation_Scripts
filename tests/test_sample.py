from src import file_operations as fo
import os

path = os.path.join(os.getcwd(), os.pardir)

def test1():
    assert fo.get_all_directory_files(path) is not None