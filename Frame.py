from tkinter import *

root = Tk()

root.title("Text Editor")

#Menu (toolbar)
menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New File")
fileMenu.add_command(label="Open File")

# SubMenu of OpenRecent
openRecentMenu = Menu(fileMenu)
fileMenu.add_cascade(label="Open Recent", menu=openRecentMenu)
openRecentMenu.add_command(label="Recent file 1")
openRecentMenu.add_command(label="Recent file 2")
openRecentMenu.add_command(label="Recent file 3")
openRecentMenu.add_command(label="Recent file 4")
openRecentMenu.add_command(label="Recent file 5")
# SubMenu of OpenRecent END

fileMenu.add_separator();
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Save as..")
fileMenu.add_separator();
fileMenu.add_command(label="Exit")

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo")
editMenu.add_command(label="Redo")
editMenu.add_command(label="Cut")
editMenu.add_command(label="Copy")
editMenu.add_command(label="Paste")

findMenu = Menu(menu)
menu.add_cascade(label="Find", menu=findMenu)
findMenu.add_command(label="Find all")
findMenu.add_command(label="Find next")
findMenu.add_command(label="Find previous")
#Creating menu END

root.mainloop()
