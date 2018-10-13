import twitter
import json

## Twitter credentials
CONSUMER_KEY = "Y5XFRuxBWJ1btZU6xu93IGCGF"
CONSUMER_SECRET = "lbCJ8qP79EKqlzkrsGvegUbE7k3rm2JZDYqX3TbbcPaj6ZVfkh"
OAUTH_TOKEN = "1032328800321777664-uvHGxG2TwP110GSWlLdYOv483fqNNX"
OAUTH_TOKEN_SECRET = "NiCzXy0cQ3QzeYDpq539lSXQ4jFzQEmYINEgu7N8gjndW"


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
