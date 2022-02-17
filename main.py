import time
import requests
from termcolor import colored
#--------------------------------
base_url = "https://api.mail.tm/"
header = {"Accept": "application/json", "Content-Type": "application/json"}
#--------------------------------
point = 0
def name(point):
  for i in range(1000):
   point += 1
   string = "harshal"
   name = string + str(point)
   print(name)
   with open('Output/Email.txt', 'a+') as the_file:
     the_file.write(name+'\n')
#--------------------------------
def generate(gg):
 with open('Output/Email.txt') as file:
   while line := file.readline():
     lines = line.rstrip() 
     address = str(lines)+"@"+gg
     password = "Mihir1703#"    
     data = {"address": address, "password": password}       
     account = requests.post(base_url + "accounts", headers=header, json=data)
     h= account.status_code
     if h == 201:
        print(colored(f'Account Created with email{address}','blue'))
        time.sleep(0.2)
        with open('Output/Mail.txt', 'a+') as the:
               the.write(address+'\n')
     else:
        print(colored(f"Account Creation Failed Of {address}",'red'))
        time.sleep(2)
#--------------------------------
def domains():    
    available_domains = requests.get(base_url + "domains", headers=header).json()
    for value in available_domains:
      gg = value['domain']
      generate(gg)
#--------------------------------              
name(point)
domains()
