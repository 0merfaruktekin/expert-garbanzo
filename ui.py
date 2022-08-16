from tkinter import *
import solver
import word_ranking as rank
window =Tk()
word_var=StringVar()
sayac=IntVar()
sayac=0
sayac2=IntVar()
sayac2=0
sayac3=IntVar()
sayac3=0
sayac4=IntVar()
sayac4=0
sayac5=IntVar()
sayac5=0
def submit():
    word=word_var.get()
    word_var.set("")
    suggest(word)

def suggest(word):
    global sayac,sayac2,sayac3,sayac4,sayac5
    sayac_list=[sayac,sayac2,sayac3,sayac4,sayac5]
    index=0
    for i in word:
        if sayac_list[index]==0:
            solver.eliminate(i)
        elif sayac_list[index]==1:
            solver.checkpos_yellow(index,i)
        else:
            solver.checkpos_green(index,i)
        index+=1
    index=0
    for s in solver.suggestion():
        index+=1
        Lb1.delete(index)
        Lb1.insert(index,s)
def res():
    rank.reset()
    Lb1.delete(1)
    Lb1.delete(1)
    Lb1.delete(1)
    Lb1.delete(1)
    Lb1.delete(1)
#renk değiştirme fonksiyonları
def wf():
    global sayac
    sayac+=1
    if sayac==3:
        w.config(bg="Gray",activebackground="Gray")
        sayac=0
    if sayac==1:
        w.config(bg="Yellow",activebackground="Yellow")
    if sayac==2:
        w.config(bg="Green",activebackground="Green")
def wf2():
    global sayac2
    sayac2+=1
    if sayac2==3:
        w2.config(bg="Gray",activebackground="Gray")
        sayac2=0
    if sayac2==1:
        w2.config(bg="Yellow",activebackground="Yellow")
    if sayac2==2:
        w2.config(bg="Green",activebackground="Green")
def wf3():
    global sayac3
    sayac3+=1
    if sayac3==3:
        w3.config(bg="Gray",activebackground="Gray")
        sayac3=0
    if sayac3==1:
        w3.config(bg="Yellow",activebackground="Yellow")
    if sayac3==2:
        w3.config(bg="Green",activebackground="Green")
def wf4():
    global sayac4
    sayac4+=1
    if sayac4==3:
        w4.config(bg="Gray",activebackground="Gray")
        sayac4=0
    if sayac4==1:
        w4.config(bg="Yellow",activebackground="Yellow")
    if sayac4==2:
        w4.config(bg="Green",activebackground="Green")
def wf5():
    global sayac5
    sayac5+=1
    if sayac5==3:
        w5.config(bg="Gray",activebackground="Gray")
        sayac5=0
    if sayac5==1:
        w5.config(bg="Yellow",activebackground="Yellow")
    if sayac5==2:
        w5.config(bg="Green",activebackground="Green")
#text entry
e = Entry(window,bd=5,font='Arial 24',textvariable =word_var,width=30).grid(row=0,column=0,columnspan=5)
#button
w=Button(window,bg="Gray",activebackground="Gray",command=wf,height=4,width=14)
w2=Button(window,bg="Gray",activebackground="Gray",command=wf2,height=4,width=14)
w3=Button(window,bg="Gray",activebackground="Gray",command=wf3,height=4,width=14)
w4=Button(window,bg="Gray",activebackground="Gray",command=wf4,height=4,width=14)
w5=Button(window,bg="Gray",activebackground="Gray",command=wf5,height=4,width=14)
w.grid(row=1,column=0)
w2.grid(row=1,column=1)
w3.grid(row=1,column=2)
w4.grid(row=1,column=3)
w5.grid(row=1,column=4)
b=Button(window,text="suggest",command=submit,height=4,width=14).grid(row=0,column=6)
r=Button(window,text="reset",command=res,height=4,width=14).grid(row=1,column=6)
#list
Lb1 = Listbox(window,width=90)
Lb1.insert(1, "Suggestions")
Lb1.insert(2,"alert")
Lb1.grid(row=2,column=0,columnspan=5)



window.mainloop()
