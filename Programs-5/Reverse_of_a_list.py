l=[]
n=int(input("Enter no.of Elements : "))
for i in range(n):
	ele=int(input("Enter elements :"))
	l.append(ele)
print("The list is ",l)
l.reverse()
print("The reversed list is :",l)
