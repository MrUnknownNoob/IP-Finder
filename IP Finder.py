import socket
import requests

print('''

 _____  ____     _____  _____  _   _  ____   _____  ____  
|_   _||  _ \   |  ___||_   _|| \ | ||  _ \ |  ___||  _ \ 
  | |  | |_| |  | |___   | |  |  \| || | | || |___ | |_| |
  | |  |  __/   |  ___|  | |  | |\  || | | ||  ___||    / 
  | |  | |      | |      | |  | | | || | | || |    | |\ \ 
 _| |_ | |      | |     _| |_ | | | || |_| || |___ | | | |
|_____||_|      |_|    |_____||_| |_||____/ |_____||_| |_|

****** Tool Name ::IP Finder ******
       Why This tool :: This tool Is Made for Find own Public and Private IP
       Contact with Me : https://github.com/mrwnknown
    ** Donot try to Copy This. All right Reserved By MR.UNKOWN 

1. Private IP
2. Public IP    

''')

select = input("Select A Number :")

if(select == '1'):
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print("My Private is :",ip)
    print("You Are Working On", hostname)  

if(select == '2'):

    hostname = socket.gethostname()
    a = requests.get("https://api.ipify.org").text
    print("My Public Ip is :",a)
    print("You Are Working On", hostname)







