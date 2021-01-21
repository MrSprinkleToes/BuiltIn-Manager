import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
#from tkinter import ttk
from tkinter.ttk import Treeview
from tkinter.ttk import Button
import os
window = tk.Tk()
window.title("BuiltIn Plugin Manager")
window.geometry("500x400")
window.minsize(500, 400)

def addBuiltIn(name):
    if os.path.exists(builtinPath+"/"+name+".sig"):
        verified = "Yes"
    else:
        verified = "No"
    listB.insert("", "end", text=name, values=(verified))

def getBuiltIns():
    return

def addBuiltIns(array):
    for name in array:
        listB.insert("end", name)

def prompt(t, title, question):
    messagebox.showinfo(title, question)
    if t == "fileUpload":
        return filedialog.askdirectory(mustexist=True, initialdir=os.getenv("LOCALAPPDATA"))
        
def findVersion(robloxPath):
    for file in os.listdir(robloxPath+"/Versions"):
        print(file)
        if os.path.exists(robloxPath+"/Versions/"+file+"/RobloxStudioBeta.exe"):
            return robloxPath+"/Versions/"+file

def refresh():
    listB.delete(*listB.get_children())
    for builtin in os.listdir(builtinPath):
        if not ".sig" in builtin:
            addBuiltIn(builtin)

def itemSelected(x):
    remove.state(["!disabled"])

def removePlugin():
    selected = listB.item(listB.focus())
    if not selected["values"][0] == "Yes":
        delete = messagebox.askokcancel("Warning", "Continuing will delete this plugin. If you are temporarily moving it, make sure you make a backup somewhere else!")
        if delete:
            os.remove(builtinPath+"/"+selected["text"])
            refresh()
    else:
        messagebox.showerror("Cannot remove plugin", "This plugin is verified by Roblox, it is unable to be removed.")

def addPlugin():
    proceed = messagebox.askokcancel("Warning", "Make sure you trust all plugins you add, BuiltIn plugins have more control over Studio than regular plugins!")
    if proceed:
        plugin = filedialog.askopenfilename(filetypes=[("Roblox Model",".rbxm"),("Roblox Model",".rbxmx")])
        name = plugin.rpartition("/")[2]
        print(name)
        os.rename(plugin, builtinPath+"/"+name)
    refresh()

titleLabel = tk.Label(window, text="BuiltIn Manager", font=("Segoe", 18))
titleLabel.grid(row=0, column=0)

listB = Treeview(window, columns=("Verified"), selectmode="browse")
listB.heading("Verified", text="Verified")
listB.column("Verified", width=70, stretch="NO")
#addBuiltIns({"Placeholder name", "Placeholder2", "BuiltIn Placeholder", "BuiltIn3"})
listB.grid(row=1, column=0, sticky="nsew", padx=(20,20))
listB.bind("<Button-1>", itemSelected)

add = Button(window, text="Add plugin", command=addPlugin)
add.grid(row=2, column=0, sticky="W", padx=20, pady=5)
remove = Button(window, text="Remove plugin", state="disabled", command=removePlugin)
remove.grid(row=2, column=0, sticky="E", padx=20, pady=5)

window.grid_columnconfigure(0, weight=1)

# main stuff
if not os.path.exists("settings.txt"):
    settings = open("settings.txt", "w")
    settings.close()
settings = open("settings.txt", "r+")
robloxPath = settings.readline()
if robloxPath == "":
    robloxPath = prompt("fileUpload", "Select directory", "Please select your Roblox installation")
    settings.write(robloxPath)
print(robloxPath)
settings.close()

versionFolder = findVersion(robloxPath)
print(versionFolder)
if not os.path.exists(versionFolder+"/ClientSettings"):
    print("clientsettings doesn't exist!")
    os.mkdir(versionFolder+"/ClientSettings")
if not os.path.exists(versionFolder+"/ClientSettings/ClientAppSettings.json"):
        print("clientappsettings doesnt exist")
        f = open(versionFolder+"/ClientSettings/ClientAppSettings.json", "w")
        f.write("{\n\t\"FFlagDoNotLoadUnverifiedBuiltInPlugins\": false\n}")
        f.close()

builtinPath = versionFolder+"/BuiltInPlugins"
refresh()

window.mainloop()
