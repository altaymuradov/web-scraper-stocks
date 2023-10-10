import requests
from bs4 import BeautifulSoup as bs
import time

startTime = time.time()

pages = []

for pageNumber in range(1,5):
    urlStart = 'https://www.centralcharts.com/en/price-list-ranking/'
    urlEnd = 'ALL/desc/ts_19-us-nasdaq-stocks--qc_2-daily-change?p='
    url= urlStart + urlEnd + str(pageNumber)
    pages.append(url)
    
valueList = []
for page in pages:
    webpage=requests.get(page)
    soup = bs(webpage.text, 'html.parser')

    stockTable = soup.find('table', class_='tabMini tabQuotes')
    trTagList = stockTable.find_all('tr')

    for eachTrTag in trTagList[1:]:
        tdTagList = eachTrTag.find_all('td')

        rowValues = []
        for eachTdTag in tdTagList[0:7]:
            newValue = eachTdTag.text.strip()
            rowValues.append(newValue)
        valueList.append(rowValues)

# print(valueList)
# print('--- %s seconds ---' % (time.time() - startTime))

length_list = [len(element) for row in valueList for element in row]
for row in valueList:

    row = "".join(element.ljust(9) for element in row)

    print(row)