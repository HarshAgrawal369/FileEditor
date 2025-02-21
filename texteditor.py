import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    color = colorchooser.askcolor()[1]
    text_area.config(fg=color)

def change_font(*args):
    font_choice = font.askfont()
    text_area.config(font=(font_choice['family'], font_choice['size']))

def new_file():
    global file
    file = None
    text_area.delete(1.0, END)

def open_file():
    global file
    file = filedialog.askopenfilename(defaultextension=".txt",
                                       filetypes=[("Text Documents", "*.txt"),
                                                  ("All Files", "*.*")])
    if file:
        window.title(f"Text editor program - {file}")
        text_area.delete(1.0, END)
        with open(file, "r") as f:
            text_area.insert(1.0, f.read())

def save_file():
    global file
    if file is None:
        file = filedialog.asksaveasfilename(defaultextension=".txt",
                                              filetypes=[("Text Documents", "*.txt"),
                                                         ("All Files", "*.*")])
    if file:
        with open(file, "w") as f:
            f.write(text_area.get(1.0, END))

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    messagebox.showinfo("About", "Text Editor Program v1.0")

def quit():
    window.quit()

window = Tk()
window.title("Text editor program")
file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)- (window_width/2))
y = int((screen_height/2)- (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width,window_height,x,y))
font_name = StringVar(window)
font_size = StringVar(window)
font_size.set("25")


text_area = Text(window, font = (font_name.get(), font_size.get()))
scroll_bar = Scrollbar(window)
scroll_bar.config(command=text_area.yview)
text_area.config(yscrollcommand=scroll_bar.set)

window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area.grid(row=0, column=0, sticky=N + E + S + W)
scroll_bar.grid(row=0, column=1, sticky=N + S)




# Create a menu bar
menu_bar = Menu(window)

# File menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Format menu
format_menu = Menu(menu_bar, tearoff=0)
format_menu.add_command(label="Change Font", command=change_font)
format_menu.add_command(label="Change Color", command=change_color)
menu_bar.add_cascade(label="Format", menu=format_menu)

# Help menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

window.config(menu=menu_bar)
window.mainloop()
