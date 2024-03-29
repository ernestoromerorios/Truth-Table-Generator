from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import numpy as np

def tabla(*args):
	global lab,main_frame
	lab.destroy()
	main_frame.destroy()
	variables = []
	func = inp.get()
	if len(func) == 0:
		
		messagebox.showerror(message="Empty Text Field!\nPlease enter at least one variable.",title="Error")

	else:

		for i in func:
			if (i.upper()).isalpha() and (not(i.upper() in variables)):
				variables.append(i.upper()) 

		if len(variables) > 10:

			messagebox.showwarning(message="Too many variables!\nPlease enter only up to ten variables.",title="Warning")
		
		else:

			variables = sorted(variables) 

			dicc = {
			'True':'1',
			'False':'0',
			True:'1',
			False:'0',
			'1':'1',
			'0':'0',
			}

			main_frame = Frame(root) #Set a new Frame to be able to use a lot of data and go down with the bar to all of them.
			main_frame.pack(fill=BOTH, expand=1)

			# Create a Canva
			my_canvas = Canvas(main_frame)
			my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

			# Add bar to canva
			my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
			my_scrollbar.pack(side=RIGHT, fill=Y)

			# Canva configuration
			my_canvas.configure(yscrollcommand=my_scrollbar.set,bg='#CCC')
			my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

			# Create another Frame inside canva
			second_frame = Frame(my_canvas,bg='#CCC')

			# Add the new Frame to the canva window
			my_canvas.create_window((0,0), window=second_frame, anchor="nw")
			
			text = '\t'

			lab = Label(second_frame,text=f"Función:   {transformacion(func).upper()}",bg='#CCC',fg='#000',font=('Helvetica', 10, 'bold'))
			lab.pack(pady=5)

			for i in range (len(variables)):
				text += variables[i] + '\t'
			
			text += "Resultado"
			
			lab = Label(second_frame,text=f"{text}",bg='#CCC',fg='#000',font=('Helvetica', 10, 'bold'))
			lab.pack(pady=5)

			for j in range (2**len(variables)):
				
				aux = str(bin(j))
				text = ''
				binary = ''
				b = False
				for i in aux:
								
					if b:
						text += str(i) + '\t'
						binary += str(i)

					if i == 'b':
						b = True

				aux = str(aux)
				aux = ''

				while (len(aux)+(len(text)) != (len(variables)*2)):
					
					aux += '0' + '\t'
					binary = '0' + binary

				res = ''
				num = 0
				text = aux + text
				expr = func

				for i in range(len(expr)):

					if expr[i].isalpha():
						num = variables.index(expr[i].upper())
						res += binary[num]
					else:
						res += expr[i]
					if num == len(variables):
						num = 0

				num = 0
				expr = transformacion(res)
				#print(res)
				#print(func) a+b
				#print(res) 0+0

				try:
					#print(res)
					res = str(dicc[eval(expr)])
					text += res

					lab = Label(second_frame,text=f"{text}",bg='#CCC',fg='#000',font=('Helvetica', 10, 'bold'))
					lab.pack(pady=5)
				
				except:
				
					messagebox.showerror(message="Error in writing the function!\nPlease go to the help section for more information.",title="Syntax Error")
					break

def help():
	
	top = Toplevel() 
	top.configure(background='#333333') 
	top.title('Help') 
	top.geometry('800x500') 
	btn2.config(state='disable') 
	
	l = Label(top,text="Truth Table Generator",fg='#FFF',bg='#333333',font=('Garamond bold', 15, 'bold italic'))
	l.place(x=250,y=30)

	l = Label(top,text="The program can calculate a truth table of up to ten variables.",fg='#FFF',bg='#333333',font=('Garamond bold', 11, 'bold '))
	l.place(x=50,y=100)

	l = Label(top,text="You must remember that an extra parenthesis or an operator without a variable can generate errors.",fg='#FFF',bg='#333333',font=('Garamond bold', 11, 'bold '))
	l.place(x=50,y=125)

	l = Label(top,text="Below are some examples of how Boolean functions are entered:",fg='#FFF',bg='#333333',font=('Garamond bold', 11, 'bold '))
	l.place(x=50,y=150)

	l = Label(top,text="AND Operator   →   . or also *  ",fg='#FFF',bg='#333333',font=('Garamond bold', 12, 'bold'))
	l.place(x=250,y=220)

	l = Label(top,text="OR Operator   →   + ",fg='#FFF',bg='#333333',font=('Garamond bold', 12, 'bold'))
	l.place(x=250,y=270)

	l = Label(top,text="NOT Operator   →   ~ or also '  ",fg='#FFF',bg='#333333',font=('Garamond bold', 12, 'bold'))
	l.place(x=250,y=320)

	l = Label(top,text="XOR Operator   →   ^   ",fg='#FFF',bg='#333333',font=('Garamond bold', 12, 'bold'))
	l.place(x=250,y=370)

	l = Label(top,text="Example: (~a+b)*(a+b+c) Or also → ('a+b).(a+b+c) ",fg='#FFF',bg='#333333',font=('Garamond bold', 14, 'bold'))
	l.place(x=250,y=420)

	def on_close():  
		top.destroy() 
		btn2.config(state='normal')  

	top.protocol("WM_DELETE_WINDOW", on_close)				


def transformacion(funcion):
	aux = ''
	for i in funcion:
		if i.isnumeric():
			aux += i
		elif i == "*" or i == ".":
			aux += " and "
		elif i == "+":
			aux += " or "
		elif i == "~" or i == "'":
			aux += " not "
		else:
			aux += i

	return aux
				

root = Tk()
root.title('\tTruth Table Generator')
root.configure(background='#CCC') 
root.geometry('550x550')

lab = Label(root)
main_frame = Frame(root)

inp = StringVar()
inpt = Entry(textvar=inp,width=35)
inpt.pack(pady=5)

btn = Button(root,text='Send',fg='#000',bg='#FF9D00',font=('Helvetica', 10, 'bold'),command=tabla)
btn.pack(pady=5)

btn2 = Button(root,text='Help',fg='#000',bg='#39CC68',font=('Helvetica', 10, 'bold'),command=help)
btn2.pack(pady=5)

l = Label(root,text="Ernesto Romero Rios ®",fg='#000',bg='#DDD',font=('Helvetica', 10, 'bold'))
l.place(x=5,y=5)

inpt.focus()
root.bind("<Return>",tabla)

root.mainloop()

