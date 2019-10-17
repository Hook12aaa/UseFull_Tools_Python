class file_control():
	""" File control is the latest and greatest from yours turly. It helps when
	you need to read and write into a text file. To create one simple do " ___.file_control(Textfile_of_your_choice)"
	The different functions are:

		* "import_to_array" = inports all the words in an array to use this  use this format  "Array =import_to_array()". 
		This will import an array to the variable "Array"

		* "exporting_array(List)" = is an exporting function for an array itself. to do this call  "exporting_array(List)"
		and replace the list with the array of your choice

		* "import_iteams(Variable_to_add)" =  exports all the varibles entered into the brackets no matter how man. This
		can input as many as you want. Example is "(Value1,Value2,Value3,Value4)"
	"""
	def __init__(self,ImportFileName):
		self.FileName = ImportFileName
		

	def import_to_array(self):
		List = []
		with open(self.FileName ,"r") as File:
			for line in File:
				List.append(line.replace("\n",""))
		File.close()
		return List

	def exporting_array(self,List):
		with open(self.FileName,"w") as File:
			for Iteam in List:
				File.write("{0}{1}".format(Iteam,"\n"))

	def import_iteams(self,*Iteams):
		with open(self.FileName,"a") as File:
			for i in Iteams:
				File.write("{0}{1}".format(i,"\n"))
