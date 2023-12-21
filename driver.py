import json
from riotapi import riot
import csv
import pickle
import os.path


key = "RGAPI-b82a4a85-4016-4b76-869f-a0b8f2bd4cb1"
summonername = input("Enter your summonername: ")
hashtagindex = summonername.find('#')
gamename = summonername[0:hashtagindex]
tagline = summonername[hashtagindex+1:len(summonername)]
region = "NA"
obj = riot(gamename,region,key,tagline)
matchesid = obj.matchhistoryids()


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
        for matchid in matchesid:
            match = obj.getmatchData(matchid)
            if('info' not in match):
                print(match)
                continue
            #if(not match["info"]): continue
            gameMode = match["info"]["gameMode"]
            if (gameMode != "ARAM" or (matchid in matchidlist)): continue
            print(matchid)
            matchidlist.append(matchid)
            combined , list = (obj.getMLData(match))
            writer.writerow(combined)

            for puuid in list:
                matchesid = obj.matchhistoryids(puuid)
                for matchid in matchesid:
                    match = obj.getmatchData(matchid)
                    if('info' not in match):
                        print(match)
                        continue
                    #if(not match["info"]): continue
                    gameMode = match["info"]["gameMode"]
                    if (gameMode != "ARAM" or (matchid in matchidlist)): continue
                    print(matchid)
                    matchidlist.append(matchid)
                    combined , list = (obj.getMLData(match))
                    writer.writerow(combined)
        print(dbfile)
        pickle.dump(matchidlist,dbfile)
        f.close()
        dbfile.close()

except:
        pickle.dump(matchidlist,dbfile)
    
        
        




