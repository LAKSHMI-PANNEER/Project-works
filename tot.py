
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

urls = ['https://support.google.com/photos/answer/6128838',
'https://support.google.com/photos/answer/6128843?co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/photos/answer/6128850',
'https://support.google.com/photos/answer/6128858?visit_id=637213412787536629-872446421&rd=1',
'https://support.google.com/photos/answer/6131416',
'https://support.google.com/photos/answer/6131416?visit_id=637176625396538486-1031873361&hl=en&rd=1&co=GENIE.Platform%3DDesktop',
'https://support.google.com/photos/answer/6153599?co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/photos/answer/6193313?co=GENIE.Platform%3DAndroid&hl=en&oco=0',
'https://support.google.com/photos/answer/6280921?hl=en',
'https://support.google.com/photos/answer/7362432',
'https://support.google.com/photos/answer/7378811?co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/photos/answer/7378942?hl=en&ref_topic=7378810&co=GENIE.Platform%3DAndroid',
'https://support.google.com/photos/answer/7539151?hl=en-GB&ref_topic=6128848',
'https://support.google.com/photos/answer/9284827?hl=en&ref_topic=6156061',
'https://support.google.com/photos/answer/9343965?hl=en',
'https://support.google.com/photos/answer/9380189?co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/photos/answer/9454489?hl=en-GB&ref_topic=6128848',
'https://support.google.com/photos/answer/9454489?hl=ur&ref_topic=6128848',
'https://support.google.com/photos/thread/29507038?hl=en',
'https://support.google.com/googlecamera/answer/2840311',
'https://www.lifewire.com/what-is-android-photo-sphere-1616136',
'https://www.androidcentral.com/how-use-new-messaging-feature-google-photos',
'https://www.androidcentral.com/how-set-google-photos',
'https://www.lifewire.com/how-to-delete-google-photos-4690368',
'https://www.lifewire.com/how-to-transfer-photos-from-phone-to-computer-4173057',
'https://www.lifewire.com/how-to-frame-photo-like-polaroid-1701563',
'https://www.lifewire.com/how-to-retrieve-google-backup-photos-4690013',
'https://www.lifewire.com/recover-deleted-photos-on-android-4165361',
'https://www.lifewire.com/save-instagram-photos-4125398',
'https://www.wikihow.com/Assign-a-Photo-to-a-Contact-on-Your-Android-Phone',
'https://support.google.com/chrome/a/answer/7131624',
'https://support.google.com/chrome/a/answer/9490493?hl=en&ref_topic=4386754',
'https://support.google.com/chrome/answer/114662?hl=en&co=GENIE.Platform=Android',
'https://support.google.com/chrome/answer/114662?hl=en-GB&co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/answer/95759?co=GENIE.Platform%3DAndroid&oco=1',
'https://support.google.com/chrome/answer/1385029?hl=en-GB&co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/answer/142065',
'https://support.google.com/chrome/answer/142065?hl=en-GB&ref_topic=7437824',
'https://support.google.com/chrome/answer/142893?hl=en&co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/answer/173424?hl=en&ref_topic=7439724&co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/answer/185277?co=GENIE&co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/chrome/answer/2391819?co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/answer/2392284?hl=bn',
'https://support.google.com/chrome/answer/2392709?co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/chrome/answer/2392709?co=GENIE.Platform%3DAndroid&hl=en-GB',
'https://support.google.com/chrome/answer/2765944?co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/chrome/answer/2765944?hl=en-gb&co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/answer/2790761?co=GENIE.Platform%253DAndroid&hl=en',
'https://support.google.com/chrome/answer/3220216?co=GENIE...hl=en&co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/chrome/answer/6204307',
'https://support.google.com/chrome/answer/6362090?hl=en&ref_topic=7437724',
'https://support.google.com/chrome/answer/7440301?co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/chrome/answer/9281740?hl=en-EN&ref_topic=7437824&co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/answer/95346?hl=en&ref_topic=14660&visit_id=637176604000229475-3948958844&rd=1&co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/chrome/answer/95417?co=GENIE.Platform%3DAndroid&hl=en',
'https://support.google.com/chrome/answer/95464?hl=is&co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/answer/95589',
'https://support.google.com/chrome/answer/95647?%20hl=fr&hlrm=en&co=GENIE.Platform%3DAndroid',
'https://support.google.com/chrome/a/answer/1360534',
'https://support.google.com/chrome/a/answer/3523633?hl=en&ref_topic=2935995'
]


for url in urls:

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
                #print ("Instruction:",o[i])
            
                words = o[i].split(' ')
                c = Counter(words)
                unique = [w for w in words if c[w] == 1]
                #print ("Number of unique words:",len(set(o[i].split())))
            
                w = [word for word in tokens if word.isalpha()]
                #print(w)
                #print("Number of words:",len(w))

                obj = list(filter(lambda x:x[1]=='NN',p))
                #print(obj)
                newob = [value1 for value1, value2 in obj]
                #print(newob)
                ob_frq.append(obj)
                #print("Number of objects:",len(obj))

                op = list(filter(lambda x:x[1]=='VB',p))
                #print(op)
                op_frq.append(op)
                #print("Number of operations:",len(op),'\n')
            
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

