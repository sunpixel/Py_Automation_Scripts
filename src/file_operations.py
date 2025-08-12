from Logg import Logger
import os, csv
logger = Logger()

file_name = "save.csv"
directory_path = os.path.dirname(os.path.realpath(__file__))
save_file_path = os.path.join(directory_path, file_name)
logger.log_action("File operations file initialized")

def unpack_list(data):
    return_data = []
    for i in data:
        logger.log_action("Retrieve data from file")
        return_data.append(i[0])
    return return_data

# BUG here TEST NEEDED
def write_list_to_file(last_used_path):
    logger.log_action("Writing data to CSV file")
    if os.path.exists(last_used_path):
        with open(save_file_path, "a", newline="") as standard_save_file:
            writer = csv.writer(standard_save_file)
            writer.writerow(last_used_path)
            logger.log_action("Writing succesfeul")
            return True
    logger.log_action("Writing failed")
    return False
# BUG here TEST NEEDED


def read_list_from_file():
    data = []
    try:
        with open(save_file_path, "r", newline="") as standard_save_file:
            reader = csv.reader(standard_save_file)
            data = unpack_list(reader)
            print(f'Reader data: {data}')
            logger.log_action("Reading data from csv file")
    except FileNotFoundError:
        print("No such file exists")
        logger.log_action("No CSV file was found")
    return data


def get_all_directory_files(input_directory):
    try:
        out = []
        logger.log_action("Try to scandir directory files")
        with os.scandir(input_directory) as files:
            print(files)
            print(list(files))
            print('-' * 40)
            for entry in files:
                if entry.is_file():
                    out.append(entry.name)
        return out
    except FileNotFoundError:
        logger.log_action("No directory under the said path was found")
        return None
    

def perform_conversion(input_directory_path, output_directory_path = None):
    logger.log_action("Entering conversion function")
    if output_directory_path is None:
        logger.log_action("Set Output directory as input directory")
        output_directory_path = input_directory_path
    try:
        logger.log_action("Find all files in specified directory")
        files = []
        with os.scandir(input_directory_path) as entries:
            for entry in entries:
                if entry.is_file() and entry.name.endswith((".doc", ".docx")):
                    files.append(entry.name)
    except FileNotFoundError:
        logger.log_action("No directroy was found under specified path")