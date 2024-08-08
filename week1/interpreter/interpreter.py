
equation=input('Equation :  ')
l=equation.split(' ')
x,i,z=float(l[0]),l[1],float(l[2])
if i=='+' : print(x+z)
elif i=='*' : print(x*z)
elif i=='-' : print(x-z)
elif i=='/' : print(x/z)


