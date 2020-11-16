import tkinter as tk

def button_1_click():
    # define new text (you can modify this to your needs!)
    new_text = "Button 1 clicked!"
    # delete content from position 0 to end
    entry.delete(0)
    # insert new_text at position 0
    entry.insert(0, new_text)

def button_2_click():
    # define new text (you can modify this to your needs!)
    new_text = "Button 2 clicked!"
    # set connected text variable to new_text
    entry_text.set(new_text)

root = tk.Tk()

entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text)

button_1 = tk.Button(root, text="Button 1", command=button_1_click)
button_2 = tk.Button(root, text="Button 2", command=button_2_click)

entry.pack(side=tk.TOP)
button_1.pack(side=tk.LEFT)
button_2.pack(side=tk.LEFT)

root.mainloop()