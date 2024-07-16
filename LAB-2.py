#Arthimatic Operators
a=int(input())
b=int(input())

print("Sum",a+b)
print("Subtraction",a-b)
print("Product",a*b)
print("Division ",a/b)
print("Exponent",a**b)
print("Floor Division ",a//b)
print("Modulus",a%b)

#Relational Operators
a=int(input())
b=int(input())

print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#Assignment Operators
a=int(input())
b=int(input())

print(a=b)
print(a+=b)
print(a-=b)
print(a*=b)
print(a%=b)
print(a/=b)

#Farhenheit to Celsius
f=int(input())
c=5/9*(f-32)
print(c)

# FINDING VOWEL&CONSONANTE
a=input()
b=('a','e','i','o','u','A','E','I','O','U')
if a in b:
  print("VOWEL")
else:
    print("Consonant")  

#find Speed
a=int(input())
b=float(input())
speed=a/b
print("Speed",speed)


#largest of three numbers
a=int(input())
b=int(input())
c=int(input())	
if (a>b and a>c):
  print("A is BIG")
elif (b>a and b>c):
  print("B is BIG")
else:
  print("C is BIG")

a=int(input())
   if(a>=90):
     print("GRADE A")
   elif(a>=80):
       print("GRADE B")
   elif(a>=70):
       print("GRADE C")
   elif(a>=60):
       print("GRADE D")
   elif(a>=50):
       print("GRADE E")
   else:
       print("FAILED")
  













