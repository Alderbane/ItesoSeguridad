import sys, math

def XGCD(a,b):
    if(a<b):
        a,b = b,a
    v = [a,b]
    x = [1,0]
    y = [0,1]
    i = 1
    while v[i] != 0:
        i = (i+1)%2
        q = math.floor(v[i]/ v[(i+1)%2])
        v[i] = v[i] - (q * v[(i+1)%2])
        x[i] = x[i] - (q * x[(i+1)%2])
        y[i] = y[i] - (q * y[(i+1)%2])
    i = (i+1)%2
    return x[i], y[i], v[i]

if __name__ == '__main__':
    a,b = int(sys.argv[1]), int(sys.argv[2])
    x, y, v = XGCD(a,b)
    print(f"{x}, {y}, MCD({a},{b})={v}")