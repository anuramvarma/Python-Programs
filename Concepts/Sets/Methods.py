s1={3,4,56,6,20,33,4,0,2,11}
s2={3,5,6,1}
s2.add(2)
print("Adding Element :",s2)
v={3,6,9,4,5,9}
v.clear()
print("Set cleared ",v)
s1.discard(56)
print("Discard Elements",s1)
s2.remove(1)
print("Removing Element :",s2)
s1.pop()
print("Poping elements : ",s1)
s3=s2
print("Copying to set-3",s3)
n={3,2,6,5,3,7}
print(n)
print("Difference ",s1.difference(s2))
print("Symmetric Difference ",s1.symmetric_difference(s2))
print("Intersection :",s1.intersection(s2))
print("Union ",s1.union(s2))
