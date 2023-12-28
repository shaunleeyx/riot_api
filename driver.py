import json
from riotapi import riot
import csv
import pickle
import os.path
import time



key = "RGAPI-ee9c71df-f827-485f-9fe1-c028d1fa4e3d"
summonername = input("Enter your summonername: ")
hashtagindex = summonername.find('#')
gamename = summonername[0:hashtagindex]
tagline = summonername[hashtagindex+1:len(summonername)]
region = "NA"
obj = riot(gamename,region,key,tagline)
delay = 0


#if there is no data.csv then make a new one with columns initiated
if(not(os.path.exists("data.csv"))):
    column_name = ["losing1","losing2","losing3","losing4","losing5","winning1","winning2","winning3","winning4","winning5","matchid"]
    f = open('data.csv','w',newline= '')
    writer = csv.writer(f)
    writer.writerow(column_name)
    f.close()

def printtoCSV(riot,write,picklefile,picklecurrent,puuid):
    puuidlist = []
    matchesid = riot.matchhistoryids(puuid)
    for matchid in matchesid:
        #time.sleep(30)
        match = riot.getmatchData(matchid)
        if('info' not in match):
            print("info:",match)
            continue
        #if(not match["info"]): continue
        gameMode = match["info"]["gameMode"]
        if (gameMode != "ARAM" or (matchid in matchidlist)): continue
        print("matchid1:",matchid)
        picklefile.append(matchid)
        combined , list =  (riot.getMLData(match))
        #print("list in function",list)
        write.writerow(combined)
        pickle.dump(matchidlist,picklecurrent)
        puuidlist += list
    return puuidlist

    

path_to_file = "savefile"
matchidlist = pickle.load(open('savefile', 'rb')) if(os.path.exists(path_to_file)) else []    
try:
    with open('data.csv','a',newline = "") as f,open('savefile','wb') as dbfile: #"r" represents the read mode
        writer = csv.writer(f, delimiter=',')
        list = printtoCSV(obj,writer,matchidlist,dbfile,obj.puuid)
        for puuid in list:
            printtoCSV(obj,writer,matchidlist,dbfile,puuid)
        #        time.sleep(30)
        #    time.sleep(30)
        f.close()
        dbfile.close()

except:
        pickle.dump(matchidlist,dbfile)
    
        
        




