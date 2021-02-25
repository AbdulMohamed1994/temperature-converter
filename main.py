from tkinter import *
import tkinter as tk

#defin formular
def convert_C():
    if E1:
        fahrenheit = float(E1.get())
        celcius = (fahrenheit-32)*5/9
        result_entry.insert(0, celcius)
def convert_F():
    if E2:
        celcius = float(E2.get())
        fahrenheit = (celcius*9/5)+32
        result_entry.insert(0, fahrenheit)

#window
win = Tk()



#Labelfram and entry 1
l1=LabelFrame(win,text='Celcius To Fahrenheit',padx=40, pady=40, bg='light blue')
l1.pack(fill="both")
l1.place(x=30, y=50)

E1=Entry(l1,state='disable')
E1.pack()

def Cel_Active():
    E1.configure(state='normal')
    if E2 == normal:
        E1.configure(state='disable')
#Button C - F
b1=Button(win,text='Activate -Celcius to Fahrenheit', command=Cel_Active, bg='light blue')
b1.place(x=30, y=250)

#label frame and entry 2
l2=LabelFrame(win, text='Fahrenheit to Celcius',padx=40, pady=40, bg='light pink')
l2.pack(fill="both")
l2.place(x=310, y=50)
E2=Entry(l2,state='disable')
E2.pack()

#defin btn
def Far_Active():
    E2.configure(state='normal')
    if E1 == normal:
        E2.configure(state='disable')

#Button 2 F -C
b2=Button(win,text='Activate -Fahrenheit to Celcius', command=Far_Active, bg='light pink')

b2.place(x=330, y=250)


#Exit Button
def exit():
    win.destroy()
exit_btn = Button(win,text = "Quit", command=exit, bg='white')
exit_btn.place(x=500, y=430)




#result button C - F
result_bnt=Button(win, text='Calculate C - F',command=convert_C, bg='light blue')
result_bnt.place(x=30, y=330)

#result button F - C
result_bnt=Button(win, text='Calculate F - C',command=convert_F, bg='light pink')
result_bnt.place(x=435, y=330)

#result entry
result_entry=Entry(win, bg='white')
result_entry.place(x=220, y=330)




#Clear button
def Clear():
    E1.delete(0, END)
    E2.delete(0, END)
    result_entry.delete(0,END)
    Clear_btn=Button(win, text='Clear',command=Clear, bg='white')
    Clear_btn.place(x=495, y=380)


win.title('Temperature Convector')
win.geometry('600x500')
win.mainloop()
