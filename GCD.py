import math

def GCD(a,b):
    if(a<b):
        a,b = b,a
    n,d = a,b
    r = n - (d * math.floor(n/d))
    while(r != 0):
        n,d = d,r
        r = n - (d * math.floor(n/d))
    return d



    