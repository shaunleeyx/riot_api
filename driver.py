import json
from riotapi import riot
import csv
import pickle
import os.path


key = "RGAPI-ad96ef91-3ca4-4be0-893e-5904bde5343f"
summonername = input("Enter your summonername: ")
region = "NA"
obj = riot(summonername,region,key)
matchesid = obj.matchhistoryids()

#if there is no data.csv then make a new one with columns initiated
#if(not(os.path.exists("data.csv"))):
#    column_name = ["losing1","losing2","losing3","losing4","losing5","winning1","winning2","winning3","winning4","winning5","matchid"]
#    f = open('data.csv','w',newline= '')
#    writer = csv.writer(f)
#    writer.writerow(column_name)
#    f.close()

path_to_file = "savefile"
matchidlist = pickle.load(open('savefile', 'rb')) if(os.path.exists(path_to_file)) else []    
try:
    with open('data.csv','a',newline = '') as f,open('savefile','wb') as dbfile: #"r" represents the read mode
        writer = csv.writer(f)
        for matchid in matchesid:
            #print(matchid)
            match = obj.getmatchData(matchid)
            if('info' not in match):
                print(match)
                continue
            #if(not match["info"]): continue
            gameMode = match["info"]["gameMode"]
            if (gameMode != "ARAM" or (matchid in matchidlist)): continue
            print(matchid)
            matchidlist.append(matchid)
            combined = (obj.getMLData(match))
            writer.writerow(combined)
        pickle.dump(matchidlist,dbfile)
        f.close()
        dbfile.close()

except:
        pickle.dump(matchidlist,dbfile)
    
        
        




