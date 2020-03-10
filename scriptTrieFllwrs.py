import instaloader
from collections import Counter
from login import *

L = instaloader.Instaloader()

# Login or load session
L.login(loginT, passW)# (login)


# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, 'lunaloisel')

""" followers = set()
followees = set()

for followee in profile.get_followers():
    username = followee.username
    followers.add(username)
    #print(username)

for fan in profile.get_followees():
    username = fan.username
    followees.add(username)
    #print(username + "!")

fans = set()
amies = set()
famous = set()

amies = followers.intersection(followees)
fans = followers.difference(followees)
famous = followees.difference(followers)

print(amies)
print(famous)
print(fans) 
 """
mes_likes = []

liker = set() #faire une liste afin de permettre de classer les personnes qui on liker le plus de post 
for post in profile.get_posts():
    for like in post.get_likes():
        mes_likes.append(like.username)
likes_trie = Counter(mes_likes).most_common()
print(likes_trie)
likes_trie = [i[0] for i in likes_trie]

print(likes_trie)

#Trouver pour chaque post qui a liker