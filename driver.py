import json
from riotapi import riot

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, indent=4)
    print(text)

key = "RGAPI-9996d7fa-7314-4105-8bd2-08aad782a578"
summonername = "Symphony"
region = "NA"
obj = riot(summonername,region,key)
#match = (obj.getmatchData("NA1_4497705376"))
matchesid = obj.matchhistoryids()
for matchid in matchesid:
    match = obj.getmatchData(matchid)
    losingteam, winningteam = obj.getMLData(match)
    print("\nmatchid:", matchid)
    print("winningteam\n",winningteam)
    print("losingteam\n",losingteam)
    print("\n")


