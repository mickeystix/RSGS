from tkinter import *
import os
import random
from tkinter import filedialog
import webbrowser
from xmlrpc.client import boolean

root = Tk()
root.title("")
root.geometry("340x55")
root.resizable(False, False)
if os.path.exists("./favicon-32x32.png"):
    icon = PhotoImage(file = "favicon-32x32.png")
    root.iconphoto(False, icon) 

# You could change this to create a default folder
games_folder = (r"")

# Print to console count (ln 50)
def logCount():
    getGameCount(1)
    
# Print to console selection (ln 66)
def logSelection():
    print("Selected Game: " + chooseGame.strSelectedGame)

# Get the list of games from a folder
def getGameList(games_folder):
    getGameList.gameList = [f for f in os.listdir(games_folder) if f.endswith(('.url', '.lnk', '.exe'))]
    if not getGameList.gameList:
        print("Failed to find any games in directory")
    else:
        #logCount()
        getGameCount(0)
        return getGameList.gameList 
        
# Choose a random game from list of games
def getRandomGame(totalgames, games):
    choice = random.randint(0,totalgames-1)
    return games[choice]

# Get total number of games in dir, if mode == 1 print to console
def getGameCount(mode):
    if mode == 0:
        i = 0
        while i < (len(getGameList.gameList)):
            i += 1
        getGameCount.totalGames = i
    elif mode == 1:
        print("\n==========GAMELIST==========")
        i = 0
        while i < (len(getGameList.gameList)):
            game = str(getGameList.gameList[i])
            print(game[:len(game)-4])
            i += 1
        print("==========GAMELIST==========")
        getGameCount.totalGames = i
        print("Total Games Found: " + str(getGameCount.totalGames))

# Main function that runs all the stuff
def chooseGame():
    if games_folder != "":
        games = getGameList(games_folder)
        if games:
            chooseGame.selectedGame = getRandomGame(getGameCount.totalGames, games)
            chooseGame.strSelectedGame = (chooseGame.selectedGame[:len(chooseGame.selectedGame)-4])
            #logSelection()
            updateChoiceLabel()
        else:
            lblGameChosen.config(text="There was an issue! Please check the directory in Settings.", fg="red")
    
# Show the user the chosen game    
def updateChoiceLabel():
    lblGameChosen.config(text=chooseGame.strSelectedGame, bg="black", fg="white")
    btnRunGame.config(text="Play", bg="green", fg="white")
    
# Run the chosen game    
def runGame():
    if games_folder != "" and chooseGame.selectedGame:
        webbrowser.open(games_folder + r"\\" + chooseGame.selectedGame)
    exit()

# Save new directory path
def saveDir(newfolder, window):
    global games_folder 
    if os.path.exists(newfolder):
        games_folder = newfolder
        lblGameChosen.config(text="Directory Set! Click Choose.", bg="black", fg="white")
        openDirMgr.window.destroy()
    else:
        lblGameChosen.config(text="There was an issue! Please check the directory in Settings.", fg="red")

# File Dialog prompt for directory selection
def findDir(window):
    newfolder = filedialog.askdirectory()
    saveDir(newfolder, window)
    lblGameChosen.config(text="Directory Set! Click Choose.", bg="black", fg="white")

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
    eDirectory.insert(0, str(games_folder))
    btnSelectDir = Button(openDirMgr.window, text="Select", command=lambda:findDir(openDirMgr.window))
    btnSelectDir.grid(row=2, column=0)
    btnSaveDir = Button(openDirMgr.window, text="Save", command=lambda:saveDir(eDirectory.get(), openDirMgr.window))
    btnSaveDir.grid(row=2, column=7)
    lblNotice = Label(openDirMgr.window, text="Directory can have .exe, .url, or .lnk files", fg="grey")
    lblNotice.grid(row=2, column=3)

# GUI Items
lblGameChosen = Label(root, text="Click Change Directory Button to set, then Click Choose.", width= 50)
lblGameChosen.grid(row=0, column=0, columnspan=12)
btnChooseGame = Button(root, text="Choose", command=chooseGame)
btnChooseGame.grid(row=1, column=3)
btnRunGame = Button(root, text="Play", command=runGame)
btnRunGame.grid(row=1, column=5)
btnChangeDir = Button(root, text="Change Directory", command=openDirMgr)
btnChangeDir.grid(row=1, column=7)

root.mainloop()