import math
def gcd(x, y):
	if y ==0:return x
	else:return gcd(y,x%y)

for _ in range(int(input())):
	no = int(input())
	limit = math.floor(no/2)
	if no == 1:
		print(1)
	else:
		while(gcd(limit,no)!=1):
			limit=limit-1
		print(limit)
