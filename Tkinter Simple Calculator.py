from tkinter import *

class MyApp(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.title('Calculator')

		self.number_1 = 0
		self.number_2 = 0
		self.operator = '0'

		self.entry = Entry(self,width=20,font='Helvetica 20')
		self.entry.grid(row=0,column=0,columnspan=6)

		self.add_button = Button(self,text='+',font='Arial 15',width=3,bg='#89cff0',fg='#ffffff',command=lambda: self.operator_button('+')).grid(row=1,column=0)
		self.minus_button = Button(self,text='-',font='Arial 15',width=3,bg='#89cff0',fg='#ffffff',command=lambda: self.operator_button('-')).grid(row=1,column=1)
		self.multiply_button = Button(self,text='x',font='Arial 15',width=3,bg='#89cff0',fg='#ffffff',command=lambda: self.operator_button('*')).grid(row=1,column=2)
		self.divide_button = Button(self,text='÷',font='Arial 15',width=3,bg='#89cff0',fg='#ffffff',command=lambda: self.operator_button('/')).grid(row=1,column=3)

		self.delete_button = Button(self,text='CE',font='Arial 15',width=3,bg='#f4c2c2',fg='#ffffff',command=self.delete).grid(row=1,column=4)
		self.equal_button = Button(self,text='=',font='Arial 15',width=3,bg='#C4F0E5',fg='#ffffff', command=self.equal).grid(row=1,column=5)

		self.b1 = Button(self,text='1',font='Arial 30',width=3,command=lambda: self.click('1')).grid(row=2,column=0,columnspan=2)
		self.b2 = Button(self,text='2',font='Arial 30',width=3,command=lambda: self.click('2')).grid(row=2,column=2,columnspan=2)
		self.b3 = Button(self,text='3',font='Arial 30',width=3,command=lambda: self.click('3')).grid(row=2,column=4,columnspan=2)

		self.b4 = Button(self,text='4',font='Arial 30',width=3,command=lambda: self.click('4')).grid(row=3,column=0,columnspan=2)
		self.b5 = Button(self,text='5',font='Arial 30',width=3,command=lambda: self.click('5')).grid(row=3,column=2,columnspan=2)
		self.b6 = Button(self,text='6',font='Arial 30',width=3,command=lambda: self.click('6')).grid(row=3,column=4,columnspan=2)

		self.b7 = Button(self,text='7',font='Arial 30',width=3,command=lambda: self.click('7')).grid(row=4,column=0,columnspan=2)
		self.b8 = Button(self,text='8',font='Arial 30',width=3,command=lambda: self.click('8')).grid(row=4,column=2,columnspan=2)
		self.b9 = Button(self,text='9',font='Arial 30',width=3,command=lambda: self.click('9')).grid(row=4,column=4,columnspan=2)

		self.b0 = Button(self,text='0',font='Arial 30',width=3,command=lambda: self.click('0')).grid(row=5,column=2,columnspan=2)


	def operator_button(self, button):
		self.number_1 = self.entry.get()
		self.entry.delete(0, END)
		self.operator = button

	def delete(self):
		self.entry.delete(0, END)

	def equal(self):
		self.number_2 = self.entry.get()
		self.entry.delete(0, END)
		if self.operator == '+':
			final_number = int(self.number_1) + int(self.number_2)
		if self.operator == '-':
			final_number = int(self.number_1) - int(self.number_2)
		if self.operator == '*':
			final_number = int(self.number_1) * int(self.number_2)
		if self.operator == '/':
			final_number = int(self.number_1) / int(self.number_2)
		self.entry.insert(0, final_number)

	def click(self,value):
		self.entry.insert(END, value)


if __name__ == "__main__":
	app = MyApp()
	app.mainloop()