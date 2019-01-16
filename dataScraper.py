import ttk as ttk
from Tkinter import *
import Tkinter as tk
import datetime
import sys
import io



global time_stamp
time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


root = Tk()
root.geometry("600x600")
root.title('DataScraper')
n = ttk.Notebook(root)


project_title = Label(root,bg="white",text = "DataScraper")
project_title.config(font=("Comfortaa", 30))
project_title.pack(pady=15)
project_title.config(fg="cyan4")
project_title.pack(fill=X)



print(time_stamp)
n.pack(fill=X)
root.mainloop()
