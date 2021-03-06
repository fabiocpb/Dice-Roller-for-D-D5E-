import random
from tkinter import*
from tkinter import scrolledtext
from tkinter.filedialog import asksaveasfile
from fpdf import FPDF

main_window = Tk()
main_window.title("Fabio´s Dice Roller")
#main_window.geometry("350x550")

# Labels
#Label(main_window, text= "# of Dices and Sides").grid(row = 2, column = 0)
Label(main_window, text= "# of Dices").grid(row = 1, column = 1)
Label(main_window, text= "# of Sides").grid(row = 1, column = 3)
Label(main_window, text= "Modifier").grid(row = 1, column = 4)
Label(main_window, text= "d").grid(row = 2, column = 2)

# Text Input

numdice = Entry(main_window, width=5, borderwidth =5)
numdice.grid(row = 2, column = 1)
numsides = Entry(main_window, width=5, borderwidth =5)
numsides.grid(row = 2, column = 3)
modifier = Entry(main_window, width=5, borderwidth =5)
modifier.grid(row = 2, column = 4)

#Default value 0
if numdice!= int:
    numdice.insert(0, 0)
if numsides!= int :
    numsides.insert(0, 0)
if modifier!= int :
    modifier.insert(0, 0)

#String Var and Display Field

result = StringVar()
resultdisplay = Entry(main_window, textvariable=result, state=DISABLED)
resultdisplay.grid(columnspan = 100, ipadx=90, ipady=2)
if resultdisplay!= int:
    resultdisplay.insert(0, 0)


#def on_click():
     #print(f"my name is {my_name.get()} and my age is {my_age.get()}")

def rolldice():
    global rolltimes
    global sides
    global intmod
    global currentRolls
    global diceTotal
    rolltimes = int(numdice.get())
    sides = int(numsides.get())
    intmod = int(modifier.get())
    currentRolls=0
    diceTotal = 0
    while currentRolls < rolltimes:
        randDice = random.randint(1, sides)
        currentRolls += 1
        diceTotal += randDice
        totalResult = diceTotal + intmod
        #print(randDice)
    finalout = f"Roll total for {rolltimes}d{sides} + {intmod} is {totalResult} ({diceTotal} + {intmod})."
    print(f"Roll Total = {totalResult}")
    result.set(finalout)

def rollAdv():
    global advDice
    global randDice
    global randDiceB
    rolltimes = int(numdice.get())
    sides = int(numsides.get())
    intmod = int(modifier.get())
    if rolltimes == 2 and sides == 20:
        randDice = random.randint(1, sides)
        randDiceB = random.randint(1, sides)
        if randDice >= randDiceB:
            advDice = randDice
        else:
            advDice = randDiceB
        totalResult = advDice + intmod
        print(randDice, randDiceB)
        print(f"{rolltimes}d{sides}({advDice}) {intmod} = {totalResult}")
        print(f"Roll Total = {totalResult}")
        result.set(totalResult)
    else:
        print("This is not a 2d20 advantage roll!")
        result.set("This is not a 2d20 advantage roll!")
def rollDisadv():
    rolltimes = int(numdice.get())
    sides = int(numsides.get())
    intmod = int(modifier.get())
    if rolltimes == 2 and sides == 20:
        randDice = random.randint(1, sides)
        randDiceB = random.randint(1, sides)
        if randDice <= randDiceB:
            advDice = randDice
        else:
            advDice = randDiceB
        totalResult = advDice + intmod
        print(randDice, randDiceB)
        print(f"{rolltimes}d{sides}({advDice}) {intmod} = {totalResult}")
        print(f"Roll Total = {totalResult}")
        result.set(totalResult)
    else:
        print("This is not a 2d20 disadvantage roll!")
        result.set("This is not a 2d20 disadvantage roll!")

def totalResult():
    print(f"{rolltimes}d{sides}({advDice}) + {intmod} = {totalResult}")


#Buttons
Button(main_window, text="Roll!", command = rolldice).grid(row =2,column=5)
Button(main_window, text="Adv", command = rollAdv).grid(row =2,column=6)
Button(main_window, text="Disadv", command = rollDisadv).grid(row =2,column=7)

#Scrolled Text Notas do DM
notasdodm = scrolledtext.ScrolledText(main_window, wrap=WORD, width=40, height=30, font=("Currier New", 10))
notasdodm.grid(columnspan = 30, ipadx =10)

def savetext():
    files = [('All Files', '*.*'),
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes=files, defaultextension=files)
    dmtxt = str(notasdodm.get("1.0", "end-1c"))
    file.write (dmtxt)
    file.close()
    #doc = open("dm_notes01.txt", "r")
    #print(doc.read())

Button(main_window, text="Save as .txt", command = savetext).grid(row =10,column=4)
#Label(main_window, text = f"{totalResult}").grid(row =3,column = 2)

main_window.mainloop()