from tkinter import *


class EntriesWithLabels(Frame):

    PADX = 10
    LABELS = {
        "age": "Enter age: ",
        "rest_hr": "Enter rest heart rate: ",
    }

    def __init__(self, parent=""):
        Frame.__init__(self, parent)
        self.parent = parent

        self.init_labels()
        self.init_entries()
    
    def init_labels(self):
        for text in self.LABELS.values():
            Label(self.parent, text=text).grid(sticky="W", padx=self.PADX)
    
    def init_entries(self):
        self.entries = {}

        for i in range(len(self.LABELS.keys())):
            entry = Entry(self.parent)
            entry.grid(column=1, row=i)

            self.entries[list(self.LABELS.keys())[i]] = entry
