import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

from tkinter import *

from lib.gui.entries_with_labels import EntriesWithLabels
from lib.gui.table_init_func import *


window = Tk()
window.title("HR Calculator")

input_form = EntriesWithLabels(window)
input_form.grid()

age = input_form.entries["age"]
rest_hr = input_form.entries["rest_hr"]

calculate = Button(window, text="Calculate",
                            command=lambda: try_init_table(age, rest_hr))
calculate.grid(column=0, row=3, sticky="W", padx=10)

mainloop()
