
from bs4 import BeautifulSoup
import requests
import nltk
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from collections import Counter 
from nltk import Tree
import re

url = 'https://www.lifewire.com/how-to-edit-videos-on-android-4770052'
r = requests.get(url)
s = BeautifulSoup(r.content, 'html.parser')
ol_read = [tag.text for tag in s.find_all('ol')]
ol = [m+'' for m in ol_read]
ol_list = "".join(ol)
with open('D:\instructions.txt', 'w') as file:
    file.write(ol_list)

file = open("D:\instructions.txt").read()
sent = nltk.sent_tokenize(file)
ls=len(sent)
    
with open('D:\out.txt', 'w') as outfile:
    outfile.write("\n".join(sent))

with open('D:\out.txt', 'r') as outfile:
    o=outfile.readlines()

ob_frq=[]
op_frq=[]

for i in range(len(o)):
    tokens = nltk.word_tokenize(o[i])
    words = [word for word in tokens if word.isalpha()]
    p=nltk.pos_tag(words)
    
    first_word = o[i].split()
    first = first_word[:2]
    #print(first)
    n=nltk.pos_tag(first)
    #print(n)

    for word, tag in n:
        if tag in ('VB'):
            print ("Instruction:",o[i])
            
            words = o[i].split(' ')
            c = Counter(words)
            unique = [w for w in words if c[w] == 1]
            print ("Number of unique words:",len(set(o[i].split())))
            
            w = [word for word in tokens if word.isalpha()]
            print(w)
            print("Number of words:",len(w))

            obj = list(filter(lambda x:x[1]=='NN',p))
            print(obj)
            newob = [value1 for value1, value2 in obj]
            #print(newob)
            ob_frq.append(obj)
            print("Number of objects:",len(obj))

            op = list(filter(lambda x:x[1]=='VB',p))
            print(op)
            op_frq.append(op)
            print("Number of operations:",len(op),'\n')
            
print('----------------------------------------------')
#print(ob_frq)      
print("From URL:",url,"\n")

ob_li=[]
for item in ob_frq:
    for i in item:
        ob_li.append(i)
print("Objects:",Counter(ob_li),'\n')
print("Most Frequent Object:",Counter(ob_li).most_common(2),'\n')

#print(op_frq)       
op_li=[]
for item in op_frq:
    for i in item:
        op_li.append(i)
print("Operations:",Counter(op_li),'\n')
print("Most Frequent Operation:",Counter(op_li).most_common(2))

