import os
import sys

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(PROJECT_ROOT)

from tkinter import *
from tkinter.messagebox import showwarning

from lib.gui.pulse_table import PulseTable


def try_init_table(age_entry, rest_hr_entry):
    try:
        init_table_in_new_win(age_entry, rest_hr_entry)
    except AssertionError as assert_error:
        showwarning(title="Warning", message=str(assert_error))

def init_table_in_new_win(age_entry, rest_hr_entry):
    age = int(age_entry.get())
    rest_hr = float(rest_hr_entry.get())
    
    window = Tk()
    window.title("Pulse Zones")

    try:
        PulseTable(age, rest_hr, window).grid()
    except AssertionError as assert_error:
        window.destroy()
        raise assert_error
