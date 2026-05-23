from .Widget import *
from .make_component import make
import tkinter as tk
import tkinter.ttk as ttk

tk_names = """
Tk
Button
Canvas
Checkbutton
Entry
Frame
Label
Listbox
Menubutton
Menu
Message
Radiobutton
Scale
Scrollbar
Text
Toplevel
Spinbox
PanedWindow
LabelFrame
"""
for tk_name in tk_names.split():
    tk_name = tk_name.strip()
    make(tk_name, getattr(tk, tk_name))
ttk_names = """
Combobox
Notebook
Progressbar
Separator
Sizegrip
Treeview
Button
Checkbutton
Entry
Frame
Label
Menubutton
Radiobutton
Scale
Scrollbar
Spinbox
PanedWindow
LabelFrame
"""
for ttk_exname in ttk_names.split():
    ttk_exname = ttk_exname.strip()
    make("T"+ttk_exname, getattr(ttk, ttk_exname))
