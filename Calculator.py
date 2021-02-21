#by SAHAR KHORSHID
from tkinter import *
import tkinter.messagebox

root = Tk()
root.title('CalCulator')
root.geometry('400x400')
root.resizable(width=FALSE , height=False)
root.configure(bg='#00A86B')

# ========================== variables ==========================================
text_input = StringVar()
operator = ""

#============= Frames ============================================================
farme_first = Frame(root, width=400, height=100, bg='#00A86B')
farme_first.pack(side=TOP)

farme_second = Frame(root, width=100, height=500, bg='#003151')
farme_second.pack(side=LEFT)

farme_third = Frame(root, width=100, height=500)
farme_third.pack(side=LEFT)

farme_forth = Frame(root, width=100, height=500)
farme_forth.pack(side=LEFT)

farme_fifth = Frame(root, width=100, height=500)
farme_fifth.pack(side=LEFT)

# ========================== Functions ============================================

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def errorMsg(ms):
    if ms == 'error':
        tkinter.messagebox.showerror('Error', 'something went wrong')
    elif ms == 'division zero error':
        tkinter.messagebox.showerror('Division Error', 'Can Not Divide By 0')

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator=""

def btnClearDisplay():
    global operator
    operator =""
    text_input.set("")

# ========================== Buttons =================================================================================

btn_plus = Button(farme_second, text="+", width=6,height=3,command=lambda: btnClick('+'),font=('bold',16), bd=3)
btn_plus.pack(side=TOP, padx=10, pady=8)

btn_minus = Button(farme_second, text="-", width=6,height=2,command=lambda:  btnClick('-'),font=('bold',16), bd=3)
btn_minus.pack(side=TOP, padx=10, pady=10)

btn_mul = Button(farme_second, text="*", width=6,height=2,command=lambda:  btnClick('*'),font=('bold',16), bd=3)
btn_mul.pack(side=TOP, padx=10, pady=9)

btn_div = Button(farme_second, text="/", width=6 ,height=4, command=lambda:  btnClick('/'),font=('bold',15), bd=3)
btn_div.pack(side=TOP, padx=10, pady=10)

# ========================== Buttons_Numbers ===========================================================================

btn_1 = Button(farme_third, text="1", width=13, height=5 ,command=lambda:btnClick(1),bg='#95C8D8', bd=3)
btn_1.pack(side=TOP)

btn_4 = Button(farme_third, text="4", width=13 , height=5,command=lambda:btnClick(4),bg='#95C8D8', bd=3)
btn_4.pack(side=TOP)

btn_7 = Button(farme_third, text="7", width=13, height=5 ,command=lambda:btnClick(7),bg='#95C8D8', bd=3)
btn_7.pack(side=TOP)

btn_2 = Button(farme_forth, text="2", width=13, height=5,command=lambda:btnClick(2),bg='#95C8D8', bd=3)
btn_2.pack(side=TOP)

btn_5 = Button(farme_forth, text="5", width=13, height=5,command=lambda:btnClick(5),bg='#95C8D8', bd=3)
btn_5.pack(side=TOP)

btn_8 = Button(farme_forth, text="8", width=13, height=5 ,command=lambda:btnClick(8),bg='#95C8D8', bd=3)
btn_8.pack(side=TOP)

btn_3 = Button(farme_fifth, text="3", width=13, height=5,command=lambda:btnClick(3),bg='#95C8D8', bd=3)
btn_3.pack(side=TOP)

btn_6 = Button(farme_fifth, text="6", width=13, height=5,command=lambda:btnClick(6),bg='#95C8D8', bd=3)
btn_6.pack(side=TOP)

btn_9 = Button(farme_fifth, text="9", width=13, height=5,command=lambda:btnClick(9),bg='#95C8D8', bd=3)
btn_9.pack(side=TOP)

btn_0 = Button(farme_forth, text="0", width=13, height=5,command=lambda:btnClick(0),bg='#95C8D8', bd=3)
btn_0.pack(side=TOP)

btn_cls = Button(farme_fifth, text="C", width=13, height=5,command=btnClearDisplay,bg='#95C8D8', bd=3)
btn_cls.pack(side=TOP)

btn_Equal = Button(farme_third, text="=", width=13, height=5,command=btnEqualsInput,bg='#95C8D8', bd=3)
btn_Equal.pack(side=TOP)


# ========================== Entries ========================================================================

first_num = Entry(farme_first,textvariable=text_input,font=('arial', 30, 'bold'))
first_num.pack(side=TOP,pady=10, padx=40)

root.mainloop()