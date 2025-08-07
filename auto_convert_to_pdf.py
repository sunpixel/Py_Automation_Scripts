
# --------------------------------
import os, csv, inspect
from logging import exception
from docx2pdf import convert
from tkinter import Tk, BooleanVar
from tkinter import ttk, filedialog
from datetime import datetime

# Functions

# LOGGER
def log_action(action_text = None):
    log_file_path = os.path.join(directory_path, "log.txt")
    log_text = f'{datetime.now()} | caller: {inspect.stack()[1].function} - {action_text}\n'

    log = open(log_file_path, "a")
    log.write(log_text)
    log.close()
    print(log_text)
    # LOGGER

def unpack_list(data):
    return_data = []
    for i in data:
        log_action("Retrieve data from file")
        return_data.append(i[0])
    return return_data

def write_list_to_file(last_used_path):
    if os.path.exists(last_used_path):
        drop_list.append(last_used_path)
        with open(save_file_path, "w", newline="") as standard_save_file:
            writer = csv.writer(standard_save_file)    

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

def perfrom_conversion(input_directory_path, output_directory_path = None):
    if not output_directory_path:
        output_directory_path = input_directory_path
        
def close_app():
    log_action("Close application")
    root.destroy()

def open_file_explorer():
    log_action("Opening file explorer")
    files_directory = filedialog.askdirectory(
        title="Select an input directory"
    )
    log_action("File explorer shut down")
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