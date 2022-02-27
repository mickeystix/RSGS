from tkinter import *
import os
import random
import webbrowser

root = Tk()

root.title("RSGS")
root.geometry("400x100")
root.resizable(False, False)

games_folder = (r"")

# Get the list of games from a folder
def getGameList(games_folder):
    gameList = [f for f in os.listdir(games_folder) if f.endswith('.url')]
    if not gameList:
        print("Failed to find any games in directory")
    else:    
        return gameList

# Choose a random game from list of games
def getRandomGame(totalgames, games):
    choice = random.randint(0,totalgames-1)
    return games[choice]

# Main function that runs all the stuff
def chooseGame():
    games = getGameList(games_folder)
    totalgames = 0
    if games:
        for game in games:
            totalgames += 1
        chooseGame.selectedGame = getRandomGame(totalgames, games)
        chooseGame.strSelectedGame = (chooseGame.selectedGame[:len(chooseGame.selectedGame)-4])
        print(chooseGame.strSelectedGame)
        updateChoiceLabel()
    

# Show the user the chosen game    
def updateChoiceLabel():
    lblGameChosen.config(text=chooseGame.strSelectedGame)
    
# Run the chosen game    
def runGame(selectedGame):
    webbrowser.open(games_folder + r"\\" + chooseGame.selectedGame)

# Save new directory path
def saveDir(newfolder):
    global games_folder 
    games_folder = newfolder

# Spawn new window for directory changing
def openDirMgr():
    dc = Tk()
    dc.geometry("400x85")
    dc.title("RSGS - Dir Manager")
    dc.resizable(False, False)
    lblDir = Label(dc, text="Path", justify=LEFT).pack()
    eDirectory = Entry(dc, width=80)
    eDirectory.pack(padx=10)
    eDirectory.delete(1, END)
    eDirectory.insert(0, str(games_folder))
    btnSaveDir = Button(dc, text="Save", command=lambda:saveDir(eDirectory.get()))
    btnSaveDir.pack()
    lblNotice = Label(dc, text="Directory should have Steam .url shortcuts", fg="grey")
    lblNotice.pack()
    lblNotice2 = Label(dc, text="Double \ is not required, simple copy and paste the path", fg="grey")
    lblNotice2.pack()

# Gui Items
btnChooseGame = Button(root, text="Choose", command=chooseGame).pack()
lblGameChosen = Label(root, text="Click Change Directory Button to set, then Click Choose button")
lblGameChosen.pack()
btnRunGame = Button(root, text="Play", command=lambda:runGame(chooseGame.selectedGame)).pack()
btnChangeDir = Button(root, text="Change Directory", command=openDirMgr).pack()

root.mainloop()
