t1=(56,66,76,86,96,106)
t2=(6,16,26,36,46)
T=t2+t1
print(T)
print("Index of Element is ",T.index(106))
print("Length of Tuple is ",len(T))
t3=(5,6,6,6,8,3,7,9,2,9,7)
print("Count of Tuple is ",t3.count(6))
t4=tuple(zip(t1,t2))
print("Zip Method :",t4)
t5=t3
print("Copied Data INTo T5 :",t5)

