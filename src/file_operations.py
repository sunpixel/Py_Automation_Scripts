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