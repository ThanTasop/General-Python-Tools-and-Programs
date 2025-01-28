def polymul(a,b):
    
    g=[]
    for i in range (len(a)+len(b)-1):
        g.append(0)
    for i in range (len(a)):
        for j in range (len(b)):
            g[i+j]+=a[i]*b[j]
    print(g)



polymul([1,2,3,4],[5,5,5,5,5])
