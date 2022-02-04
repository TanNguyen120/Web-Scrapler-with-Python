from contextlib import nullcontext
from tokenize import String
from typing import no_type_check
from bs4 import BeautifulSoup
import requests






def getDuelMasterContet():
        #get the text file from a web page
    htmlContent = requests.get('https://www.masterduelmeta.com/').text

    soup = BeautifulSoup(htmlContent,'lxml')

    cards = soup.find_all('div',class_='perspective svelte-kncn9e')
    
    # create an empty string
    mailContent = ""
    for card in cards:
        tile = card.find('p', class_='title svelte-kncn9e').text
        updateTime = card.find('div', class_='sub-text full-width svelte-kncn9e').text
        anchorLink = card.find('a',class_='image-card svelte-kncn9e')
        mailContent = mailContent + ("\n ---------------------------------------------------------------------------------- \n")
        anchorHref = anchorLink['href']
        updateTime.rstrip("\n")
        anchorHref.rstrip("\n")
        mailContent = mailContent + ("Tile: "+ tile + "\n")
        if(len(updateTime) != 0):
            mailContent = mailContent + ("Info: "+ updateTime)
            mailContent = mailContent + ("Link:" + 'https://www.masterduelmeta.com'+anchorHref)
    return mailContent


def getGoldPrice():
    htmlContent = requests.get('https://www.pnj.com.vn/blog/gia-vang/').text

    soup = BeautifulSoup(htmlContent,'lxml')

    priceTable = soup.find_all('tr')
    
    # create an empty string
    mailContent = ""
    for goldType in priceTable:
        rowCheck = goldType.find('td', class_='colorGrey pdL10')
        if not (rowCheck is None):
            type =  goldType.find('td', class_='colorGrey pdL10').text
            buyPrice = goldType.find('td', class_='price_in').text
            sellPrice = goldType.find('td',class_='price_out').text
            mailContent = mailContent + ("\n ---------------------------------------------------------------------------------- \n")
            mailContent = mailContent +'vàng: ' + type + ' mua vào: ' + buyPrice +'vnđ' +'||' + ' bán ra: ' + sellPrice + 'vnđ'
    return mailContent
