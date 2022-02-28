from tkinter import *
import os
import random
from tkinter import filedialog
import webbrowser

root = Tk()
root.title("")
root.geometry("340x55")
root.resizable(False, False)
if os.path.exists("./favicon-32x32.png"):
    icon = PhotoImage(file = "favicon-32x32.png")
    root.iconphoto(False, icon) 

# You could change this to create a default folder
chosen_folder = (r"")

# Print to console count (ln 50)
def logCount():
    getFileCount(1)
    
# Print to console selection (ln 66)
def logSelection():
    print("Selected File: " + chooseFile.strSelectedFile)

# Get the list of files from a folder
def getFileList(chosen_folder):
    getFileList.fileList = [f for f in os.listdir(chosen_folder) if f.endswith(('.url', '.lnk', '.exe'))]
    if not getFileList.fileList:
        print("Failed to find any valid files in directory")
    else:
        #logCount()
        getFileCount(0)
        return getFileList.fileList 
        
# Choose a random file from list of file
def getRandomFile(totalFiles, files):
    choice = random.randint(0,totalFiles-1)
    return files[choice]

# Get total number of files in dir, if mode == 1 print to console
def getFileCount(mode):
    if mode == 0:
        i = 0
        while i < (len(getFileList.fileList)):
            i += 1
        getFileCount.totalFiles = i
    elif mode == 1:
        print("\n==========fileList==========")
        i = 0
        while i < (len(getFileList.fileList)):
            file = str(getFileList.fileList[i])
            print(file[:len(file)-4])
            i += 1
        print("==========fileList==========")
        getFileCount.totalFiles = i
        print("Total Files Found: " + str(getFileCount.totalFiles))

# Main function that runs all the stuff
def chooseFile():
    if chosen_folder != "":
        files = getFileList(chosen_folder)
        if files:
            chooseFile.selectedFile = getRandomFile(getFileCount.totalFiles, files)
            chooseFile.strSelectedFile = (chooseFile.selectedFile[:len(chooseFile.selectedFile)-4])
            #logSelection()
            updateChoiceLabel()
        else:
            lblFileChosen.config(text="There was an issue! Please check the directory in Settings.", fg="red")
    
# Show the user the chosen file    
def updateChoiceLabel():
    lblFileChosen.config(text=chooseFile.strSelectedFile, bg="black", fg="white")
    btnRunFile.config(text="Play", bg="green", fg="white")
    
# Run the chosen file    
def runFile():
    if chosen_folder != "" and chooseFile.selectedFile:
        webbrowser.open(chosen_folder + r"\\" + chooseFile.selectedFile)
    exit()

# Save new directory path
def saveDir(newfolder):
    global chosen_folder 
    if os.path.exists(newfolder):
        chosen_folder = newfolder
        lblFileChosen.config(text="Directory Set! Click Choose.", bg="black", fg="white")
        openDirMgr.window.destroy()
    else:
        lblFileChosen.config(text="There was an issue! Please check the directory in Settings.", fg="red")

# File Dialog prompt for directory selection
def findDir():
    newfolder = filedialog.askdirectory()
    saveDir(newfolder)
    lblFileChosen.config(text="Directory Set! Click Choose.", bg="black", fg="white")

# Spawn new window for directory changing
def openDirMgr():
    openDirMgr.window = Tk()
    openDirMgr.window.geometry("400x70")
    openDirMgr.window.title("RSGS - Dir Manager")
    openDirMgr.window.resizable(False, False)
    lblDir = Label(openDirMgr.window, text="Path", justify=LEFT)
    lblDir.grid(row=0, column=0)
    eDirectory = Entry(openDirMgr.window, width=62)
    eDirectory.grid(row=1, column=0, columnspan = 8, padx=10)
    eDirectory.delete(1, END)
    eDirectory.insert(0, str(chosen_folder))
    btnSelectDir = Button(openDirMgr.window, text="Select", command=findDir)
    btnSelectDir.grid(row=2, column=0)
    btnSaveDir = Button(openDirMgr.window, text="Save", command=lambda:saveDir(eDirectory.get()))
    btnSaveDir.grid(row=2, column=7)
    lblNotice = Label(openDirMgr.window, text="Directory can have .exe, .url, or .lnk files", fg="grey")
    lblNotice.grid(row=2, column=3)

# GUI Items
lblFileChosen = Label(root, text="Click Change Directory Button to set, then Click Choose.", width= 50)
lblFileChosen.grid(row=0, column=0, columnspan=12)
btnchooseFile = Button(root, text="Choose", command=chooseFile)
btnchooseFile.grid(row=1, column=3)
btnRunFile = Button(root, text="Start", command=runFile)
btnRunFile.grid(row=1, column=5)
btnChangeDir = Button(root, text="Change Directory", command=openDirMgr)
btnChangeDir.grid(row=1, column=7)

root.mainloop()
