#Membership Operator in Python

x = 'Hello world'
y = {1:'apple', 2: 'ball'}
output : True
print('H' in x)
print('hello' not in x)
print(1 in y)
print('apple' in y)

s = int(input('enter a index:' ))

print (s)
print('\n')
if s not in y: print('invalid')
else: print('valid') #yo pachi loop start garna paryo tyo sikna paryo 

print (y[s])
print('\n')
if s in y == y: print(y[s]) ## why this is giving value instead of 'True' or 'False'. 
else: print('No index found')