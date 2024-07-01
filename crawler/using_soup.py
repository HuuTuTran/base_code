from bs4 import BeautifulSoup
import requests
from datetime import datetime
from tabulate import tabulate

# Step 1: Send an HTTP request to the web page
current_time = datetime.now()

url = 'https://www.24h.com.vn/gia-vang-hom-nay-c425.html'
response = requests.get(url)

data = {}

soup = BeautifulSoup(response.content, 'html.parser')

# links = soup.find_all('table')
# find by tags

element = soup.find(class_='gia-vang-search-data-table')
# find by attribute


# Step 4: Extract data from elements
# for link in links:
#     print(link['href'])  
# Print the href attribute of each <a> tag

if element is not None:
    # print(element)  
    rows = element.find_all("tr")
    for row in rows:
    	name = row.find_all("h2")[0].text 
    	data[name] = []
    	prices = row.find_all("span")
    	for price in prices:
    		if 'colorGreen' in price['class'] or 'colorRed' in price['class']:
    			continue
    		data[name].append(price.text)

print("Gia vang: " + str(current_time))
# for key in data:
# 	print(key)
# 	for val in data[key]:
# 		print("")
# 		print(val)

# Create a list of dictionaries where each dictionary represents a row of the table
table_data = []
for key, values in data.items():
    row = {'Loai vang': key}
    row['Buy price'] =  values[0]
    row['Sell price'] =  values[1]
    table_data.append(row.copy())
# Print the table
print(tabulate(table_data, headers='keys', tablefmt='grid'))



url = "https://www.coindesk.com/price/bitcoin/"
response = requests.get(url)
html = BeautifulSoup(response.content, 'html.parser')
price = html.find(class_ ='currency-pricestyles__Price-sc-1v249sx-0 fcfNRE').text
print("bitcoin price: " +price)
