class AI:

	filename = "machine_learning.py"

	def __init__(self):

		self.__create_file()

	def __create_file(self):

		with open(self.filename, 'w') as file:
			pass

	def __println(self, line=""):

		with open(self.filename, 'a') as file:
			file.write(line + "\n")


if __name__ == '__main__':

	ai = AI()
