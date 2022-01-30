from bs4 import BeautifulSoup

# doc file html local
with open('index.html', 'r') as htmlFile:
    content = htmlFile.read()
    # read the content with beauty ful soup
    soup = BeautifulSoup(content,'lxml')

    tags = soup.find_all('div',class_='price')
    for tag in tags:
        print(tag.span)