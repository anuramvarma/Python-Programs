s = input("enter a string")
rev =""
print(s)
for i in s:
	rev = i+rev
if(s== rev):
	print(f"{s} is a palindrome")
else:
	print(f"{s} is not a a palindrome")
