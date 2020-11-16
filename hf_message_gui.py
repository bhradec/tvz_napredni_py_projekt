import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from hide_message import hide_message
from find_message import find_message

img_path = ""

def browse_image_path():
    global img_path
    img_path = tk.filedialog.askopenfilename()
    out_img_path.delete(1.0, tk.END)
    out_img_path.insert(tk.END, img_path)

main_window = tk.Tk()

tab_parrent = ttk.Notebook(main_window)

hide_msg_tab = ttk.Frame(main_window)
find_msg_tab = ttk.Frame(main_window)

tab_parrent.add(hide_msg_tab, text="Hide message")
tab_parrent.add(find_msg_tab, text="Find message")
tab_parrent.pack(expand=1, fill="both")

############### HIDE MESSAGE TAB #################

hide_out_label = tk.Label(hide_msg_tab, text="Output image:")
hide_in_label = tk.Label(hide_msg_tab, text="Input text:")

in_txt = tk.Text(hide_msg_tab, height=8, width=35)
out_img_path = tk.Text(hide_msg_tab, height=1, width=35)
browse_img_btn = tk.Button(hide_msg_tab, text="Browse", command=browse_image_path)

hide_in_label.grid(row=0, column=0)
hide_out_label.grid(row=1, column=0)
in_txt.grid(row=0, column=1, columnspan=2, sticky="we")
out_img_path.grid(row=1, column=1, sticky="we")
browse_img_btn.grid(row=1, column=2)

main_window.mainloop()