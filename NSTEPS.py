t = int(raw_input())

for i in range(t):
    str = raw_input()
    x,y = str.split(' ')
    x = int(x)
    y = int(y)
    if( x > 10000 or y > 10000 or x < 0 or y < 0):
	print("No Number")
    elif((x+y) % 2 != 0):
      print("No Number")
    elif (x==0 and y==0):
      print(0)
    elif(x-y ==2 or x-y ==0):
      if(x%2 !=0):
	print(x+y-1)
      else:
        print(x+y)
    else:
        print("No Number")
 
