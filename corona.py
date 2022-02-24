#Corona: Shreya
import requests
from bs4 import BeautifulSoup
from plyer import notification
import time
result = requests.get('https://www.mohfw.gov.in/').text
soup = BeautifulSoup(result,'html.parser')
soup.encode("utf-8")
total_cases = soup.find('li',{'class':'bg-blue'}).get_text().strip()
print(total_cases)
while True:
 notification.notify(
    title = "Covid Update",
    message = total_cases,
    app_icon = "C:\\Users\\Dell\\OneDrive\\Desktop\\project PE\\virus_corona_coronavirus_icon_140473.ico",
    timeout = 5
 )
 time.sleep(5)