import time
sta = time.time()
from collections import Counter
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
import collections
ntext = [line.strip() for line in open("wsj00-18.tag", 'r')]
sentences =[]
sentence = []
for line in ntext:
	l = line.split('\t')
	if(len(line)>0):
		sentence.append(l[0].lower())
	if(len(line) == 0):
		sentences.append(sentence)
		sentence = []
#text = ['a','cat','is','a','cat','no','matter','what','.']
t,newText,alphabet,lcount,rcount,lecount = [],[],set(),collections.defaultdict(int),collections.defaultdict(int),collections.defaultdict(int)
words = []
listofwords = []
for sentence in sentences:
	for word in sentence:
		listofwords.append(word)
counts = Counter(listofwords)
requiredwords =dict(counts.most_common(500))
frequentwords= requiredwords.keys()
#for requireds in requiredwords:
#	frequentwords.append(requireds[0])
setofwords = set(listofwords)
if(' ' in listofwords):
    print("yes")
wor =  " ".join(str(x) for x in listofwords)
#newwords = re.findall("\w+|\S+", wor)
#print(Counter(zip(newwords,newwords[1:])))
#print(len(setofwords))
#frequentwords = ['cat','.']
listofarrays = []
"""for text in sentences:
	    for i in range(len(text)):
	    	if(i == 0 & i < len(text)-1):
			lecount[text[i]+text[i+1]] += 1
		elif(i == len(text)-1):
			lecount[text[i-1]+text[i]] +=1
		elif(i>0 & i < len(text)-1):
			lecount[text[i-1]+text[i]] +=1"""
for text in sentences:
	for i in range(len(text)):
		if text[i] in requiredwords:
			if(i == 0 & i < len(text)-1):
				lecount[text[i]+text[i+1]] += 1
			elif(i == len(text)-1):
				lecount[text[i-1]+text[i]] +=1
			elif(i>0 & i < len(text)-1):
				lecount[text[i-1]+text[i]] +=1
				lecount[text[i]+text[i+1]] +=1
allkeys = lecount.keys()
for currentword in requiredwords.keys():
    for wo in setofwords:
    	rcount[wo] = lecount.get((currentword+wo),0)
	lcount[wo] = lecount.get((wo+currentword),0)
    left = np.array((list(lcount.values())))
    right = np.array((list(rcount.values())))
    finalar = np.concatenate((left, right), axis=0)    
    vec = finalar
    #normalarray = normalize(vec, axis=1, norm='l1')
    #print(counter)
    #counter += 1            
    listofarrays.append(finalar)
X = normalize(np.array(listofarrays),axis=1, norm='l1')
sto = time.time()
print(sto-sta)
sta = time.time()
kmeans = KMeans(n_clusters=25, random_state=0).fit(X)            
sto = time.time()
print(sto-sta)
"""print(kmeans.labels_)
for currentword in frequentwords:
    for s in setofwords:
	    lcount[s] = 0
	    rcount[s] = 0
    for text in sentences:
	    for i in range(len(text)):
	 	 if(i == 0 & i < len(text)-1):   
			if(text[i+1] == currentword):
			    lcount[text[i]] += 1
		 elif(i == len(text)-1):
		     if(text[i-1] == currentword):
			 rcount[text[i]] += 1
		 elif(i > 0 & i < len(text)-1):
		    if(text[i-1] == currentword):             
			rcount[text[i]] += 1    
		    elif(text[i+1] == currentword):             
			lcount[text[i]] += 1    
    vec = np.array([list(lcount.values()),list(rcount.values())])
    normalarray = normalize(vec, axis=1, norm='l1')            
    finalar = np.concatenate((normalarray[0], normalarray[1]), axis=0)
    listofarrays.append(finalar)
X = np.array(listofarrays)
kmeans = KMeans(n_clusters=25, random_state=0).fit(X)"""            
for k in range(25):
	clusteredwords = []
	for j in range(len(kmeans.labels_)):
		if(k == kmeans.labels_[j]):		
			clusteredwords.append(frequentwords[j])	
	print(k,":",clusteredwords)
