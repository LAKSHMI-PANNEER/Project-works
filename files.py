import requests
from bs4 import BeautifulSoup
import nltk
from nltk import sent_tokenize

url = 'https://www.lifewire.com/how-to-edit-videos-on-android-4770052'

reqs = requests.get(url)

soup = BeautifulSoup(reqs.text,'lxml')

for tag in soup.find_all("ol"): 
    t=tag.text
    print(t)

tokens = nltk.sent_tokenize(t)
print (tokens)

links_list_prettified = [tag.text for tag in soup.find_all("ol")]

list_with_word = [m+'' for m in links_list_prettified]

list_as_one = "".join(list_with_word)

with open('D:\soup_list.txt', 'w') as file:
    file.write(list_as_one)
