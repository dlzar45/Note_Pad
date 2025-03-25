import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

root.geometry("600x600")
root.title("Notepad")
root.resizable(False,False)
root.config(bg="lightgrey")

def save_file():
    file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if file is None:
        return
    text=str(space.get(1.0,tk.END))
    file.write(text)
    file.close()

     

def open_file():
    file=filedialog.askopenfile(mode='r',filetypes=[('text files','*.txt')])
    if file is not None:
        content=file.read()
    space.insert(tk.INSERT,content)


b1= tk.Button(root,width='20',height='2',bg='#fff',text='Save File',command=save_file)
b1.place(x=100,y=5)
b2= tk.Button(root,width='20',height='2',bg='#fff',text='Open File',command=open_file)
b2.place(x=300,y=5)

space=tk.Text(root,height=33,width=72,wrap='word')
space.place(x=10,y=60)

root.mainloop()