def minWindow(s,t):
    taf = set(t)
    for i in range(len(t), len(s) + 1):
        step = 0
        while step + i < len(s) + 1:
            slice = s[step:step + i]
            diff=0
            for letter in taf:
                x=t.count(letter)
                y=slice.count(letter)
                if x-y>0:
                    diff+=x-y
            if  diff==0:
                return slice
            else:
                step+=diff
    return "."
print(minWindow("ADOBECODEBANC","ABC"))