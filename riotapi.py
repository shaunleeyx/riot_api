import requests
import json
    
server = "na1.api.riotgames.com"
region = "https://americas.api.riotgames.com"
matchhistoryapi = "/lol/match/v5/matches/by-puuid/{puuid}/ids"


#matchhistoryrequest = requests.get(matchv5url)
#matchhistory = matchhistoryrequest.json()

class riot:
    apikey = ""

    def __init__(self,apikey):
        self.apikey = apikey
        print(self.apikey)

    def regioncheck(self,region):
        match region:
            case "BR1":
                region = "br1.api.riotgames.com"
            case "EUN1":
                region = "eun1.api.riotgames.com"
            case "EUW1":
                region = "euw1.api.riotgames.com"
            case "JP1":
                region = "jp1.api.riotgames.com"
            case "KR":
                region = "kr.api.riotgames.com"
            case "LA1":
                region = "la1.api.riotgames.com"
            case "LA2":
                region = "la2.api.riotgames.com"
            case "NA":
                region = "na1.api.riotgames.com"
            case "OC1":
                region = "oc1.api.riotgames.com"
            case "TR1":
                region = "tr1.api.riotgames.com"
            case "RU":
                region = "ru.api.riotgames.com"
        return region




    def getIDjson(self,region,name="Symphony"):
        server = self.regioncheck(region)
        apicall = "https://{0}/lol/summoner/v4/summoners/by-name/{1}?api_key={2}".format(server,name,self.apikey)
        print(apicall)
        request = requests.get(apicall)
        return request.json()

                
