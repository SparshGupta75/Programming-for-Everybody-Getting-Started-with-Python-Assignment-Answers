def computepay(h,r):
    w=r*1.5
    t=h-40
    if(h>40):
        x=40*r+t*w
        return x
    else:
        x=h*r
        return x

    

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
p = computepay(h,r)
print("Pay",p)
