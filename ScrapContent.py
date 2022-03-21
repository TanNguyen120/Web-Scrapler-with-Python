from contextlib import nullcontext
from tokenize import String
from typing import no_type_check
from bs4 import BeautifulSoup
import requests





# get new and leak from master duel meta
def getDuelMasterContet():
    mailContent = ""

    leakHTMLContent = requests.get('https://www.masterduelmeta.com/leaks-and-updates').text

    leakSoup = BeautifulSoup(leakHTMLContent,'lxml')

    leakCards = leakSoup.find_all('div', class_= 'information svelte-kncn9e')
    
    leakCount = 0

    for leakCard in leakCards:
        if(leakCount < 2):
            mailContent = mailContent + ("\n ---------------------------------------------------------------------------------- \n")
            mailContent = mailContent + leakCard.text
        leakCount += 1
    #-------------------------------------------------------------------------------------------------------------------------------

    tierListHTMLContent = requests.get('https://www.masterduelmeta.com/tier-list').text

    tierSoup = BeautifulSoup(tierListHTMLContent,'lxml')

    tierDecks = tierSoup.find_all('div', class_= 'label svelte-1xbooa7')

    # for tierDeck in tierDecks:
    #     deckName = tierDeck.find('div', class_='label svelte-1xbooa7')
    #     deckPower = tierDeck.find('div', class_='power-label svelte-1winidr')
    #     mailContent = mailContent + ("\n ---------------------------------------------------------------------------------- \n")
    #     mailContent = mailContent + ' deck: ' + deckName + 'power: ' + deckPower 



    #-------------------------------------------------------------------------------------------------------------------------------

    #get the text file from a web page
    htmlContent = requests.get('https://www.masterduelmeta.com/').text


    soup = BeautifulSoup(htmlContent,'lxml')

    cards = soup.find_all('div',class_='perspective svelte-kncn9e')
    
    # create an empty string
    count = 0
    # we just want to scrap the new not the fist four card
    for card in cards:
        if(count > 5):
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
        count += 1
    print("scrap content from master duel meta successful")
    return mailContent

#******************************************************************************************************************************************************
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
            mailContent = mailContent +'vàng: ' + type + ' mua vào: ' + buyPrice +'vnđ' +' || ' + ' bán ra: ' + sellPrice + 'vnđ'
    print("scrap gold price successful")
    return mailContent

#******************************************************************************************************************************************************

def getElectricSchedule():
    mailContent = ""
    htmlContent = requests.get('https://ithongtin.com/lich-cat-dien-an-giang').text
    soup = BeautifulSoup(htmlContent,'lxml')
    table = soup.find_all('tr')[1:]

    for tr in table:
        tds = tr.find_all('td')
        mailContent = mailContent + (" %s, %s \n" % \
              (tds[0].text, tds[1].text))
        mailContent +=  ("\n ---------------------------------------------------------------------------------- \n")
    if(len(mailContent) != 0):
        print('get lich cat dien successful')
    return mailContent


