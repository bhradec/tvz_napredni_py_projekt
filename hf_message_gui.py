import tkinter as tk

from tkinter import Label, Text, Button
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from hide_message import hide_message
from find_message import find_message
from hide_message import MessageTooLongException

in_img_path = ""        # Putanja ulazne slike
out_img_path = ""       # Putanja izlazne slike

# Upisuje zadanu poruku na sliku koja se nalazi na zadanoj putanji
def embed_message():
    message = in_txt_entry.get("1.0", "end")
    # Brisanje line feeda s kraja poruke koji je dodao text widget
    message = message[:-1]
    
    if len(message) == 0:
        tk.messagebox.showerror(title="Error", message="No message given")
        return
    elif len(out_img_path) == 0:
        tk.messagebox.showerror(title="Error", message="No output image path given")
        return
    try:
        hide_message(message, out_img_path)
        tk.messagebox.showinfo(title="Success", message="Message succesfully embeded")
    except MessageTooLongException:
        tk.messagebox.showerror(title="Error", message="Message is too long for given image")

def browse_out_img_path():
    global out_img_path
    out_img_path = tk.filedialog.askopenfilename()
    out_img_entry.configure(state="normal")
    out_img_entry.delete(1.0, "end")
    out_img_entry.insert("end", out_img_path)
    out_img_entry.configure(state="disabled")

def browse_in_img_path():
    global in_img_path
    in_img_path = tk.filedialog.askopenfilename()
    out_img_entry.configure(state="normal")
    in_img_entry.delete(1.0, "end")
    in_img_entry.insert("end", in_img_path)
    out_img_entry.configure(state="disabled")

main_window = tk.Tk()
main_window.title("H/F message")

tab_parrent = ttk.Notebook(main_window)

hide_msg_tab = ttk.Frame(main_window)
find_msg_tab = ttk.Frame(main_window)

tab_parrent.add(hide_msg_tab, text="Hide message")
tab_parrent.add(find_msg_tab, text="Find message")
tab_parrent.pack(expand=1, fill="both")

############### HIDE MESSAGE TAB #################

hide_in_label = tk.Label(hide_msg_tab, text="Input text:")
hide_out_label = tk.Label(hide_msg_tab, text="Output image:")

in_txt_entry = tk.Text(hide_msg_tab, height=8, width=40)
out_img_entry = tk.Text(hide_msg_tab, height=1, width=40)
out_img_btn = tk.Button(hide_msg_tab, text="Browse", command=browse_out_img_path)
hide_msg_btn = tk.Button(hide_msg_tab, text="Embed message", command=embed_message)

hide_in_label.grid(row=0, column=0, sticky="n")
hide_out_label.grid(row=1, column=0)
in_txt_entry.grid(row=0, column=1, columnspan=2, sticky="we")
out_img_entry.grid(row=1, column=1, sticky="we")
out_img_btn.grid(row=1, column=2)
hide_msg_btn.grid(row=2, column=0, columnspan=3)

# Text widget koji prikazuje putanju do slike je readonly
out_img_entry.configure(state="disabled")

############### FIND MESSAGE TAB #################

find_in_label = tk.Label(find_msg_tab, text="Input image:")
find_out_label = tk.Label(find_msg_tab, text="Output text:")

in_img_entry = tk.Text(find_msg_tab, height=1, width=40)
in_img_btn = tk.Button(find_msg_tab, text="Browse", command=browse_in_img_path)
out_txt_entry = tk.Text(find_msg_tab, height=8, width=40)

find_in_label.grid(row=0, column=0)
find_out_label.grid(row=1, column=0, sticky="n")
in_img_entry.grid(row=0, column=1, sticky="we")
in_img_btn.grid(row=0, column=2)
out_txt_entry.grid(row=1, column=1, columnspan=2, sticky="we")

# Text widget u koji se ispisuje izlazni tekst je read only
out_txt_entry.configure(state="disabled")

# Prvi stupac svakog taba je iste duljine
hide_msg_tab.columnconfigure(0, weight="1", uniform="first_columns")
find_msg_tab.columnconfigure(0, weight="1", uniform="first_columns")

main_window.mainloop()
