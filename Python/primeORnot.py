number = int(input())

flag=False
for i in range(2, number//2+1):
	if(number%i==0):
		flag=True
		break

if number == 1:
	print("Neither prime nor composite")
elif flag:
	print("Number is not prime")
else:
	print("Number is prime")
