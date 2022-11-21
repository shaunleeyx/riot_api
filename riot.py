import requests
import json
    
server = "na1.api.riotgames.com"
region = "https://americas.api.riotgames.com"
apikey = "RGAPI-16d253e5-f549-46d6-b345-a38f26e0ef11"
matchhistoryapi = "/lol/match/v5/matches/by-puuid/{puuid}/ids"
puuid = "VZGeiLRo-jnyT4qa3eSNM39hdOr6wyV7AxCHkHE66ocileMfKBtMSQznhFHpU_jmqNYeUWEq-mORiQ"
matchv5url = region + matchhistoryapi.format(puuid=puuid) + "?api_key=" + apikey


#matchhistoryrequest = requests.get(matchv5url)
#matchhistory = matchhistoryrequest.json()

class riot:

    def regioncheck(region):
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
            case "NA1":
                region = "na1.api.riotgames.com"
            case "OC1":
                region = "oc1.api.riotgames.com"
            case "TR1":
                region = "tr1.api.riotgames.com"
            case "RU":
                region = "ru.api.riotgames.com"
        return region


    def jprint(obj):
        # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_apikeys=True, indent=4)
        print(text)


    def getIDjson(apikey,server,name="Symphony"):
        apicall = "https://{0}/lol/summoner/v4/summoners/by-name/{1}?api_key={2}".format(server,name,apikey)
        request = requests.get(apicall)
        return request.json()

    def __init__(self,apikey):
        self.apikey = apikey
        self.region = self.regioncheck(region)
                