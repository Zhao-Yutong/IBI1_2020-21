a = 110302
b = 190784
c = 100321
d = abs(a-c)
e = abs(a-b)
print "d =",d
print "e =",e
if d > e:
   print "d is greater"
else:
   print "e is greater"
X = True
Y = False
Z = (X and not Y)or(Y and not X)
print Z
X = True
Y = False
W = X!=Y
print W


