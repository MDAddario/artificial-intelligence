import numpy as np


class AI:

	filename = "machine_learning.py"
	indent = " "

	def __init__(self, size=3):

		# Save attribute
		self.size = size

		# Create file
		self.__create_file()

		# Setup parameters
		self.__setup_parameters()

		# Do AI
		self.__if_else(0)

		# Terminate
		self.__terminate()

	def __create_file(self):

		with open(self.filename, 'w') as file:
			pass

	def __println(self, line=""):

		with open(self.filename, 'a') as file:
			file.write(line + "\n")

	def __setup_parameters(self):

		conditions = "conditions = ["

		for i in range(self.size):
			conditions += f"{np.random.rand() < 0.5}"

			if i == self.size - 1:
				conditions += "]"
			else:
				conditions += ", "

		parameters = "parameters = ["

		for i in range(self.size):
			parameters += f"{np.random.rand():.2f}"

			if i == self.size - 1:
				parameters += "]"
			else:
				parameters += ", "

		self.__println("# Setup the model parameters")
		self.__println(conditions)
		self.__println(parameters)
		self.__println(f"epsilon = 0.01")
		self.__println()
		self.__println("# Training the model")

	def __if_else(self, depth):

		# Max depth reached:
		if depth == self.size:
			return

		small_buffer = self.indent * depth
		big_buffer = self.indent * (depth + 1)

		self.__println(f"{small_buffer}if conditions[{depth}]:")
		self.__println(f"{big_buffer}parameters[{depth}] += epsilon")
		self.__if_else(depth + 1)
		self.__println(f"{small_buffer}else:")
		self.__println(f"{big_buffer}parameters[{depth}] -= epsilon")

	def __terminate(self):

		self.__println()
		self.__println("# Post-training evaluation")
		self.__println("print(parameters)")


if __name__ == '__main__':

	ai = AI(size=100)
