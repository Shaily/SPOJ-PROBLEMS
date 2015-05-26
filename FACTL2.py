def fact(x):
	if x == 0 or x == 1:
	   return 1
	else:
	   return x * fact(x-1)

t = int(input())

for i in range(t):
    no = int(input())
    print(fact(no))
