
# --------------------------------
import os, csv
from docx2pdf import convert
from tkinter import Tk, BooleanVar
from tkinter import ttk, filedialog
from datetime import datetime
import Logg

# Functions

# LOGGER
logger = Logg.Logger()
logger.log_action("Logger created")
logger.log_action("Application startup")
# LOGGER

def unpack_list(data):
    return_data = []
    for i in data:
        logger.log_action("Retrieve data from file")
        return_data.append(i[0])
    return return_data

def write_list_to_file(last_used_path):
    if os.path.exists(last_used_path):
        drop_list.append(last_used_path)
        with open(save_file_path, "w", newline="") as standard_save_file:
            csv.writer(standard_save_file)

def read_list_from_file():
    data = []
    try:
        with open(save_file_path, "r", newline="") as standard_save_file:
            reader = csv.reader(standard_save_file)
            data = unpack_list(reader)
            print(f'Reader data: {data}')
    except FileNotFoundError:
        print("No such file exists")
        file = open(save_file_path, "wb")
        file.close()
    return data

def perform_conversion(input_directory_path, output_directory_path = None):
    if not output_directory_path:
        output_directory_path = input_directory_path
        
def close_app():
    root.destroy()
    logger.log_action("Close application")

def open_file_explorer():
    logger.log_action("Opening file explorer")
    files_directory = filedialog.askdirectory(
        title="Select an input directory"
    )
    logger.log_action("File explorer shut down")
    if not files_directory:
        return None
    return files_directory


# Program

root = Tk()  # Creating a root object
check_box = ttk.Checkbutton()
btn_search_directory = ttk.Button()
dropdown_list = ttk.Combobox()

# Variable creation

file_name = "save.csv"
directory_path = os.path.dirname(os.path.realpath(__file__))
save_file_path = os.path.join(directory_path, file_name)
is_same_directory = BooleanVar(value=False)
drop_list = list(read_list_from_file())

# Widgets initialization

print(datetime.microsecond)

dropdown_list.pack()
btn_search_directory.pack()
check_box.pack()

root.title("PDF auto converter")
root.geometry("300x300")
root.minsize(width=300, height=300)


dropdown_list.config(
    values=drop_list
)
check_box.config(
    text="Put PDF into the same directory?",
    variable=is_same_directory,
    onvalue=True,
    offvalue=False
)
btn_search_directory.config(
    text="...",
    command=open_file_explorer
)

root.protocol("WM_DELETE_WINDOW", close_app)
print(f"Path to - {directory_path}")
print(is_same_directory)

root.mainloop()