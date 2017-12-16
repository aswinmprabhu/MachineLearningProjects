import tweepy
from textblob import TextBlob

consumer_key='xxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret='xxxxxxxxxxxxxxxxxxxxxxxxxx'

access_token='xxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret='xxxxxxxxxxxxxxxxxxxxxxxxxx'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

places = api.geo_search(query="India", granularity="country")
place_id = places[0].id



p1 = raw_input("Enter the name of party 1 : ")
p2 = raw_input("Enter the name of party 2 : ")

t1 = list(raw_input("Enter the list of words about which if the sentiment is positive, it will be beneficial for "+p1+" : ").split(' '))
t2 = list(raw_input("Enter the list of words about which if the sentiment is positive, it will be beneficial for "+p2+" : ").split(' '))


tweetsAbtP1=api.search(p1)
tweetsAbtP2=api.search(p2)

for i in range(len(t1)):
	tweetsAbtP1.append(api.search(q = 'place:'+place_id+' '+p1,c = 200))

for i in range(len(t2)):
        tweetsAbtP2.append(api.search('place:'+place_id+' '+p2,c= 200))

c1=0
s1=0.0
r1=0.0

c2=0
s2=0.0
r2=0.0

for tweet in tweetsAbtP1:
	try:
		analysis = TextBlob(tweet.text)
		c1+=1
		s1+=analysis.sentiment.polarity
	except:
		pass
for tweet in tweetsAbtP2:
	try:
		analysis = TextBlob(tweet.text)
		c2+=1
		s2+=analysis.sentiment.polarity
	except:
		pass
r1=s1/c1
r2=s2/c2

print(r1,r2)

if r1>r2 : print(p1+" will win .")
else :print(p2+" will win .")
