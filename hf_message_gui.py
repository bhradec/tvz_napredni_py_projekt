import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from hide_message import hide_message
from find_message import find_message

in_img_path = ""        # input image path
out_img_path = ""       # output image path

def browse_out_img_path():
    global out_img_path
    out_img_path = tk.filedialog.askopenfilename()
    out_img_entry.delete(1.0, tk.END)
    out_img_entry.insert(tk.END, out_img_path)

def browse_in_img_path():
    global in_img_path
    in_img_path = tk.filedialog.askopenfilename()
    in_img_entry.delete(1.0, tk.END)
    in_img_entry.insert(tk.END, in_img_path)

main_window = tk.Tk()

tab_parrent = ttk.Notebook(main_window)

hide_msg_tab = ttk.Frame(main_window)
find_msg_tab = ttk.Frame(main_window)

tab_parrent.add(hide_msg_tab, text="Hide message")
tab_parrent.add(find_msg_tab, text="Find message")
tab_parrent.pack(expand=1, fill="both")

############### HIDE MESSAGE TAB #################

hide_in_label = tk.Label(hide_msg_tab, text="Input text:")
hide_out_label = tk.Label(hide_msg_tab, text="Output image:")

in_txt_entry = tk.Text(hide_msg_tab, height=8, width=35)
out_img_entry = tk.Text(hide_msg_tab, height=1, width=35)
out_img_btn = tk.Button(hide_msg_tab, text="Browse", command=browse_out_img_path)

hide_in_label.grid(row=0, column=0)
hide_out_label.grid(row=1, column=0)
in_txt_entry.grid(row=0, column=1, columnspan=2, sticky="we")
out_img_entry.grid(row=1, column=1, sticky="we")
out_img_btn.grid(row=1, column=2)

############### FIND MESSAGE TAB #################

find_in_label = tk.Label(find_msg_tab, text="Input image:")
find_out_label = tk.Label(find_msg_tab, text="Output text:")

in_img_entry = tk.Text(find_msg_tab, height=1, width=35)
in_img_btn = tk.Button(find_msg_tab, text="Browse", command=browse_in_img_path)
out_txt_entry = tk.Text(find_msg_tab, height=8, width=35)

find_in_label.grid(row=0, column=0)
find_out_label.grid(row=1, column=0)
in_img_entry.grid(row=0, column=1, sticky="we")
in_img_btn.grid(row=0, column=2)
out_txt_entry.grid(row=1, column=1, columnspan=2, sticky="we")

main_window.mainloop()
