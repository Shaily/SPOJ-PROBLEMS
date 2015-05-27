def gcd(x, y):
   if y ==0:return x
   else:return gcd(y,x%y)

t = int(input())
for k in range(t):
    l=list(int(i) for i in input().split())
    b=gcd(abs(l[0]),abs(l[1]))
    if l[2] % b == 0:
       print("Case "+str(k+1)+": Yes")
    else:
       print("Case "+str(k+1)+": No")
