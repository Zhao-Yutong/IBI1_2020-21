#Define the variable n as the origin infected individuals
n = 84
#Assume the given r rate is 1.2
r = 1.2
#Repeat for 5 times as we need to find out the number of infected individuals after 5 rounds of infection
for i in  range(1,6):
#Every new round is the old round multiplies the r rate
    n = n *r
    print "The number of infected individuals is", n
