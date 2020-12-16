from textblob import TextBlob
import nltk

file = open("D:\instruction.txt").read()

blob = TextBlob(file) 
for nouns in blob.noun_phrases:
    print(nouns)
    
text = nltk.word_tokenize(file)
pos_tagged = nltk.pos_tag(text)
#print(pos_tagged)
nouns = list(filter(lambda x:x[1]=='NN',pos_tagged))
print(nouns)

for word, tag in pos_tagged:
    if tag in ('VB'):
        print (word, tag)

from textblob import TextBlob
text = "Tap Save copy in the upper right corner to save your video."
text_blob_object = TextBlob(text)
for ngram in text_blob_object.ngrams(2):
    print(ngram)

