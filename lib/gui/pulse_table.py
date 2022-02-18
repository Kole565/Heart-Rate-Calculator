from tkinter import *

from lib.zones_calculator import ZonesCalculator


class PulseTable(Frame):

    PADX = 5

    def __init__(self, age, rest_hr, parent=""):
        Frame.__init__(self, parent)
        self.parent = parent

        self.calculator = ZonesCalculator(age, rest_hr)
        
        self.init_title()
        self.init_rows()

    def init_title(self):
        Label(self.parent, text="Your zones: ").grid()
    
    def init_rows(self):
        for i in range(len(self.calculator.zones)):
            zone = self.calculator.zones[i]

            self.init_row(i+1, zone)
            
    def init_row(self, ind, zone):
        Label(self.parent, text="{:s}:".format(zone.name)).grid(
            column=0, row=ind, sticky="W", padx=self.PADX)
        Label(self.parent, text="{} - {}".format(zone.lower, zone.upper)).grid(
            column=1, row=ind, sticky="E")
