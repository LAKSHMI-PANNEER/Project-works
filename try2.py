import nltk
from nltk.corpus import webtext
from nltk.probability import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt
 
words = ['contact']
 
nltk.download('webtext')
wt_words = webtext.words('D:\out.txt') 
 
points = [(x, y) for x in range(len(wt_words)) for y in range(len(words)) if wt_words[x] == words[y]]
 
if points:
    x, y = zip(*points)
else:
    x = y = ()
 
plt.plot(x, y, "rx", scalex=.1)
plt.yticks(range(len(words)), words, color="b")
plt.ylim(-1, len(words))
plt.title("Lexical Dispersion Plot")
plt.xlabel("Word Offset")
plt.show()
