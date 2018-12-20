#----------------------------------------------
# Stay Alive!
#----------------------------------------------

#import the modules we need, for creating a GUI
import tkinter

#only press return once
okToPressReturn = True

#the player's attributes.
hunger = 100
day = 0
entertained = 50

#-------------------------------------------------------------------

def startGame(event):

    global okToPressReturn

    if okToPressReturn == False:
        pass
    
    else:
        #update the time left label.
        startLabel.config(text="")
        #start updating the values
        updateHunger()
        updateDay()
        updatePlay()
        updateDisplay()

        okToPressReturn = False

# -------------------------------------------------------------------
 
def updateDisplay():
    #use the globally declared variables above.
    global hunger
    global day

    if hunger <= 50:
        if hunger > 0:
            bearPic.config(image=hungryphoto)
        else:
            bearPic.config(image=gameoverphoto)
    else:
        if entertained > 0:
            if entertained >= 25:
                bearPic.config(image=normalphoto)
            else:
                bearPic.config(image=boredphoto)
        else:
            bearPic.config(image=runawayphoto)


    #update the time left label.
    hungerLabel.config(text="Hunger: " + str(hunger))

    #update the day label.
    dayLabel.config(text="Day: " + str(day))

    #update the entertained label.
    entertainedLabel.config(text="Entertained: " + str(entertained))

    #run the function again after 100ms.
    bearPic.after(100, updateDisplay)

#-------------------------------------------------------------------
 
def updateHunger():

    #use the globally declared variables above.
    global hunger

    #decrement the hunger.
    hunger -= 1

    if isAlive():
        #run the function again after 500ms.
        hungerLabel.after(500, updateHunger)

#-------------------------------------------------------------------

def updateDay():

    #use the globally declared variables above.
    global day

    #decrement the hunger.
    day += 1

    if isAlive():
        #run the function again after 5s.
        dayLabel.after(5000, updateDay)

# -------------------------------------------------------------------

def updatePlay():

    #use globally declared variables above.
    global entertained

    #decrement entertainment
    entertained -= 1

    if isAlive():
        #run function again after 500ms
        entertainedLabel.after(500, updatePlay)

# -------------------------------------------------------------------

def feed():

    global hunger
    
    if hunger <= 95:
        hunger += 15
    else:
        hunger -= 50
        
#-------------------------------------------------------------------
def play():

    global entertained

    if entertained <= 40:
        entertained += 20
    else:
        entertained -= 20

# -------------------------------------------------------------------
def isAlive():

    global hunger
    
    if hunger <= 0:
        #update the start info label with death.
        bearPic.config(image=gameoverphoto)
        startLabel.config(text="GAME OVER! YOUR BEAR DIED OF HUNGER!")
        return False
    elif entertained <= 0:
        bearPic.config(image=runawayphoto)
        startLabel.config(text="GAMEOVER! YOUR BEAR RAN AWAY!")
    else:
        return True
        
#-------------------------------------------------------------------


#create a GUI window.
root = tkinter.Tk()
#set the title.
root.title("Stay Alive!")
#set the size.
root.geometry("1000x1000")

#add a label for the start text.
startLabel = tkinter.Label(root, text="Press 'Return' to start!", font=('Helvetica', 12, 'bold'))
startLabel.pack()

#add a hunger label.
hungerLabel = tkinter.Label(root, text="Hunger: " + str(hunger), font=('Helvetica', 12))
hungerLabel.pack()

#add a 'day' label.
dayLabel = tkinter.Label(root, text="Day: " + str(day), font=('Helvetica', 12))
dayLabel.pack()

#add an entertained label
entertainedLabel = tkinter.Label(root, text="Entertained: " + str(entertained), font=('Helvetica', 12))
entertainedLabel.pack()

hungryphoto = tkinter.PhotoImage(file="hungry.png")
normalphoto = tkinter.PhotoImage(file="normal.png")
boredphoto = tkinter.PhotoImage(file="bored.png")
gameoverphoto = tkinter.PhotoImage(file="gameOver.png")
runawayphoto = tkinter.PhotoImage(file="runaway.png")

#add a bear image
bearPic = tkinter.Label(root, image=normalphoto)
bearPic.pack()

btnFeed = tkinter.Button(root, text="Feed Me", command=feed)
btnFeed.pack()

btnPlay = tkinter.Button(root, text="Play With Me", command=play)
btnPlay.pack()

#run the 'startGame' function when the enter key is pressed.
root.bind('<Return>', startGame)

#start the GUI
root.mainloop()
