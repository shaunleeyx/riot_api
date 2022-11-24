import json
from riotapi import riot
import csv
import pickle
import os.path


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, indent=4)
    print(text)

key = "RGAPI-d8703075-df44-4e75-aa8f-de0718fd013a"
summonername = "Symphony"
region = "NA"
obj = riot(summonername,region,key)
matchesid = obj.matchhistoryids()
column_name = ["losing1","losing2","losing3","losing4","losing5","winning1","winning2","winning3","winning4","winning5"]
path_to_file = "savefile"
matchidlist = pickle.load(open('savefile', 'rb')) if(os.path.exists(path_to_file)) else []    
with open('data.csv','a',newline = '') as f,open('savefile','wb') as dbfile: #"r" represents the read mode
    writer = csv.writer(f)
    writer.writerow(column_name)
    for matchid in matchesid:
        match = obj.getmatchData(matchid)
        gameMode = match["info"]["gameMode"]
        if (gameMode != "ARAM" or matchid in matchidlist): continue
        matchidlist.append(matchid)
        combined = (obj.getMLData(match))
        writer.writerow(combined)
    pickle.dump(matchidlist,dbfile)
    f.close()
    dbfile.close()

        
        




