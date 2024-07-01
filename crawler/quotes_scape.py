import requests as r
from bs4 import BeautifulSoup
from tabulate import tabulate
import time


tables = []

for page in range(2,3):
	response = r.get(f'https://quotes.toscrape.com/page/{page}/') 

	soup = BeautifulSoup(response.content, 'html.parser')


	quotes_divs = soup.find_all("div",class_="quote")



	if quotes_divs:
		for row in quotes_divs:
			content = row.find("span",class_="text")
			author = row.find("small",class_="author")
			tags = row.find_all('a',class_="tag")
			tags_content = []
			for tag in  tags:
				tags_content.append(tag.text)
			tags_content = ",".join(tags_content)
			table_row = {'content':content.text}
			table_row['author']  = author.text
			table_row['tags']  = tags_content
			tables.append(table_row)

	else:
		print('no quotes found')
# print(tables)
print(tabulate(tables, headers='keys', tablefmt='grid'))
