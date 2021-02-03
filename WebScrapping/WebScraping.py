import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

req =requests.get("https://pythonhow.com/example.html",  headers=headers)
cont =req.content
soup=BeautifulSoup(cont,"html.parser")
#all=soup.find_all("div",{"class":"cities"})
all=soup.find_all("div",class_="cities")
all[0].find_all("h2")[0].text
for str in all:
    print(str.find("h2").text)

for str in all:
    print(str.find_all("h2")[0].text)
