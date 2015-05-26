def fun(a, b):
    if (b==0) :
	return a
    else:
	return fun(b,a%b)


t = int(raw_input())

for i in range(t):
    str = raw_input()
    x,y = str.split(' ')
    x = long(x)
    y = long(y)
    print(fun(x,y))
