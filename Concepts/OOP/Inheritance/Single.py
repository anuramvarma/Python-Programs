class Parent :
	def Met1(self):
		print("Method in Parent class")
class Child(Parent):
	def Met2(self):
		print("Method in Child Class")
c = Child()
c.Met1()
c.Met2()

