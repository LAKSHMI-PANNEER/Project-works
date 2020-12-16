from mongoengine import *

connect('6033', host='localhost', port=27017)

class Post(Document):
    title = StringField()
    
cname = Post(title='Open Source Technologies')
cname.save()       
print(cname.title)
