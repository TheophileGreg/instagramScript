import instaloader
from login import *

L = instaloader.Instaloader()

# Login or load session
L.login(loginT, passW)# (login)


# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, 'rudyleguillermic')

followers = set()
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