# simple text editor
# Date :- 26-06-2019
# praveen kumar

from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import tkinter.scrolledtext

root=Tk(className="Simple Text Editor")
textPad = scrolledtext.ScrolledText(root,width=600,height=600)

def open_command():
    file=filedialog.askopenfile(parent=root,mode="rb",title="Select a file")
    if file!=None:
        contents=file.read()
        textPad.insert("1.0",contents)
        file.close()
        
def save_command():
    file=filedialog.asksaveasfile(mode="w")
    if file!= None:
        data = textPad.get("1.0",END+"-1c")
        file.write(data)
    
def exit_command():
    if messagebox.askokcancel("Quit","Do you really want to quit"):
        root.destroy()
def about_command():
    lablel = messagebox.showinfo("About","This Simple Text Editor is created for Python")


        
def work():
    print("Its working !!")

def res():
    print("GUI window resized")
    root.geometry("200x100")
def norm():
    print(" GUI window back to normal")
    root.geometry("400x300")
    


menu_1 = Menu(root)
root.config(menu=menu_1)

#First menu
file_menu=Menu(menu_1)
menu_1.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="New file",command=work)
file_menu.add_command(label=" Open",command=open_command)
file_menu.add_command(label="Save",command=save_command)
file_menu.add_command(label="Exit",command=exit_command)

#Second menu

edit_menu=Menu(menu_1)
menu_1.add_cascade(label="Edit",menu=edit_menu)

edit_menu.add_command(label="Resize",command=res)
edit_menu.add_command(label="Normal",command=norm)
edit_menu.add_cascade(label="Cut")
edit_menu.add_cascade(label="Copy")
edit_menu.add_cascade(label="Paste")


#Third menu
view_menu=Menu(menu_1)
menu_1.add_cascade(label="View",menu=view_menu)

view_menu.add_command(label="About",command=about_command)

#Fourth menu
code_menu=Menu(menu_1)
menu_1.add_cascade(label="Code",menu=code_menu)

#Fifth menu

run_menu=Menu(menu_1)
menu_1.add_cascade(label="Run",menu=run_menu)

#Sixth Menu

help_menu=Menu(menu_1)
menu_1.add_cascade(label="Help",menu=help_menu)

#Status Bar
status =Label(root,text="Run",bg="yellow",relief=SUNKEN,bd=1)
status.pack(side=BOTTOM,fill=X)

textPad.pack()

root.mainloop()