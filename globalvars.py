from enum import Enum

from rich.console import Console


Count_Jobs = 0

Count_Pages = 0

Count_Failed_Jobs = 0

Count_Filterd_Jobs = 0

Count_Sent = 0

num_of_testing = 3

Registerd_threads = []


class TypeOfMessage(Enum):
    
    Delay = 0
    
    Success = 1
    
    Failed = 2


def Finish_scraping_unit(index):
    global Registerd_threads
    Registerd_threads[index] = True
    
    
def Country_CODE(countryName) -> str:
        
    if countryName == 'الاردن':
        return 'JO'
        
    elif countryName == 'الكويت':
        return 'KW'
        
    elif countryName == 'مصر':
        return 'EG'
        
    elif countryName == 'السعودية':
        return 'SA'
        
    elif countryName == 'الامارات':
        return 'AE'
        
    elif countryName == 'قطر':
        return 'QA'
        
    elif countryName == 'فلسطين':
        return 'PS'
        
    elif countryName == 'لبنان':
        return 'LB'
        
    elif countryName == 'عمان':
        return 'OM'
        
    elif countryName == 'سوريا':
        return 'SY'
        
    
    elif countryName == 'السودان':
        return 'SD'
        
    elif countryName == 'الجزائر':
        return 'DZ'
        
    elif countryName == 'البحرين':
        return 'BH'
        
    elif countryName == 'تونس':
        return 'TN'
        
    elif countryName == 'ليبيا':
        return 'LY'
        
    elif countryName == 'المغرب':
        return 'MA'
        
    elif countryName == 'العراق':
        return 'IQ'
        
    elif countryName == 'اليمن':
        return 'YE'
        
    else:
        return 'uknown'
    
def Extract_exp(exp) -> int:
        
    Experiance = 0
        
    if len(exp) > 1:
            
        Save_latter = []
        Save_tries = False
            
        for Letter in exp:
                
            try:
                num = int(Letter)
                if Save_tries == True:
                    Last_Index = len(Save_latter) - 1
                    Save_latter[Last_Index] = int(str(Save_latter[Last_Index]) + str(num))
                else:
                    Save_tries = True
                    Save_latter.append(num)
             
            except:
                Save_tries = False
                continue
            
        if len(Save_latter) == 0:
            return Experiance
        else:
            Experiance = max(Save_latter)
            return Experiance
                
    elif len(exp) == 1:
            
        try:
            Experiance = int(exp)
            return Experiance
        except:
            return Experiance
    
def Filter_Jobs(Jobs):
    y = 0
        
    Final_ls = []
    
    while y < len(Jobs):
            
      
        x = 0
            
        Duplacited = False
            
        
            
        while x < len(Jobs):
                
            
            count = 0
                
            if x != y:
                    
                if Jobs[x]['Name'] == Jobs[y]['Name']:
                    count += 1
                if Jobs[x]['GenralPro'] == Jobs[y]['GenralPro']:
                    count += 1
                if Jobs[x]['CountryCODE'] == Jobs[y]['CountryCODE']:
                    count += 1
                if Jobs[x]['BriefOfTheJob'] == Jobs[y]['BriefOfTheJob']:
                    count += 1
                

                   
                
            if(count == 4):
                
                Duplacited = True
                break
            else:
                Duplacited = False
                
            x += 1
            
        if Duplacited == False:
            Final_ls.append(Jobs[y])
            Count_Filterd_Job()
        y += 1
    
    return Final_ls

def Change_Console_Title():
    Console().set_window_title('Jobs collected: ' + str(Count_Jobs) + ' | ' + 'Pages fetched: ' + str(Count_Pages) + ' | ' + 'Failed jobs: ' + str(Count_Failed_Jobs) + ' | ' + 'Filtered Jobs: ' + str(Count_Filterd_Jobs) + ' | ' + 'Sent to Database: ' + str(Count_Sent) )

    
def Count_Job():
    global Count_Jobs
    Count_Jobs += 1
    Change_Console_Title()
    
def Count_Page():
    global Count_Pages
    Count_Pages += 1
    Change_Console_Title()

def Count_Failed_Job():
    global Count_Failed_Jobs
    Count_Failed_Jobs += 1
    Change_Console_Title()

def Count_Filterd_Job():
    global Count_Filterd_Jobs
    Count_Filterd_Jobs += 1
    Change_Console_Title()

def Count_Sent_To_DataBase():
    global Count_Sent
    Count_Sent += 1
    Change_Console_Title()
    
def StatusMessage(Message,TypeOfMessage):
    
    color = ''
    emoji = ''
    
    if TypeOfMessage.Success == TypeOfMessage:
        color = '#0ccf3a'
        emoji = ':vampire:'
        
    elif TypeOfMessage.Delay == TypeOfMessage:
        color = '#f7ab07'
        emoji = '🛏️'
    else:
        color = '#c70821'
        emoji = '😡'
        
    Console().print("[#03a1fc]Status:[/#03a1fc]" + Message + ' ' + emoji,style="bold " + color,emoji=True)
