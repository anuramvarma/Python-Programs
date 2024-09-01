l=[]
n=int(input("No of elements : "))
for i in range(n):
    e=int(input("Enter elements in list : "))
    l.append(e)
print("Enter an element to remove : ")
m=int(input())
l.remove(m)
print(l)
