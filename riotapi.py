import requests
import json
from ratelimit import limits, sleep_and_retry,RateLimitException
    
#server = "na1.api.riotgames.com"
#region = "https://americas.api.riotgames.com"
#matchhistoryrequest = requests.get(matchv5url)
#matchhistory = matchhistoryrequest.json()

class riot:
    TIME_PERIOD = 120  # time period in seconds
    MAX_CALLS_PER_TIME_PERIOD = 100

    apikey = ""
    id = ""
    accountID = ""
    puuid = ""
    platformhost = ""
    platform = ""

    def getRegion(self,platform):
        AMERICAS = "americas.api.riotgames.com"
        ASIA = "asia.api.riotgames.com"
        EUROPE = "europe.api.riotgames.com"
        SEA = "sea.api.riotgames.com"
        match platform:
            case "BR1":
                platform = AMERICAS
            case "EUN1":
                platform = EUROPE
            case "EUW1":
                platform = EUROPE
            case "JP1":
                platform = ASIA
            case "KR":
                platform = ASIA
            case "LA1":
                platform = AMERICAS
            case "LA2":
                platform = AMERICAS
            case "NA":
                platform = AMERICAS
            case "OC1":
                platform = SEA
            case "TR1":
                platform = EUROPE
            case "RU":
                platform = EUROPE
        return platform
        
    def platformcheck(self,platform):
        match platform:
            case "BR1":
                platform = "br1.api.riotgames.com"
            case "EUN1":
                platform = "eun1.api.riotgames.com"
            case "EUW1":
                platform = "euw1.api.riotgames.com"
            case "JP1":
                platform = "jp1.api.riotgames.com"
            case "KR":
                platform = "kr.api.riotgames.com"
            case "LA1":
                platform = "la1.api.riotgames.com"
            case "LA2":
                platform = "la2.api.riotgames.com"
            case "NA":
                platform = "na1.api.riotgames.com"
            case "OC1":
                platform = "oc1.api.riotgames.com"
            case "TR1":
                platform = "tr1.api.riotgames.com"
            case "RU":
                platform = "ru.api.riotgames.com"
        return platform

    @sleep_and_retry
    @limits(calls=MAX_CALLS_PER_TIME_PERIOD, period=TIME_PERIOD)
    def matchhistoryids(self):
        region = self.getRegion(self.platform)
        apicall = "https://{0}/lol/match/v5/matches/by-puuid/{1}/ids?api_key={2}".format(region,self.puuid,self.apikey)
        request = requests.get(apicall)
        return request.json()

    @sleep_and_retry
    @limits(calls=MAX_CALLS_PER_TIME_PERIOD, period=TIME_PERIOD)
    def getmatchData(self,matchid):
        region = self.getRegion(self.platform)
        apicall = "https://{0}/lol/match/v5/matches/{1}?api_key={2}".format(region,matchid,self.apikey)    
        #print(apicall)
        request = requests.get(apicall)
        return request.json()

    def getMLData(self,match):
        info = match["info"]
        players = info["participants"]
        teams = info["teams"]
        team1 = teams[1]
        teamwin = "1" if (team1["win"]) else "0"
        row = []
        for player in players:
            row.append(player["championName"])
        row.append(teamwin)
        return row
    
    @sleep_and_retry
    @limits(calls=MAX_CALLS_PER_TIME_PERIOD, period=TIME_PERIOD)
    def getIDjson(self,platform,name="SofaKingEasy"):
        server = self.platformcheck(platform)
        apicall = "https://{0}/lol/summoner/v4/summoners/by-name/{1}?api_key={2}".format(server,name,self.apikey)
        request = requests.get(apicall)
        return request.json()

                
    def changePlayer(self,platform,summonername):
        playerdata = self.getIDjson(platform,summonername)
        self.id = playerdata["id"]
        self.accountID = playerdata["accountId"]
        self.puuid = playerdata["puuid"]

    def __init__(self,summonername,platform,apikey):
        self.apikey = apikey
        playerdata = self.getIDjson(platform,summonername)
        self.id = playerdata["id"]
        self.accountID = playerdata["accountId"]
        self.puuid = playerdata["puuid"]
        self.platform = platform
        self.platformhost = self.platformcheck(platform)