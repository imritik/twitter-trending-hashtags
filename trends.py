import twitter
import json

## Twitter credentials
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""


auth = twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)

twitter_api=twitter.Twitter(auth=auth)


print twitter_api


WORLD_WOE_ID = 1
US_WOE_ID = 23424977
IN_WOE_ID = 23424848

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)
in_trends = twitter_api.trends.place(_id=IN_WOE_ID)

# print world_trends[0][0]
# print
# print us_trends


# print json.dumps(world_trends[0]["trends"], indent=1)
print
# print json.dumps(us_trends, indent=1)

for tname in world_trends[0]["trends"]:
    print tname["name"]
print 
print "============================="
print "TRENDS IN INDIA IS HERE "
print "============================="

for tname in in_trends[0]["trends"]:
    print tname["name"]
