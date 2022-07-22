
from ast import And, If
from asyncio import sleep
from datetime import datetime
from functools import partial
import imp
import json
from random import Random, random
from sqlite3 import Time
from xml.dom.minidom import Element
from xmlrpc.client import DateTime
from attr import s
from colorama import Style
import requests
from itertools import zip_longest
from bs4 import BeautifulSoup, Tag
import csv
import time
from gazpacho import Soup
from dateutil.relativedelta import relativedelta
from iteration_utilities import unique_everseen
import sys
import globalvars as ref
import aiohttp







class Wazaf:
        
    
    
    
    def FetchPage(self,urls):
            
            for url in urls:
                
                ref.StatusMessage('Featching page ' + url,ref.TypeOfMessage.Success)
                ref.Count_Job()
                response = requests.get(url)
                content = response.content
                soup =  BeautifulSoup(content,"lxml")
            
            
                GenralPro = soup.find(string='القسم :').parent.parent.a.text.strip().strip('\n')
            

                """print(soup.find(string=' صاحب العمل :').parent.parent.lable.text.strip().strip('\n'))
                print(soup.find(string='الدولة\n: ').parent.parent.lable.text.strip().strip('\n'))
                print(soup.find(string='نوع العمل\n: ').parent.parent.lable.text.strip().strip('\n'))
                print(soup.find(string=' وصف الوظيفة ').parent.parent.find_all('strong',{})[1].text.strip().strip('\n'))
                """
                
                try:
                    Name = soup.find(string=' صاحب العمل :').parent.parent.lable.text.strip().strip('\n')
                except:
                    Name = soup.find(string=' طالب الوظيفة').parent.parent.lable.text.strip().strip('\n')
                    
                try:
                    City = soup.find(string='المنطقة / المحافظة\n: ').parent.parent.lable.text.strip().strip('\n')
                except:
                    City = ''
                    
                CountryNAME = soup.find(string='الدولة\n: ').parent.parent.lable.text.strip().strip('\n')
                CountryCODE = ref.Country_CODE(countryName=CountryNAME)
                CreatedAt = datetime.now()
            
                Date_ExpireAt = CreatedAt + relativedelta(months=1)
            
                Worktime = 0
                
                try:
                    if soup.find(string='نوع العمل\n: ').parent.parent.lable.text.strip().strip('\n') == 'دوام جزئي':
                        Worktime = 1
                    else:
                        Worktime = 2
                except:
                    Worktime = 2
                    
                        
        
                Workplace = 2
            
                try:
                    exp = ref.Extract_exp(soup.find(string='سنين الخبرة\n: ').parent.parent.lable.text.strip().strip('\n'))
                except:
                    exp = 0
                
                try:
                    Grade = soup.find(string='المستوى التعليمى\n: ').parent.parent.lable.text.strip().strip('\n')
                except:
                    Grade = GenralPro
                    
                Job_Description = soup.find(string=' وصف الوظيفة ').parent.parent.find_all('strong',{})[1].text.strip().strip('\n')
            
                if City == '':
                    Worklocation = CountryNAME
                else:
                    Worklocation = CountryNAME + ',' + City
                    
                
                self.Jobs.append({
                'GenralPro' : GenralPro,
                'SpecifcPro' : Grade,
                'Name' : Name,
                'LastName' : '',
                'CreatedAt' : CreatedAt,
                'ExpireDate' : Date_ExpireAt,
                'IsAdmin' : True,
                'exp' : exp,
                'CountryCODE' : CountryCODE,
                'CountryNAME' : CountryNAME,
                'Worklocation' : Worklocation,
                'Workplace' : Workplace,
                'City' : City,
                'BriefOfTheJob' : Job_Description,
                'url' : url,
                'ShowAdd' : True,
                'urlImage' : '',
                'Worktime' : Worktime
            })
                
                ref.StatusMessage('Got all Page Details!',ref.TypeOfMessage.Success)
                ref.StatusMessage('Delay ..',ref.TypeOfMessage.Delay)
                time.sleep(self.rest_between_jobs_sec)
                ref.StatusMessage('Delay Finished',ref.TypeOfMessage.Success)
            
    
    def Scrap(self,rest_between_pages_sec , rest_between_jobs_sec,test = False):
        
        self.pagenumber = 1
        
        self.Jobs = []
        
        self.rest_between_pages_sec = rest_between_pages_sec
        self.rest_between_jobs_sec = rest_between_jobs_sec
        
        num = 0
        while True:
            
            if test == True:
                if(num == ref.num_of_testing):
                    break
            
            self.url = 'https://wazaf.net/jobs-today/?pagenum=' + str(self.pagenumber)
            ref.Count_Page()
            response = requests.session().get(self.url)

            content = response.content

            soup =  BeautifulSoup(content,"lxml")
        
                
            section = soup.find('section',{'class':'small-slider text-center first-slider'})
            part = section.find('div',{'class' : 'row'})
            urls = part.findAll('a')
            url_text = []
            
            for url in urls:
                url_text.append(url.attrs['href'])
                
            
            ref.StatusMessage('Page number: ' + str(self.pagenumber) + ' Jobs counts is ' + str(len(urls)),ref.TypeOfMessage.Success)
            
            self.FetchPage(url_text)
            
            if soup.find('a',{'class' : 'next page-numbers'}) == None:
                break
            
            self.pagenumber += 1
            
            ref.StatusMessage('Resting before start in the next page ...',ref.TypeOfMessage.Delay)
            time.sleep(rest_between_pages_sec)
            ref.StatusMessage('Rest ended',ref.TypeOfMessage.Success)
            num += 1
        
        
        Filtered_jobs = ref.Filter_Jobs(self.Jobs)
        
        
        ref.StatusMessage('Finshed Scraping Wazaf jobs',ref.TypeOfMessage.Success)
        
        return Filtered_jobs
        

       
        
                
 # Not working
