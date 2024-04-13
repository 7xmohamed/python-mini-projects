from tkinter import *
import ast

root = Tk()
i = 0
def getNumber(num):
    global i
    display.insert(i, num)
    i += 1

def getOperation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)  
    i += length

def clearAll():
    display.delete(0, END)

def calculate():
    entireString = display.get()
    try:
        node = ast.parse(entireString , mode= "eval")
        result = eval(compile(node, '<string>', 'eval'))
        clearAll()
        display.insert(0,result)
    except Exception:
        clearAll()
        display.insert(0, 'Error')
        
def undo():
    entireString = display.get()
    if len(entireString):
        newString = entireString[:-1]
        clearAll()
        display.insert(0, newString)
    else:
        clearAll()
        display.insert(0, "")



display = Entry(root)
display.grid(row=1, columnspan=6)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for x in range(3):
    for y in range(3):
        buttonText = numbers[counter]
        button = Button(root, text = buttonText,width=2 , height=2, command=lambda text = buttonText:getNumber(text))
        button.grid(row=x+2, column=y)
        counter+= 1


button = Button(root , text='0', width=2, height=2 , command=lambda :getNumber(0))
button.grid(row=5, column=1)

count = 0
operations = ['+', '-', '*', '/', '*3.14', '%', '(', '**', ')', '**2']
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = Button(root, text= operations[count], width=2, height=2 ,command=lambda text = operations[count]: getOperation(text))
            count += 1
            button.grid(row=x+2, column=y+3)


Button(root, text='AC', width=2, height=2, command= clearAll).grid(row=5 , column=0)
Button(root, text='=', width=2, height=2, command=calculate).grid(row=5 , column=2)
Button(root, text="<-", width=2, height=2, command= lambda: undo()).grid(row=5, column=4)

root.mainloop()

