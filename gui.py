from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
class Mp3ConverterGui(object):
    def __init__(self):
        self.file_list = []
    def build_gui(self):
        root = Tk()
        frm = ttk.Frame(root, padding=10)
frm.grid()
list_items = Variable(value=file_list)
lb = Listbox(
    frm,
    height=6,
    listvariable=list_items,
    selectmode=EXTENDED
)
root.mainloop()