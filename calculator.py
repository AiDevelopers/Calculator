# Simple calculator:
from tkinter import *

cal=Tk()
cal.title('Calculator')
text_Input=StringVar()
operator=''

def btnClick(numbers):
        global operator
        operator= operator + str(numbers)
        text_Input.set(operator)

def btnClear():
        global operator
        operator=''
        text_Input.set('')

def btnEquals():
        global operator
        sumup = str(eval(operator))
        text_Input.set(sumup)
        operator=''

text_display=Entry(cal,font=('arial',20,'bold'),textvariable=text_Input,
                           bd=30,insertwidth=3,bg='cyan',justify='right').grid(columnspan=5)

##########################################################################################################

button7=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='7',
                       command =lambda: btnClick(7))
button7.grid(row=1,column=0)

button8=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='8',
                       command =lambda: btnClick(8))
button8.grid(row=1,column=1)

button9=Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='9',
                       command =lambda: btnClick(9))
button9.grid(row=1,column=2)

buttondev = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='/',
                           command=lambda: btnClick('/'))
buttondev.grid(row=1, column=3)

buttonPow = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='ln',
                           command=lambda: btnClick('ln'))
buttonPow.grid(row=1, column=4)

##########################################################################################################

button4 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='4',
                         command=lambda: btnClick(4))
button4.grid(row=2, column=0)

button5 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='5',
                         command=lambda: btnClick(8))
button5.grid(row=2, column=1)

button6 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='6',
                         command=lambda: btnClick(6))
button6.grid(row=2, column=2)

buttonMul = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='*',
                           command=lambda: btnClick('*'))
buttonMul.grid(row=2, column=3)

buttonPercentage = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='%',
                                  command=lambda: btnClick('%'))
buttonPercentage.grid(row=2, column=4)

###########################################################################################################

button1 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='1',
                         command=lambda: btnClick(1))
button1.grid(row=3, column=0)

button2 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='2',
                         command=lambda: btnClick(2))
button2.grid(row=3, column=1)

button3 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='3',
                         command=lambda: btnClick(3))
button3.grid(row=3, column=2)

buttonSub = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='-',
                           command=lambda: btnClick('-'))
buttonSub.grid(row=3, column=3)

buttonClr = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='C',
                           command= btnClear)
buttonClr.grid(row=3, column=4)

###########################################################################################################

button0 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='0',
                         command=lambda: btnClick(0))
button0.grid(row=4, column=0)

buttonAdd = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='.',
                           command=lambda: btnClick('.'))
buttonAdd.grid(row=4, column=1)

buttonAdd = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='+',
                           command=lambda: btnClick('+'))
buttonAdd.grid(row=4, column=2)

buttonEqu = Button(cal, padx=16, pady=16, bd=8, fg='blue', font=('arial', 20, 'bold'), text='=',
                           command= btnEquals)
buttonEqu.grid(row=4, column=3, columnspan=2, sticky='NWNESWSE')


cal.mainloop()