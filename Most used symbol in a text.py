lex="Data science, on the other hand, is a more complex and iterative process that involves working with larger, more complex datasets that often require advanced computational and statistical methods to analyze. Data scientists often work with unstructured data such as text or images and use machine learning algorithms to build predictive models and make data-driven decisions. In addition to statistical analysis, data science often involves tasks such as data preprocessing, feature engineering, and model selection. For instance, a data scientist might develop a recommendation system for an e-commerce platform by analyzing user behavior patterns and using machine learning algorithms to predict user preferences"
lex=list(lex)
dic={}
for word in lex:
    dic[word]=0   #aftes tis 2 for tha borousa na tis grapsw me mia ws ekshs
for word in lex: #for word in lex: if word not in dic: dic[word]=1
    dic[word]+=1 #else: dic[word]+=1 (psounioooos)
lista=[]
for value in dic.values():#episis gia to max tha borousa,m=max(list(dic.values()))
    lista.append(value)
m=max(lista)
print(m)
for key in dic.keys():
    if dic[key]==m :
        print("to symvolo '"+key+"' exei emfanistei tis perissoteres fores (102)")
