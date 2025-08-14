
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

def toogle_elemets_visibility():
    logger.log_action("Hiding/Unhidng elemnts")
    x = is_same_directory.get()
    for widget in [dropdown_output_list, btn_search_dir_out, text_field_out]:
        widget.grid() if not x else widget.grid_remove()

# Program

root = Tk()  # Creating a root object
text_field_in = ttk.Label(text="Select input directory")
text_field_out = ttk.Label(text="Select output directory")
check_box_hide = ttk.Checkbutton()
check_box_search = ttk.Checkbutton()
btn_search_dir_in = ttk.Button()
btn_search_dir_out = ttk.Button()
dropdown_input_list = ttk.Combobox()
dropdown_output_list = ttk.Combobox()

# Variable creation

is_same_directory = BooleanVar(value=True)
search_sub_dirs = BooleanVar(value=False)
drop_list = list(read_list_from_file())

# Widgets initialization

logger.log_action("Initialization of grid elements")

text_field_in.grid(row=0)

dropdown_input_list.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
btn_search_dir_in.grid(row=1, column=1, padx=5, pady=5, sticky='w')

text_field_out.grid(row=2)

dropdown_output_list.grid(row=3, column=0, padx=5, pady=5, sticky='ew')
btn_search_dir_out.grid(row=3, column=1, padx=5, pady=5, sticky='w')

check_box_hide.grid(row=4)



root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)

logger.log_action("Initial hiding of elemnts")
toogle_elemets_visibility() # Essential for hiding elements

root.title("PDF auto converter")
root.geometry("300x300")
root.minsize(width=300, height=300)


dropdown_input_list.config(
    values=drop_list
)
# Values are to be redone
dropdown_output_list.config(
    values=drop_list
)

check_box_hide.config(
    text="Put PDF into the same directory?",
    variable=is_same_directory,
    onvalue=True,
    offvalue=False,
    command=toogle_elemets_visibility
)

check_box_search.config(
    text="Search sub directories for files?",
    onvalue=True,
    offvalue=False,
    variable=search_sub_dirs
)

btn_search_dir_in.config(
    text="...",
    command=open_file_explorer
)

btn_search_dir_out.config(
    text="...",
    command=open_file_explorer
)

root.protocol("WM_DELETE_WINDOW", close_app)

root.mainloop()