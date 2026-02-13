def maxi(a,b,c):
    
    if a>b and a>c:
        print("a=")
        return a
    
    elif b>a and b>c:
        return b

    else:
        return c


ret=maxi(80,40,30)
print(ret)


