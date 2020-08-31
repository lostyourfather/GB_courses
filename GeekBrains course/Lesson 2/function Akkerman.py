def akker(m,n):
    if m==0:
        return n+1
    elif n==0 and m>0:
        return akker(m-1,1)
    return akker(m-1,akker(m,n-1))

print(akker(3,5))