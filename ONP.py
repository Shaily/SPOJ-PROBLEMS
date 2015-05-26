left = 0
right = 1

ops = {'+':(0,left),
       '-':(9,left),
       '*':(5,left),
       '/':(5,left),
       '%':(5,left),
       '^':(10,right)}

def checkAssociativity(token,assoc):
    if token not in ops.keys():
       raise ValueError('Invalid Token!')
    return ops[token][1] == assoc

def compare(tok1,tok2):
    if (tok1 not in ops.keys()) or (tok2 not in ops.keys()) :    
        raise ValueError('Invalid Tokens!')
    return ops[tok1][0] - ops[tok2][0]

t = int(raw_input())


for temp in range(t):
	str = raw_input()
	inp = list(str)
        output = []
	stack = []
	for token in inp:
	    if token in ops.keys():
	       while len(stack) !=0 and (stack[-1] in ops.keys()) :
		     if (checkAssociativity(token,left) and (compare(token,stack[-1]) <=0)) or (checkAssociativity(token,right) and (compare(token,stack[-1]) <0)):
			    output.append(stack.pop())
			    continue      
		     break
	       stack.append(token)
	    elif token == '(':
	       stack.append(token)
	    elif token == ')':
	       while len(stack) != 0 and stack[-1] != '(':
		     output.append(stack.pop())
	       stack.pop()
	    else:
	       output.append(token)
	   
	while len(stack) !=0:
	      output.append(stack.pop())

	print ''.join(output)
