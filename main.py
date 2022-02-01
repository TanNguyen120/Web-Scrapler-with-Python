from bs4 import BeautifulSoup
import requests


#get the text file from a web page
htmlContent = requests.get('https://www.masterduelmeta.com/').text

soup = BeautifulSoup(htmlContent,'lxml')

newCards = soup.find_all('div',class_='information svelte-kncn9e')

for newCard in newCards:
    tile = newCard.find('p', class_='title svelte-kncn9e').text
    updateTime = newCard.find('div', class_='sub-text full-width svelte-kncn9e').text
    print ("tile: "+ tile)
    print ("info: "+ updateTime)

