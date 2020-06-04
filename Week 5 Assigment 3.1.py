hrs = input("Enter Hours:")
h = float(hrs)
Pay = input("enter rate:")
p = float(Pay)

if h>40:
    y=p*1.5
    t=h-40
    x=40*p+t*y
    print(x)
else:
    x=h*p
    print(x)
