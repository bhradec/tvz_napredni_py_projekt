import tkinter as tk

from tkinter import ttk
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk

MIN_WIN_WIDTH = 600
MIN_WIN_HEIGHT = 275

current_img_path = "./img/placeholder.png"
current_img_tk = None

# Učitava ulaznu sliku i prilagođava ju za prikaz u GUI-u
def get_img_tk(img_path):
    in_img = Image.open(img_path)
    # Postavljanje veličine slike na polovicu širine glavnog prozora
    # Metoda thumbnail zadržava izvorne omjere visine i širine
    in_img.thumbnail((MIN_WIN_WIDTH/2, MIN_WIN_WIDTH/2), Image.ANTIALIAS)
    # Pretvaranje slike u oblik pogodan za prikaz s tkinterom
    in_img_tk = ImageTk.PhotoImage(in_img)
    return in_img_tk

# Stvaranje glavnog prozora
main_window = tk.Tk()
main_window.minsize(MIN_WIN_WIDTH, MIN_WIN_HEIGHT)
main_window.title("Message finder")

tab_parent = ttk.Notebook(main_window)

# Tab parent sadrži tab za skrivanje i tab za otkrivanje poruke
hide_msg_tab = ttk.Frame(main_window)
find_msg_tab = ttk.Frame(main_window)
tab_parent.add(hide_msg_tab, text="Hide message")
tab_parent.add(find_msg_tab, text="Find message")

# Tab parent zauzima cijelu širinu i visinu prozora
tab_parent.pack(expand=1, fill="both")

# Oba stupca u gridu taba za skrivanje poruke su jednako široka
find_msg_tab.columnconfigure(0, weight=1, uniform="group1")
find_msg_tab.columnconfigure(1, weight=1, uniform="group1")

find_in_lbl = tk.Label(find_msg_tab, text="Input:")
find_out_lbl = tk.Label(find_msg_tab, text="Output:")
find_in_lbl.grid(row=0, column=0, sticky="w")
find_out_lbl.grid(row=0, column=1, sticky="w")

# Dohvaćanje placeholder slike u obliku pogodnom za tkinter
in_img_tk = get_img_tk(current_img_path)

# Label sa ulaznom slikom
in_img_lbl = tk.Label(find_msg_tab, image=in_img_tk)
in_img_lbl.grid(row=1, column=0, sticky="we")

# Label sa izlaznim tekstom
out_text_lbl = tk.Label(find_msg_tab, text="output message", wraplength=MIN_WIN_WIDTH/2)
out_text_lbl.grid(row=1, column=1, sticky="we")

# Otvara prozor za odabir slikovne datoteke i vraća
# apsolutnu putanju do adabrane datoteke
def set_input_image():
    global current_img_path
    global current_img_tk
    
    img_path = filedialog.askopenfilename()
    
    if not img_path:
        img_path = current_img_path

    current_img_path = img_path
    current_img_tk = get_img_tk(img_path)
    # Promjena trenutne slike na labelu za prikaz input slike
    in_img_lbl.configure(image=current_img_tk)        
        
load_img_btn = tk.Button(find_msg_tab, text="Load input image", command=set_input_image)
load_img_btn.grid(row=2, column=0, sticky="w")

main_window.mainloop()