class Const:
	def __init__(self):
		print("Hello CSE!")
	def __del__(self):
		print("Object is deleted")
c = Const()
del c
