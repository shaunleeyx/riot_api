import json
from riotapi import riot
import csv
import pickle
import os.path
import time



key = "RGAPI-f55102ca-c20d-4bca-a04d-c232f9b9ac67"
summonername = input("Enter your summonername: ")
hashtagindex = summonername.find('#')
gamename = summonername[0:hashtagindex]
tagline = summonername[hashtagindex+1:len(summonername)]
region = "NA"
obj = riot(gamename,region,key,tagline)
matchesid = obj.matchhistoryids(obj.puuid)
delay = 0


#if there is no data.csv then make a new one with columns initiated
if(not(os.path.exists("data.csv"))):
    column_name = ["losing1","losing2","losing3","losing4","losing5","winning1","winning2","winning3","winning4","winning5","matchid"]
    f = open('data.csv','w',newline= '')
    writer = csv.writer(f)
    writer.writerow(column_name)
    f.close()

path_to_file = "savefile"
matchidlist = pickle.load(open('savefile', 'rb')) if(os.path.exists(path_to_file)) else []    
print(matchidlist)
try:
    with open('data.csv','a',newline = "") as f,open('savefile','wb') as dbfile: #"r" represents the read mode
        writer = csv.writer(f, delimiter=',')
        print("matchesid1:",matchesid)
        for matchid in matchesid:
            #time.sleep(30)
            match = obj.getmatchData(matchid)
            print("matchidasdasdasd",match)
            if('info' not in match):
                print("info:",match)
                continue
            #if(not match["info"]): continue
            gameMode = match["info"]["gameMode"]
            if (gameMode != "ARAM" or (matchid in matchidlist)): continue
            #print("matchid1:",matchid)
            matchidlist.append(matchid)
            combined , list = (obj.getMLData(match))
            print("puuidlist:",list)
            writer.writerow(combined)
            for puuid in list:
                print("puuid in driver:",puuid)
                matchesid = obj.matchhistoryids(puuid)
                for matchid in matchesid:
                    match = obj.getmatchData(matchid)
                    if('info' not in match):
                        continue
                    #if(not match["info"]): continue
                    gameMode = match["info"]["gameMode"]
                    if (gameMode != "ARAM" or (matchid in matchidlist)): continue
                    print("matchid2:",matchid)
                    matchidlist.append(matchid)
                    combined , list = (obj.getMLData(match))
                    writer.writerow(combined)
            #        time.sleep(30)
            #    time.sleep(30)
        print(dbfile)
        pickle.dump(matchidlist,dbfile)
        f.close()
        dbfile.close()

except:
        pickle.dump(matchidlist,dbfile)
    
        
        




