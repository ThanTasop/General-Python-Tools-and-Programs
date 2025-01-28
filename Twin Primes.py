import math
vrika=0
index=1
prwtoi=[2]
for x in range(3,1000, 2):
    
    for y in range (2,math.trunc(math.sqrt(x))+1):
        if x%y==0:
            vrika=1
            break
    if vrika==0:
        index+=1 #to index metraei to plithos twn prwtwn
        prwtoi+=[x]
        if prwtoi[-1]-prwtoi[-2]==2: #h diafora borei na peiraxtei
            print(prwtoi[-1],prwtoi[-2]) #didumoi prwtoi
    
    vrika=0
# print(prwtoi) akolouthia prwtwn
