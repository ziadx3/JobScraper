

#Start Scrapping

import asyncio
from datetime import datetime
import Bot
import time
import multiprocessing
import google_crc32c
from grpc import Status
from rich.console import Console
from Modules import Wazaf,Wazzuf,Shaglanty
import globalvars as ref

import firebase_admin
from firebase_admin import credentials,firestore

import threading

import multiprocessing.pool as pool


#cred = credentials.Certificate("adminjson.json")

#firebase_admin.initialize_app(cred)



Test = False
Jobs = []

def Target1():
    global Jobs
    ls =  Wazaf().Scrap(3,1,Test)
    
    Jobs = Jobs + ls
    
def Target2():
    global Jobs
    ls = Shaglanty().Scrap(rest_sec=2,rest_between_jobs_sec=1,test=Test)
    
    Jobs = Jobs + ls
    


# Start point
#db =  firestore.client()




t1 = threading.Thread(target=Target1)

t2 = threading.Thread(target=Target2)

t1.start()

t2.start()

t2.join()
t1.join()





if Test == False:
    ref.StatusMessage('Sending data to Hirestation database ..',ref.TypeOfMessage.Delay)
    num_of_elements = 1
    num_of_sent = 0
    Delay_time = 1 * 60
    
    for job in Jobs:
        
        if num_of_sent == num_of_elements:
            num_of_sent = 0
            ref.StatusMessage('Waiting till sleeping finish ..',TypeOfMessage=ref.TypeOfMessage.Delay)
            time.sleep(Delay_time)
            ref.StatusMessage('Waiting ended',TypeOfMessage=ref.TypeOfMessage.Success)
        
        job['CreatedAt'] = datetime.now()
        
        
        
        
        #Bot.Send_Bot(job['Name'],job['GenralPro'],job['Worklocation'],job['SpecifcPro'],job['BriefOfTheJob'],job['exp'],job['url'])
        
        ref.Count_Sent_To_DataBase()
        num_of_sent += 1
        
            
            
        
        

ref.StatusMessage('Program finished',ref.TypeOfMessage.Success)

input()