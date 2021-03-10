#Value the viariables as the first and second terms of the sequence
x = 1
y = 1
#Repeat
for i in range(3,14):
#Value the adjacent three items in the sequence  
    z = x + y
    x = y
    y = z
    print z
