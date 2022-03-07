import os
from tkinter import *
from tkinter import font
from tkinter import colorchooser
from tkinter import filedialog
from tkinter.filedialog import LoadFileDialog, SaveFileDialog, askopenfilename
from tkinter.messagebox import showinfo

from nbformat import write





def change_color() : 
    color = colorchooser.askcolor()
    text_area.config(fg=color[1])
    
def back_color() : 
    color = colorchooser.askcolor()
    text_area.config(bg=color[1])

def change_font(*args) :
    text_area.config(font=(font_name.get() , spin_button.get()))
    
def new_file() :
    window.title("New file")
    text_area.delete(1.0 , END)

def save_file() :
    file = filedialog.asksaveasfilename(initialfile="Untiteled.txt",
                                    defaultextension=".txt",
                                    filetypes=[("All Files" , "*.*"),
                                               ("Text Documents" , "*.txt")])
    if file is None :
        return 
    else :
        try :
            window.title(os.path.basename(file))
        
            file = open(file , "w")
        
            file.write(text_area.get(1.0 , END))
        except Exception :
            print("Can not save file ! ")
        finally :
            file.close()
        
def open_file() :
   file = askopenfilename(defaultextension=".txt",
                          filetypes=[("All Files" , "*.*"),
                                ("Text Documents" , "*.txt")])
   try :
       window.title(os.path.basename(file))
       
       text_area.delete(1.0 , END)
       
       
       file = open(file , "r") 
       
       text_area.insert(1.0 , file.read())
       
   except Exception :
       print("Can not open file ! ")
   finally :
       file.close()
       
def cut() :
    text_area.event_generate("<<Cut>>") 

def copy() :
    text_area.event_generate("<<Copy>>") 

def paste() :     
    text_area.event_generate("<<Paste>>") 

def about() :
    showinfo("This is made by me ! ") # i dont know what is wrong with this 

def quit() :
    window.destroy()

window = Tk()

window.title("Text_editor ! ")

file = None

window_width = 500

window_height = 500

screen_width = window.winfo_screenwidth()
screen_heght = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2)) 
y = int((screen_width / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width , window_height , x , y))

font_name = StringVar(window)
font_name.set("Ariel")

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window , font=(font_name.get() , font_size.get()))

scrol_bar = Scrollbar(text_area)
window.grid_rowconfigure( 0  , weight=1)
window.grid_columnconfigure( 0  , weight=1)
text_area.grid(sticky=N + E + S + W )

scrol_bar.pack(side=RIGHT , fill=Y)
text_area.config(yscrollcommand=scrol_bar.set)

frame = Frame(window)
frame.grid()

color_button = Button(frame , text="Color" , command=change_color)
color_button.grid(row=0 , column=0 )

back_button = Button(frame , text="Back Ground" , command=back_color )
back_button.grid(row=0  , column=3)

font_button = OptionMenu(frame , font_name , *font.families() , command=change_font)
font_button.grid(row=0 , column=1)

spin_button = Spinbox(frame , from_=1 , to=100 , textvariable=font_size , command=change_font)
spin_button.grid(row=0 , column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)
 
file_menu = Menu(menu_bar , tearoff=0)
menu_bar.add_cascade( label="File"  , menu=file_menu)
file_menu.add_command(label="New"   , command=new_file)
file_menu.add_command(label="Open"  , command=open_file)
file_menu.add_command(label="Save"  , command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit"  , command=quit)



edit_menu = Menu(menu_bar , tearoff=0)
menu_bar.add_cascade(label="Edit"    , menu=edit_menu)
edit_menu.add_command(label="Copy"   , command=copy)
edit_menu.add_command(label="Paste"  , command=paste)
edit_menu.add_command(label="Cut"    , command=cut)

about_menu = Menu(menu_bar , tearoff=0)
menu_bar.add_cascade(label="Help"   , menu=about_menu)
about_menu.add_command(label="About", command=about)




 
window.mainloop()