# JSON is a commonly used format for returning objects from API calls (e.g., when we get data from Twitter, Instagram, Facebook, etc). 
# Below, we have provided a hypothetical string userProfilesString in JSON format that contains information about 5 user profiles.
# 1.Read the userProfilesString string as a python object userProfiles using json functions.
#   Suppose it's been 3 days since you got the Twitter profile data. In the past 3 days, the following twitter activity happened:
#   (a) Iman tweeted 5 times and liked 5 tweets.
#   (b) Allan tweeted once.
#   (c) Xinyan tweeted 10 times, followed 17 people and got 25 new followers.

# 2.Add the Twitter activity from the last 3 days to userProfiles

# 3.Convert the updated userProfiles python object back to a string in JSON format

# 4.Print the updated JSON string, sorted in alphabetical order, and in a human-readable format (hint: try indent=4).
import json
userProfilesString = '{"profiles": \n{"Iman"\n\n: {"tweets": 450, "likes": 2500, "followers": 190, "following": 300},\n\n"Allan"\n\n: {"tweets": 200, "likes": 700, "followers": 150, "following": 100},\n\n"Xinyan"\n\n: {"tweets": 1135, "likes": 3000, "followers": 400, "following": 230},\n\n"Hao"\n\n: {"tweets": 645, "likes": 800, "followers": 300, "following": 500},\n"Harman"\n\n: {"tweets": 300, "likes": 1750, "followers": 200, "following": 400}}}'
userProfiles = json.loads(userProfilesString)
userProfiles['profiles']['Iman']['tweets'] ,userProfiles['profiles']['Iman']['likes'] = userProfiles['profiles']['Iman']['tweets'] + 5,userProfiles['profiles']['Iman']['likes'] + 5
userProfiles['profiles']['Allan']['tweets'] = userProfiles['profiles']['Allan']['tweets'] + 1
userProfiles['profiles']['Xinyan']['tweets'],userProfiles['profiles']['Xinyan']['following'],userProfiles['profiles']['Xinyan']['followers'] = userProfiles['profiles']['Xinyan']['tweets'] + 10,userProfiles['profiles']['Xinyan']['following'] + 17,userProfiles['profiles']['Xinyan']['followers'] + 25
print(userProfiles)
userProfiles = json.dumps(userProfiles , indent = 4)
print(userProfiles)