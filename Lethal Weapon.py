#Game to find out which Lethal weapon character you are
# import GUI and Random Libraries
import tkinter
import random
#List the possible names to be chosen
names = ['McNeille','Martin Riggs','Detective Murtaugh','Bailey','Schorsese','Avery','Bowman','Daddy Riggs','Captain Rog','Fanboy', 'Trish Murtaugh']

#define the name picking function
def pickName():
    nameLabel.configure(text=random.choice(names))

 #define the GUI window
root = tkinter.Tk()
root.title("Lethal Weapon Name Picker")
root.geometry("400x100")

#add a label to display the name
nameLabel = tkinter.Label(root, text="", font=('Times New Roman',30))
nameLabel.pack()

#add a "pick Name" button
pickButton = tkinter.Button(text="Who Are You?", width=15, command=pickName)
pickButton.pack(side="bottom")

#start the GUI
root.mainloop()

