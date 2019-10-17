
class menu():
	""" This is the prefect menu system. I built this module to
	simplfy coding what you need. I made it as easy as possilble to use.
	Just follow this docstring for more infomation
	
	* To setup the program use Menu.menu("Function()","Function2()", "Function3()")
	follow the syntax and add as many functions as you want. This will create
	the setup for you and add the functions for the user. Each function will displayed
	by the user as your function without the "()".

	* To create the menu use "exec(Menu.main_menu(Message))" this will start the menu system
	so make sure to place it at the last line of your script. Replace the word "Message" with
	what you would like to be displayed before it promets for an input. 

	Enjoy!
	"""
	def __init__(self, *menu):
		User_Functions =[]
		User_Options = []
		for x in menu:
			User_Functions.append(x)
		for choice in User_Functions:
			User_Options.append(choice.replace("()",""))
		self.Options = [User_Options] + [User_Functions]
		print(self.Options)

	def main_menu(self,Input,Info = ""):
		print(Info)
		for num,char in enumerate(self.Options[0]):
			if char == Input:
				return self.Options[1][num]

			elif num == len(self.Options[0]):
				print("Try Again")