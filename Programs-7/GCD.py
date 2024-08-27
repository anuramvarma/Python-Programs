def gcd(a,b):
	while b:
		a, b=b,a%b
	return a
num1=89
num2=85
print(f"The GCD of Given numbers is {gcd(num1,num2)}")
