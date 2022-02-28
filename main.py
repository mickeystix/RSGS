from tkinter import *
import os
import random
import webbrowser

root = Tk()

root.title("")
root.geometry("340x60")
root.resizable(False, False)
if os.path.exists("./favicon-32x32.png"):
    icon = PhotoImage(file = "favicon-32x32.png")
    root.iconphoto(False, icon) 


games_folder = (r"")

def logList():
    # Logging to console
    print("\n==========GAMELIST==========")
    i = 0
    while i < (len(getGameList.gameList)):
        game = str(getGameList.gameList[i])
        print(game[:len(game)-4])
        i += 1
    print("==========GAMELIST==========")
    getGameList.totalGames = i
    print("Total Games Found: " + str(getGameList.totalGames))
    # End Logging

def logSelection():
    print("Selected Game: " + chooseGame.strSelectedGame)

# Get the list of games from a folder
def getGameList(games_folder):
    getGameList.gameList = [f for f in os.listdir(games_folder) if f.endswith(('.url', '.lnk', '.exe'))]
    if not getGameList.gameList:
        print("Failed to find any games in directory")
    else:
        logList()
        return getGameList.gameList 
        
# Choose a random game from list of games
def getRandomGame(totalgames, games):
    choice = random.randint(0,totalgames-1)
    return games[choice]

# Main function that runs all the stuff
def chooseGame():
    games = getGameList(games_folder)
    #totalgames = 0
    if games:
        #for game in games:
        #    totalgames += 1
        chooseGame.selectedGame = getRandomGame(getGameList.totalGames, games)
        chooseGame.strSelectedGame = (chooseGame.selectedGame[:len(chooseGame.selectedGame)-4])
        logSelection()
        updateChoiceLabel()
    
# Show the user the chosen game    
def updateChoiceLabel():
    lblGameChosen.config(text=chooseGame.strSelectedGame)
    
# Run the chosen game    
def runGame():
    webbrowser.open(games_folder + r"\\" + chooseGame.selectedGame)

# Save new directory path
def saveDir(newfolder):
    global games_folder 
    games_folder = newfolder

# Spawn new window for directory changing
def openDirMgr():
    dc = Tk()
    dc.geometry("400x120")
    dc.title("RSGS - Dir Manager")
    dc.resizable(False, False)
    lblDir = Label(dc, text="Path", justify=LEFT)
    lblDir.grid(row=0, column=0)
    eDirectory = Entry(dc, width=62)
    eDirectory.grid(row=1, column=0, columnspan=6, padx=10)
    eDirectory.delete(1, END)
    eDirectory.insert(0, str(games_folder))
    btnSaveDir = Button(dc, text="Save", command=lambda:saveDir(eDirectory.get()))
    btnSaveDir.grid(row=3, column=1)
    lblNotice = Label(dc, text="Directory can have .exe, .url, or .lnk files", fg="grey")
    lblNotice.grid(row=4, column=1)
    lblNotice2 = Label(dc, text="For best results, simply copy and paste the path", fg="grey")
    lblNotice2.grid(row=5, column=1)

# GUI Items
lblGameChosen = Label(root, text="Click Change Directory Button to set, then Click Choose.", width= 50)
lblGameChosen.grid(row=0, column=0, columnspan=12)
btnChooseGame = Button(root, text="Choose", command=chooseGame)
btnChooseGame.grid(row=1, column=3)
btnRunGame = Button(root, text="Play", command=lambda:runGame())
btnRunGame.grid(row=1, column=5)
btnChangeDir = Button(root, text="Change Directory", command=openDirMgr)
btnChangeDir.grid(row=1, column=7)

root.mainloop()