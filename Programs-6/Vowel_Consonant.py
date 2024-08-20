s=input("Enter a String : ")
v,c=0,0
for i in s:
	if(i in "aeiouAEIOU"):
		v+=1
	else:
		c+=1
print("Vowel : ",v)
print("Consonant ",c)
