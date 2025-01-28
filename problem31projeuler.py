lis=[1,2,5,10,20,50,100,200]
su=0

for a in range (1+1): # arithmos 2 eurwn
    for c in range (2+1): # arithmos 1 eurwn
        if 200*a + 100*c>200:
            break
        for d in range (4+1): # arithmos 50 leptwn
            if 200*a + 100*c + 50*d>200:
                break
            for e in range (10+1):# arithmos 20 leptwn
                if 200*a + 100*c + 50*d + 20*e>200:
                    break
                for f in range (20+1):# arithmos 10 leptwn
                    if 200*a + 100*c + 50*d + 20*e + 10*f>200:
                        break
                    for g in range (40+1):# arithmos 5 leptwn
                        if 200*a + 100*c + 50*d + 20*e + 10*f + 5*g>200:
                            break
                        for h in range (100+1):# arithmos 2 leptwn
                            if 200*a + 100*c + 50*d + 20*e + 10*f + 5*g + 2*h>200:
                                break
                            for i in range (200+1):# arithmos 1 leptwn
                                if 200*a + 100*c + 50*d + 20*e + 10*f + 5*g + 2*h + 1*i==200:
                                    su+=1
                                    break
print(su)   
