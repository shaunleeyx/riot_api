import pickle
import os.path



def loadData():
    # for reading also binary mode is important
    matchidlist = pickle.load(open('savefile', 'rb'))
    for item in matchidlist:
        print(item)
loadData()