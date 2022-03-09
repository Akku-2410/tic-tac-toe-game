#!/usr/bin/env python
# coding: utf-8

# In[10]:


from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Tic-Tac-Toe')
root.resizable(height=False, width=False)
click = True
count = 0

btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()

btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()

btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

xPhoto = PhotoImage(file = 'Tic Tac Toe\\x.png')
oPhoto = PhotoImage(file = 'Tic Tac Toe\\o.png' )

def play():
    button1 = Button(root,height = 10, width = 20, relief = 'ridge', borderwidth = 5, background = '#e6ffe6', textvariable = btn1, command = lambda:press(1,0,0))
    button1.grid(row = 0, column = 0)
    
    button2 = Button(root,height = 10, width = 20, relief = 'ridge', borderwidth = 5, background = '#e6ffe6', textvariable = btn1, command = lambda:press(2,0,1))
    button2.grid(row = 0, column = 1)
    
    button3 = Button(root,height = 10, width = 20, relief = 'ridge', borderwidth = 5, background = '#e6ffe6', textvariable = btn1, command = lambda:press(3,0,2))
    button3.grid(row = 0, column = 2)
    
    button4 = Button(root,height = 10, width = 20, relief = 'ridge', borderwidth = 5, background = '#b3ffb3', textvariable = btn1, command = lambda:press(4,1,0))
    button4.grid(row = 1, column = 0)
    
    button5 = Button(root,height = 10, width = 20, relief = 'ridge', borderwidth = 5, background = '#b3ffb3', textvariable = btn1, command = lambda:press(5,1,1))
    button5.grid(row = 1, column = 1)
    
    button6 = Button(root,height = 10, width = 20, relief = 'ridge', borderwidth = 5, background = '#b3ffb3', textvariable = btn1, command = lambda:press(6,1,2))
    button6.grid(row = 1, column = 2)
    
    button7 = Button(root,height = 10, width = 20, relief = 'ridge', borderwidth = 5, background = '#80ff80', textvariable = btn1, command = lambda:press(7,2,0))
    button7.grid(row = 2, column = 0)
    
    button8 = Button(root,height = 10, width = 20, relief = 'ridge', borderwidth = 5, background = '#80ff80', textvariable = btn1, command = lambda:press(8,2,1))
    button8.grid(row = 2, column = 1)
    
    button9 = Button(root,height = 10, width = 20, relief = 'ridge', borderwidth = 5, background = '#80ff80', textvariable = btn1, command = lambda:press(9,2,2))
    button9.grid(row = 2, column = 2)
    
def press(num,r,c):
    global click, count
    
    if click==True:
        labelPhoto = Label(root, image = xPhoto)
        labelOhoto.grid(row=r, column=c)
        if num==1:
            btn1.set("X")
        elif num==2:
            btn2.set("X")
        elif num==3:
            btn3.set("X")
        elif num==4:
            btn4.set("X")
        elif num==5:
            btn5.set("X")
        elif num==6:
            btn6.set("X")
        elif num==7:
            btn7.set("X")
        elif num==8:
            btn8.set("X")
        else:
            btn9.set('X')
        count +=1
        click = False
        checkWin()
            
    else:
        labelPhoto = Label(root, image = oPhoto)
        labelPhoto.grid(row=r, column=c)
            
        if num==1:
            btn1.set('O')
        elif num==2:
            btn2.set('O')
        elif num==3:
            btn3.set('O')
        elif num==4:
            btn4.set('O')            
        elif num==5:
            btn5.set('O')             
        elif num==6:
            btn6.set('O')             
        elif num==7:
            btn7.set('O')             
        elif num==8:
            btn8.set('O')
        else:
            btn9.set('O')
        count +=1
        click = True
        checkWin()
        
        
def checkWin():
    global count, click
    if(btn1.get=='X' and btn2.get()=='x' and btn3.get()=='X' or
       btn4.get=='X' and btn5.get()=='x' and btn6.get()=='X' or
       btn7.get=='X' and btn8.get()=='x' and btn9.get()=='X' or
       btn1.get=='X' and btn4.get()=='x' and btn7.get()=='X' or
       btn2.get=='X' and btn5.get()=='x' and btn8.get()=='X' or
       btn3.get=='X' and btn6.get()=='x' and btn9.get()=='X' or
       btn1.get=='X' and btn5.get()=='x' and btn9.get()=='X' or
       btn3.get=='X' and btn5.get()=='x' and btn7.get()=='X'):
        messagebox.showinfo("Tic Tac Toe", "Player X wins!")
        click = True
        count = 0
        clear()
        play()
    elif(btn1.get=='O' and btn2.get()=='O' and btn3.get()=='O' or
         btn4.get=='O' and btn5.get()=='O' and btn6.get()=='O' or
         btn7.get=='O' and btn8.get()=='O' and btn9.get()=='O' or
         btn1.get=='O' and btn4.get()=='O' and btn7.get()=='O' or
         btn2.get=='O' and btn5.get()=='O' and btn8.get()=='O' or
         btn3.get=='O' and btn6.get()=='O' and btn9.get()=='O' or
         btn1.get=='O' and btn5.get()=='O' and btn9.get()=='O' or
         btn3.get=='O' and btn5.get()=='O' and btn7.get()=='O'):
        messagebox.showinfo("Tic Tac Toe", "Player O wins!")
        click = True
        count = 0
        clear()
        play()
    elif(count==9):
        message.box.showinfo("Tic Tac Toe", "Tie Game!")
        click = True
        count = 0
        clear()
        play()
        
def clear():
    btn1.set("")
    btn2.set("")
    btn3.set("")
    btn4.set("")
    btn5.set("")
    btn6.set("")
    btn7.set("")
    btn8.set("")
    btn9.set("")
    
play()
root.mainloop()
        


# In[ ]:




