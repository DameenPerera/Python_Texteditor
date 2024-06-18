import customtkinter
import tkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

customtkinter.set_appearance_mode("System")

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def change_menu_color(menu, bg_rgb, fg_rgb):
    menu.config(background=rgb_to_hex(bg_rgb), foreground=rgb_to_hex(fg_rgb), activebackground=rgb_to_hex(bg_rgb), activeforeground=rgb_to_hex(fg_rgb))
    for i in range(menu.index("end") + 1):
        menu.entryconfig(i, background=rgb_to_hex(bg_rgb), foreground=rgb_to_hex(fg_rgb), activebackground=rgb_to_hex(bg_rgb), activeforeground=rgb_to_hex(fg_rgb))

#New File
def newFile(form, textEditor):
    textEditor.delete(1.0, tkinter.END)
    form.title("Text Editor")

#Open File
def openFile(form, textEditor):
    openFile = askopenfilename(filetypes=[("All Files", ".*"), ("Text Files", ".txt")])
    if not openFile:
        return
    newFile(form, textEditor)
    with open(openFile, "r") as f:
        content = f.read()
        textEditor.insert(1.0, content)
    form.title(f"Text Editor - {os.path.basename(openFile)}")

#Save File
def saveFile(form, textEditor):
    saveFile = asksaveasfilename(filetypes=[("All Files", ".*"), ("Text Files", ".txt")])
    if not saveFile:
        return
    with open(saveFile, "w") as f:
        content = textEditor.get(1.0, tkinter.END)
        f.write(content)
    form.title(f"Text Editor - {os.path.basename(saveFile)}")

#SaveAs File
def saveAsFile(form, textEditor):
    saveFile = asksaveasfilename(filetypes=[("All Files", ".*"), ("Text Files", ".txt")])
    if not saveFile:
        return
    with open(saveFile, "w") as f:
        content = textEditor.get(1.0, tkinter.END)
        f.write(content)
    form.title(f"Text Editor - {os.path.basename(saveFile)}")

#Main Form
root = customtkinter.CTk()
root.geometry("1000x750+200+200")
root.title("Text Editor")

#main menu
mainMenu = tkinter.Menu(root)

#file tab of main menu
fileMenu = tkinter.Menu(mainMenu, tearoff=False)
fileMenu.add_command(label="New File    ", command=lambda:newFile(root, textEditor))
fileMenu.add_command(label="Open File   ", command=lambda:openFile(root, textEditor))
fileMenu.add_command(label="Save    ", command=lambda:saveFile(root, textEditor))
fileMenu.add_command(label="Save As    ", command=lambda:saveAsFile(root, textEditor))
mainMenu.add_cascade(label="    File    ", menu=fileMenu)


root.configure(menu=mainMenu)

change_menu_color(fileMenu, (64, 64, 64), (255, 255, 255))

textEditor = tkinter.Text(root, wrap='word', bg=rgb_to_hex((64, 64, 64)), fg=rgb_to_hex((255, 255, 255)), insertbackground=rgb_to_hex((255, 255, 255)), selectbackground='blue', selectforeground='white')
textEditor.pack(expand=True, fill='both', pady=1)

root.bind("<Control-n>", lambda x: newFile(root, textEditor))
root.bind("<Control-o>", lambda x: openFile(root, textEditor))
root.bind("<Control-s>", lambda x: saveFile(root, textEditor))

root.mainloop()
