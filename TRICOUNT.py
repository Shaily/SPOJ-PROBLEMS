t = int(input())

for e in range(t):
    i = long(input())
    if i%2 == 0:
       count = (i*(i+2)*(2*i+1))/8
    else:
       count = ((i*(i+2)*(2*i+1))-1)/8
    
    print(count)
