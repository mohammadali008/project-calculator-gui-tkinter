### I.N.O.G --- MohammadAli ---Project02

# --- Tkinter-Lib --- #
import tkinter as tk
from math import factorial
# --- Set up --- #
root = tk.Tk()
# root.configure(bg='#2E2E2E')
### - project01:calculator --- ###
equation = tk.StringVar()
above_label = tk.Label(
    text="Enter your  num ...",textvariable=equation,fg = 'Orange',padx = 15,pady = 10
)
above_label.grid(columnspan = 5)
# ---Define calculated var to check result of entry or equation
calculated = False

##--- DefineMain Functions ---##
def SetNumber(num):
    global calculated
    if calculated:
        equation.set('')
        calculated = False
    equation.set(equation.get()+num)


#/--- Define Plus-Function --- /#
def PlusNum(num):
    pass

#/--- Define Subtraction-Function ---/#
def SubNum(num):
    pass

#---
def sign(x):
    input = equation.get()
    if input[-1]=='*' or input[-1]=='/' or input[-1]=='+' or input[-1]=='-' :
        equation.set(input[:-1]+x)
    else:
        equation.set(input+x)

#---- Define Clear-One-Item-Function ---#
def ClearOneItem():
    equation.set(equation.get()[:-1])

#--- Define Factorial-Replacement-Function ---#
def ReplaceFactorial(expr):
    if '!' in expr:
        num_str = expr.split('!')[0] 
        if num_str.isdigit(): 
            num = int(num_str)
            factorial_result = factorial(num)
            expr = expr.replace(f'{num}!', str(factorial_result))
    return expr

#---Define Calculate -Function ---#
def Calculate():
    global calculated
    try:
        # Replace '^' with '**' for exponentiation
        expression = equation.get().replace("^", "**")
        expression = ReplaceFactorial(expression)
        # Safely evaluate the expression
        result = eval(expression)
        equation.set('')
        equation.set(result)
        calculated = True
    except ZeroDivisionError:
        equation.set('')
        equation.set("Cannot divide by 0")
    except Exception:
        equation.set('')
        equation.set("Error")










## --- buttons
btn1 = tk.Button(root,text = '1',width=5,height=2,
                 bg = "#3C3F41",
                 command = lambda :SetNumber('1')
                 )
btn1.grid(row=1,column=0)
btn2 = tk.Button(root,text = '2',width=5,height=2,
                 bg = "#3C3F41",
                 command=lambda :SetNumber('2')
                 )
btn2.grid(row=1,column=1)
btn3 = tk.Button(root,text = '3',width=5,height=2,
                 bg = "#3C3F41",
                 command=lambda : SetNumber('3')
                 )
btn3.grid(row=1,column=2)
btn4 = tk.Button(root,text = '4',width=5,height=2,
                 bg = "#3C3F41",
                 command=lambda : SetNumber('4')
                 )
btn4.grid(row=2,column=0)
btn5 = tk.Button(root,text = '5',width=5,height=2,
                 bg = "#3C3F41",
                 command=lambda : SetNumber('5')
                 )
btn5.grid(row=2,column=1)
btn6 = tk.Button(root,text = '6',width=5,height=2,
                 bg = "#3C3F41",
                 command=lambda :SetNumber('6')
                 )
btn6.grid(row=2,column=2)
btn7 = tk.Button(root,text = '7',width=5,height=2,
                 bg = "#3C3F41",
                 command=lambda : SetNumber('7')
                 )
btn7.grid(row=3,column=0)
btn8 = tk.Button(root,text = '8',width=5,height=2,
                 bg = "#3C3F41",
                 command=lambda : SetNumber('8')
                 )
btn8.grid(row=3,column=1)
btn9 = tk.Button(root,text = '9',width=5,height=2,
                 bg = "#3C3F41",
                 command=lambda : SetNumber('9')
                 )
btn9.grid(row=3,column=2)
btn0 = tk.Button(root,text = '0',width=5,height=2,
                 bg = "#3C3F41",
                 command=lambda : SetNumber('0' \
                 '')
                 )
btn0.grid(row=4,column=1)
##--- Operators-Button --- ##
btn_equal = tk.Button(root,text = '=',width=5,height=2,
                      bg = "#6B8E23",
                      command=lambda : Calculate()
                      )
btn_equal.grid(row=4,column=2)
btn_clear = tk.Button(root,text = 'clear',width=5,height=2,
                      bg = "#B22222",
                      command=lambda :equation.set('')
                      )
btn_clear.grid(row=4,column=0)
btn_plus = tk.Button(root,text = '+',width=5,height=2,
                     bg = "#4B5162",
                     command=lambda : sign('+')
                     )
btn_plus.grid(row=1,column=4)
btn_subtraction = tk.Button(root,text = '-',width=5,height=2,
                    bg = "#4B5162",
                    command=lambda : sign('-')
                    )
btn_subtraction.grid(row=2,column=4)
btn_multiplication = tk.Button(root,text = '*',width=5,height=2,
                         bg = "#4B5162",
                         command=lambda : sign('*')
                         )

btn_multiplication.grid(row=3,column=4)
btn_division = tk.Button(root,text = '/',width=5,height=2,
                    bg = "#4B5162",
                    command=lambda : sign('/')
                    )
btn_division.grid(row=4,column=4)

btn_clear_one_item = tk.Button(root,text = 'C',width=5,height=2,
                      bg = "#B22222",
                      command=lambda :ClearOneItem()
                      )
btn_clear_one_item.grid(row=1,column=5)

btn_exponentiation = tk.Button(root,text = '^',width=5,height=2,
                    bg = "#4B5162",
                    command=lambda : sign('^')
                    )
btn_exponentiation.grid(row=2,column=5)

btn_modulo = tk.Button(root,text = '%%',width=5,height=2,
                    bg = "#4B5162",
                    command=lambda : sign('%')
                    )
btn_modulo.grid(row=3,column=5)
btn_factorial = tk.Button(root,text = '!',width=5,height=2,
                    bg = "#4B5162",
                    command=lambda : sign('!')
                    )
btn_factorial.grid(row=4,column=5)

# --- Ending-Set up --- #
root.mainloop()
