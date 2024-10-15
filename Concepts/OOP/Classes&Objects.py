class Student:
	branch=" CSE "
	def read_student(self,rno,n):
		self.roll_no=rno
		self.name=n
	def display(self):
		print(self.roll_no)
		print(self.name)
s = Student()
s.read_student(9,"Anuram")
s.display()
