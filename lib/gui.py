from tkinter import *
from tkinter.messagebox import showwarning

from pulse import *
from pulse import ZONES


class EntriesWithLables(Frame):

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


class PulseTable(Frame):

    PADX = 5

    def __init__(self, max_hr, rest_hr, parent=""):
        Frame.__init__(self, parent)
        self.parent = parent

        self.max_hr = max_hr
        self.rest_hr = rest_hr
        
        self.init_title()
        self.init_rows()

    def init_title(self):
        Label(self.parent, text="Your zones: ").grid()
    
    def init_rows(self):
        for i in range(1, len(ZONES)):
            lower, upper = ZONES_FUNC[i](self.max_hr, self.rest_hr)
            self.init_row(i, ZONES[i], lower, upper)
            
    def init_row(self, ind, name, lower, upper):
        Label(self.parent, text="{:s}:".format(name)).grid(
                    column=0, row=ind, sticky="W", padx=self.PADX)
        Label(self.parent, text="{} - {}".format(lower, upper)).grid(
                    column=1, row=ind, sticky="E")
                    

def init_table_in_new_win(age_entry, rest_hr_entry):
    window = Tk()
    window.title("Pulse Zones")

    age = int(age_entry.get())
    
    try:
        max_hr = max_heart_rate(age)
        rest_hr = float(rest_hr_entry.get())

        PulseTable(max_hr, rest_hr, window).grid()
    except Exception as E:
        showwarning(title="Warning", message=str(E))


window = Tk()
window.title("HR Calculator")

input_form = EntriesWithLables(window)
input_form.grid()

age = input_form.entries["age"]
rest_hr = input_form.entries["rest_hr"]
calc = Button(window, text="Calculate",
                            command=lambda: init_table_in_new_win(age, rest_hr))
calc.grid(column=0, row=3, sticky="W", padx=10)

mainloop()
