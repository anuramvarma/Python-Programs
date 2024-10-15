class Parent1:
	def Met1(self):
		print("Method in Parent_1 class")
class Parent2:
	def Met2(self):
		print("Method in Parent_2 Class")
class Child(Parent1,Parent2):
	def Met3(self):
		print("Method in Child Class")
c = Child()
c.Met1()
c.Met2()	
c.Met3()			
