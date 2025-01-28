dic={1:"a", 2:"a", 3:"b", 4:"b", 5:"b", 9:"c", 10:"a", 20:"c"}
lis=list(dic.values())
lis.sort
final_dic={}
for i in lis:
    a=[]
    for j in dic:
        if dic[j]==i:
            a.append(j)
    final_dic[i]=a
print(final_dic)


    
    

    
