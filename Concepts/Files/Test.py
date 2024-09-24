f=open('test.txt','w')
f.write("Welcome to Files")

f=open('test.txt','a')
f.write("Concept")

f=open('test.txt','r')
print(f.read())

print("Initial Pos : ",f.tell())
f.seek(10)

print("Pos after seek : ",f.tell())

print(f.read(5))
print("POS after READ : ",f.tell())


f.close()
