class Parent:
	def Met1(self):
		print("Method in Parent class")
class Child1(Parent):
	def Met2(self):
		print("Method in child_1 Class")
class Child2(Parent):
	def Met3(self):
		print("Method in Child_2 Class")
class Child3(Parent):
	def Met4(self):
		print("Method in Child_3 Class")
c1 = Child1()
c1.Met1()
c1.Met2()
print()
c2 = Child2()
c2.Met3()
c2.Met1()
print()
c3 = Child3()
c3.Met4()
c3.Met1()
