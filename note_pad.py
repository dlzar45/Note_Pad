import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

root.geometry("600x600")
root.title("Notepad")
root.resizable(False,False)
root.config(bg="lightgrey")

# Function to save the content of the Text widget to a file
def save_file():
    file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    # If the user cancels the file dialog (i.e., file is None), return without doing anything
    if file is None:
        return
    text=str(space.get(1.0,tk.END))
    file.write(text)
    file.close()

     
# Function to open an existing file and display its content in the Text widget
def open_file():
    file=filedialog.askopenfile(mode='r',filetypes=[('text files','*.txt')])
    # If the user selects a file, read its content
    if file is not None:
        content=file.read()
    space.insert(tk.INSERT,content)


# Create a 'Save File' button, which triggers the save_file function when clicked
b1= tk.Button(root,width='20',height='2',bg='#fff',text='Save File',command=save_file)
b1.place(x=100,y=5)

# Create an 'Open File' button, which triggers the open_file function when clicked
b2= tk.Button(root,width='20',height='2',bg='#fff',text='Open File',command=open_file)
b2.place(x=300,y=5)

# Create a Text widget (area where the user can type or display file content)
space=tk.Text(root,height=33,width=72,wrap='word')
space.place(x=10,y=60)

# Start the main event loop (this will keep the application running)
root.mainloop()