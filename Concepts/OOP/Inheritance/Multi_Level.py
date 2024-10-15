class Parent :
	def Met1(self):
		print("Method in Parent class")
class Child1(Parent):
	def Met2(self):
		print("Method in Child_1 Class")
class Child2(Child1):
	def Met3(self):
		print("Method in Child_2 Class")
c = Child2()
c.Met1()
c.Met2()	
c.Met3()			