class Wazzuf:
    
    
    def Scrap(self):
        
        self.pagenumber = 0
        
        def Fetch_Page(urls):
            
            #for loop in urls
            
            soup = BeautifulSoup(requests.get(urls[0],).content,'html.parser')
            
            print(soup.encode())
            GenralPro = soup.find_all('h1',{'class' : 'css-f9uh36'})
            
            print(GenralPro)
            SpecificPro = GenralPro
            
            
            Job_Detials = soup.find_all('span',{'class' : 'css-4xky9y'})
            
            print(len(Job_Detials))
        
       
        
        url = 'https://wuzzuf.net/search/jobs/?a=hpb&filters%5Bpost_date%5D%5B0%5D=within_24_hours&start=' + str(self.pagenumber)  
        
        content = requests.get(url).content
        
        soup = BeautifulSoup(content,'lxml')
        
        links = soup.find_all('a',{'class':'css-o171kl','rel' : 'noreferrer'})
        
        jobs_links = []
        
        for link in links:
            jobs_links.append('https://wuzzuf.net' + link.attrs['href'])
        
        
        Fetch_Page(jobs_links)
        
        

class Shaglanty:
    
    def Fetch_Page(self,urls,rest_sec):
            
            for url in urls:
                
                
                ref.StatusMessage('Feaching Job with url ' + '/' + url + ' and in page number ' + str(self.Pagenumber),TypeOfMessage=ref.TypeOfMessage.Success)
                job_url = 'https://shoghlanty.com/' + url
                
                page = BeautifulSoup(requests.get(url=job_url).content,'lxml')
        
                table = page.find('table',{'class' : 'table1' ,'style' : 'width:280px;' , 'align' : 'center'})  
        
                Details = table.find_all('tr')
        
                Convert_To_Json = {}
                
                for Detail in Details:
                    
                   Array = Detail.find('th').find_all('h3')
                   
                   if(len(Array) == 0):
                       
                       Array2 = Detail.find('th').find_all('h2')
                       
                       if(len(Array2) == 0):
                           
                           continue
                       
                       else:
                        
                           Json = {str(Array2[0].text).strip().strip('\n') : str(Array2[1].text).strip().strip('\n')}
                           Convert_To_Json |= Json
                   
                   elif(len(Array) == 1):
                       
                       Key = str(Array[0].text).strip().strip('\n')
                       
                       value = str(Array[0].parent.parent.find('td').find('h2').text).strip().strip('\n')
                       
                       Convert_To_Json |= {Key : value}
                
                Convert_To_Json |= { 'SOURCE_URL' : job_url }
                
                self.Jobs.append(Convert_To_Json)
                ref.StatusMessage('Got all url jobs!',ref.TypeOfMessage.Success)
                ref.Count_Job()
                ref.StatusMessage('Delay..',ref.TypeOfMessage.Delay)
                time.sleep(rest_sec)
                ref.StatusMessage('Delay ended',ref.TypeOfMessage.Success)
                
                
    
    
    def Scrap(self,rest_sec,rest_between_jobs_sec,test = False):
        
        self.Jobs = []
        
        self.Pagenumber = 1
        
        
        
        num = 0
        while True:
            if test == True:
                if num == ref.num_of_testing:
                    break
            
          
            soup = BeautifulSoup(requests.get(url='https://shoghlanty.com/search.aspx?query=%D9%88%D8%B8%D8%A7%D8%A6%D9%81%20%D8%A7%D9%84%D9%8A%D9%88%D9%85&page=' + str(self.Pagenumber)).content,'lxml')
        
            elements = soup.find_all('a',{'style' : 'text-decoration:underline;'})
        
            urls = []
        
            for url in elements:
                urls.append(url.attrs['href'])
            
            ref.StatusMessage('Page number ' + str(self.Pagenumber) + ' and Jobs count is ' + str(len(urls)),ref.TypeOfMessage.Success)
            
            ref.Count_Page()
            
            self.Fetch_Page(urls=urls,rest_sec=rest_between_jobs_sec)
            
            try:
                if soup.find('a',{'alt' : 'التالي','title' : 'التالي'}) == None:
                    break
            except:
                break
            
            self.Pagenumber += 1
            
            ref.StatusMessage('Delay',ref.TypeOfMessage.Delay)
            
            num += 1
            
            time.sleep(rest_sec)
            ref.StatusMessage('Rest ended',TypeOfMessage=ref.TypeOfMessage.Success)
        
        Formated_jobs = []
    
        for job in self.Jobs:
            
            job = dict(job)
            
            BriefOfTheJob = ''
            City = ''
            CountryCODE = ''
            CountryNAME = ''
            CreatedAt = datetime.now()
            ExpireDate = CreatedAt + relativedelta(months=1)
            GenralPro = ''
            IsAdmin = True
            Name = ''
            LastName = ''
            ShowAdd = True #Ignore it for now
            SpecifcPro = ''
            Worklocation = ''
            Workplace = 2 #Ignore it for now
            Worktime = 2
            urlImage = '' #Ignore it for now
            exp = 1
            source_url = job['SOURCE_URL'] #Name it url
            
            
            
            if 'المصدر' in job.keys():
                Name = job['المصدر']
            else:
                print('This job not good Because Name')
                continue
            
            if 'الدولة' in job.keys():
                CountryNAME = job['الدولة']
                CountryCODE = ref.Country_CODE(countryName=CountryNAME)
                
            else:
                print('This job not good Country')
                continue
            
            
            if 'الوظيفة الخالية' in job.keys():
                GenralPro = job['الوظيفة الخالية']
            else:
                print('This job not good Because GenralPro')
                continue
            
            if 'الشروط' in job.keys():
                BriefOfTheJob = job['الشروط']
            else:
                pass
            
            if 'تفاصيل المؤهِل' in job.keys() and BriefOfTheJob == '':
                BriefOfTheJob = job['تفاصيل المؤهِل']
            else:
                if BriefOfTheJob == '':
                    BriefOfTheJob = 'مطلوب ' + GenralPro
            
            
            if 'مؤهِل' in job.keys():
                SpecifcPro = job['مؤهِل']
            else:
                SpecifcPro = GenralPro
                
            if 'سنوات الخبرة' in job.keys():
                exp = ref.Extract_exp(exp=job['سنوات الخبرة'])
            else:
                exp = 0    
            
            if 'مدينة العمل' in job.keys():
                City = job['مدينة العمل']
                Worklocation = CountryNAME + ',' + City
            else:
                Worklocation = CountryNAME
                
            if 'مجال العمل' in job.keys():
                pass
            else:
                pass
            
            if 'جنسية الموظف' in job.keys():
                pass
            else:
                pass
            
            if 'النوع' in job.keys():
                pass
            else:
                pass
            
            if 'لغة أولى' in job.keys():
                pass
            else:
                pass
            
            Formated_jobs.append({
                'GenralPro' : GenralPro,
                'SpecifcPro' : SpecifcPro,
                'Name' : Name,
                'LastName' : LastName,
                'CreatedAt' : CreatedAt,
                'ExpireDate' : ExpireDate,
                'IsAdmin' : IsAdmin,
                'exp' : exp,
                'CountryCODE' : CountryCODE,
                'CountryNAME' : CountryNAME,
                'Worklocation' : Worklocation,
                'Workplace' : Workplace,
                'City' : City,
                'BriefOfTheJob' : BriefOfTheJob,
                'url' : source_url,
                'ShowAdd' : ShowAdd,
                'urlImage' : urlImage,
                'Worktime' : Worktime
            })
            
        
        Final_ls = ref.Filter_Jobs(Formated_jobs)
        
        
        ref.StatusMessage("All jobs from Shaglanty Formated Currectly ! u have " + str(len(Final_ls)) + ' Jobs after Filtiring it and Before is ' + str(len(Formated_jobs)),TypeOfMessage=ref.TypeOfMessage.Success)
        ref.StatusMessage('Shaglanty last jobs got scrapped successfully!',TypeOfMessage=ref.TypeOfMessage.Success)
        return Final_ls
        
            
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
    
        
        

        

