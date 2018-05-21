from Tkinter import *
from tkMessageBox import * 

#them thu vien MessageBox
import tkMessageBox 

root = Tk()
root.title("App Project")
#root.configure(bg="black")
root.geometry("600x700")
menu = Menu(root)
root.config(menu=menu)

def NewFile():
    print "Chua lam !"
def OpenFile():
    print "Error !"
def kitchen():
    print "So Hot !"
def About():
    print "Please seach Google ! Because it's free "
def idle():
    print "Please contact 0981.348.398 "
def exits():
    if askyesno('Verify', 'Really exit ?'):
        showinfo('Yes', 'Good Bye')
        print "See you later !"
        root.destroy()
    else:
        showinfo('No', 'You Turn Back !')
        print "Welcome Back !"

on = PhotoImage(file="on.gif").subsample(3,3)
off = PhotoImage(file="off.gif").subsample(3,3)

high = PhotoImage(file="high.gif").subsample(5,5)
low = PhotoImage(file="low.gif").subsample(5,5)
    




# DEN
def toggle_den():
    """toggle button text between Hi and Goodbye"""
    if btn["text"] == "ON":
        # switch to OFF
        btn["text"] = "OFF"
        lb_3=Label(root, image=on)
        lb_3.place(x=550, y=300)
        
    else:
        # reset to ON
        btn["text"] = "ON"
        lb_3=Label(root, image=off)
        lb_3.place(x=550, y=300)
      

def toggle_den1():
    """toggle button text between Hi and Goodbye"""
    if btn1["text"] == "ON":
        # switch to OFF
        btn1["text"] = "OFF"
        lb_3=Label(root, image=on)
        lb_3.place(x=550, y=350)
    else:
        # reset to ON
        btn1["text"] = "ON"
        lb_3=Label(root, image=off)
        lb_3.place(x=550, y=350)

def toggle_den2():
    """toggle button text between Hi and Goodbye"""
    if btn2["text"] == "ON":
        # switch to OFF
        btn2["text"] = "OFF"
        lb_3=Label(root, image=on)
        lb_3.place(x=550, y=400)
    else:
        # reset to ON
        btn2["text"] = "ON"
        lb_3=Label(root, image=off)
        lb_3.place(x=550, y=400)

#QUAT
def toggle_quat():
    """toggle button text between Hi and Goodbye"""
    if btn3["text"] == "ON":
        # switch to OFF
        btn3["text"] = "OFF"
        lb_3=Label(root, image=high)
        lb_3.place(x=150, y=302)
    else:
        # reset to ON
        btn3["text"] = "ON"
        lb_3=Label(root, image=low)
        lb_3.place(x=150, y=302)

def toggle_quat1():
    """toggle button text between Hi and Goodbye"""
    if btn4["text"] == "ON":
        # switch to OFF
        btn4["text"] = "OFF"
        lb_3=Label(root, image=high)
        lb_3.place(x=150, y=352)
    else:
        # reset to ON
        btn4["text"] = "ON"
        lb_3=Label(root, image=low)
        lb_3.place(x=150, y=352)

def toggle_quat2():
    """toggle button text between Hi and Goodbye"""
    if btn5["text"] == "ON":
        # switch to OFF
        btn5["text"] = "OFF"
        lb_3=Label(root, image=high)
        lb_3.place(x=150, y=402)
       
    else:
        # reset to ON
        btn5["text"] = "ON"
        lb_3=Label(root, image=low)
        lb_3.place(x=150, y=402)
       
    

    



#CHEN BACKGOUND
photo = PhotoImage(file="1.gif")
lb1 = Label(root, image = photo).place(x=0, y=0)


# button den
btn = Button( text="ON", width=5, command=toggle_den,font=('Harrington',15,'bold'))
btn.place(x=465, y=300)

btn1 = Button( text="ON", width=5, command=toggle_den1,font=('Harrington',15,'bold'))
btn1.place(x=465, y=350)

btn2 = Button( text="ON", width=5, command=toggle_den2,font=('Harrington',15,'bold'))
btn2.place(x=465, y=400)

# button quat
btn3 = Button( text="ON", width=5, command=toggle_quat,font=('Harrington',15,'bold'))
btn3.place(x=60, y=300)

btn4 = Button( text="ON", width=5, command=toggle_quat1,font=('Harrington',15,'bold'))
btn4.place(x=60, y=350)

btn5 = Button( text="ON", width=5, command=toggle_quat2,font=('Harrington',15,'bold'))
btn5.place(x=60, y=400)



# tao thanh cong cu

# tao 1 menu file
filemenu = Menu(menu)
menu.add_cascade(label="Temp & Humi", menu=filemenu)  # thanh chon
filemenu.add_command(label="Bed room", command=NewFile)
filemenu.add_command(label="Living room", command=OpenFile)
filemenu.add_command(label="Kitchen", command=kitchen)

# tao 1 menu  Help
helpmenu = Menu(menu)
menu.add_cascade(label="Help & Exit", menu=helpmenu)  # thanh chon
helpmenu.add_command(label="Help to use ", command=About)
helpmenu.add_command(label="More infors ", command=idle)
helpmenu.add_separator() # tao cai gach ngang
helpmenu.add_command(label="Exit ", command=exits)

text1 = Text(root,bg ="PINK", height=5, width=60)
text1.pack(ipadx=15,padx=70,pady=80, ipady=20,side=TOP)

w = Label(root, text="QUAT", bg="grey", fg="yellow", height=1, width=5 ,font=('Harrington',24,'bold'))
w.place(x=45, y=250)
w1 = Label(root, text="DEN", bg="grey", fg="red", height=1, width=5 , font=('Harrington',24,'bold'))
w1.place(x=450, y=250)


root.mainloop()
