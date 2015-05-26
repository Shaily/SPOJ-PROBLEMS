def gcd(x, y):
   if y ==0:return x
   else:return gcd(y,x%y)

for _ in input()*[0]:
    l=list(int(i) for i in raw_input().split())
    b=gcd(l[0],l[1])
    print str(l[1]/b)+" "+str(l[0]/b)
