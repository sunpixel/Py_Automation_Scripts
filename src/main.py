
# --------------------------------
import os, csv
from docx2pdf import convert
from tkinter import Tk, BooleanVar
from tkinter import ttk, filedialog
from datetime import datetime
from Logg import Logger
from file_operations import *

# Functions

# LOGGER
logger = Logger()
logger.log_action("Logger created")
logger.log_action("Application startup")
# LOGGER


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
print(f'is_same_directory - {is_same_directory}')

root.mainloop()