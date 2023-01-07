import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
#SEARCH = input().replace(" ", "+")

#url = f"https://www.amazon.com/s?k={SEARCH}" #&crid=3HQJMD8HATXRI&sprefix=rtx+3060%2Caps%2C146&ref=nb_sb_noss_1
url = "https://www.amazon.com/deals?ref_=nav_cs_td_lm_dt_cr&deals-widget=%257B%2522version%2522%253A1%252C%2522viewIndex%2522%253A0%252C%2522presetId%2522%253A%2522AB48D68973BA06D9DFD05723DA760601%2522%252C%2522dealType%2522%253A%2522LIGHTNING_DEAL%2522%252C%2522sorting%2522%253A%2522BY_SCORE%2522%257D"
page = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(page.content, "html.parser")
dealsGrid = soup.find("div", attrs={"class":'Grid-module__gridDisplayGrid_2X7cDTY7pjoTwwvSRQbt9Y'})
#for child in bodyTag.children:
    #print(child)
print(dealsGrid.string.strip())