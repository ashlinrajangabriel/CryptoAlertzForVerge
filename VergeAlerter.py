# importing libraries
from bs4 import BeautifulSoup as BS
import requests
import re
import urllib3
import beepy as beep
import time



 

    
    
def  StartAlert():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # method to get the proce of bit coin
    def get_price(currency):
        url = "https://www.google.com/search?q={}+price".format(currency)
        # getting the request from url
        data = requests.get(url,verify=False)
     
        # converting the text
        soup = BS(data.text, 'html.parser')
     
        # finding metha info for the current price
        ans = soup.find("div", class_ ="BNeawe iBp4i AP7Wnd").text
         
        # returning the price
        return ans
        
  
    
    while(1):
        time.sleep(60)
        Verge = get_price('Verge')
        Verge = re.findall('\d*\.?\d+',Verge) 
        
        if (float(Verge[0])>=2.35):
            print ("Alert !!!",Verge[0])
            
            beep.beep(sound='wilhelm')
            
        elif(float(Verge[0])<1.25):
            
            print ("Alert !!!",Verge[0])
            beep.beep(sound='robot_error')

        else:
            print ("Alert !!!",Verge[0])
            



    
    
    
StartAlert()
