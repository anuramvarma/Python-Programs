class Parent:
	def Met1(self):
		print("Method in Main Parent class")
class Child1(Parent):
	def Met2(self):
		print("Method in child_1(Sub) Class")
class Child2(Parent):
	def Met3(self):
		print("Method in Child_2(Sub class) Class")
class Child3(Child1,Child2):
	def Met4(self):
		print("Method in Child_3(Sub_Sub class) Class")
print()
c3 = Child3()
c3.Met1()
c3.Met2()
c3.Met3()
c3.Met4()
