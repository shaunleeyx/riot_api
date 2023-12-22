import json
from riotapi import riot
import csv
import pickle
import os.path
import time



key = "RGAPI-edc3fa83-9534-4882-9439-c5ab5ac8395e"
summonername = input("Enter your summonername: ")
hashtagindex = summonername.find('#')
gamename = summonername[0:hashtagindex]
tagline = summonername[hashtagindex+1:len(summonername)]
region = "NA"
obj = riot(gamename,region,key,tagline)
matchesid = obj.matchhistoryids()
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
try:
    with open('data.csv','a',newline = "") as f,open('savefile','wb') as dbfile: #"r" represents the read mode
        writer = csv.writer(f, delimiter=',')
        for matchid in matchesid:
            #time.sleep(30)
            match = obj.getmatchData(matchid)
            if('info' not in match):
                print("info:",match)
                continue
            #if(not match["info"]): continue
            gameMode = match["info"]["gameMode"]
            if (gameMode != "ARAM" or (matchid in matchidlist)): continue
            print("asdasd   ",matchid)
            matchidlist.append(matchid)
            combined , list = (obj.getMLData(match))
            writer.writerow(combined)
            print("list",list)
            for puuid in list:
                print("puuid in driver:",puuid)
                matchesid2 = obj.matchhistoryids(puuid)
                for matchid in matchesid:
                    match = obj.getmatchData(matchid)
                    if('info' not in match):
                        continue
                    #if(not match["info"]): continue
                    gameMode = match["info"]["gameMode"]
                    if (gameMode != "ARAM" or (matchid in matchidlist)): continue
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
    
        
        




