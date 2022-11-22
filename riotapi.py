import requests
import json
    
#server = "na1.api.riotgames.com"
#region = "https://americas.api.riotgames.com"
#matchhistoryrequest = requests.get(matchv5url)
#matchhistory = matchhistoryrequest.json()

class riot:
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

    def matchhistoryids(self):
        region = self.getRegion(self.platform)
        apicall = "https://{0}/lol/match/v5/matches/by-puuid/{1}/ids?api_key={2}".format(region,self.puuid,self.apikey)
        request = requests.get(apicall)
        return request.json()

    def getmatchData(self,matchid):
        region = self.getRegion(self.platform)
        apicall = "https://{0}/lol/match/v5/matches/{1}?api_key={2}".format(region,matchid,self.apikey)    
        request = requests.get(apicall)
        return request.json()

    def getMLdata(self,match):
        info = match["info"]
        players = info["participants"]
        losingteam = []
        winningteam = []
        for player in players:
            if(player["win"]): winningteam.append(player["championName"])
            else: losingteam.append(player["championName"])
        print("winningteam\n",winningteam)
        print("losingteam\n",losingteam)
    
    

    def getIDjson(self,platform,name="Symphony"):
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
        print("self.id:",self.id,"\n self.accountID",self.accountID,"\nself.puuid",self.puuid)