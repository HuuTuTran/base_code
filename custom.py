import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import openpyxl
import csv   
import json


# def findByidTarget(id=0):
# 	file = open("migration_map.csv")
# 	csvreader = csv.reader(file)
# 	header = next(csvreader)
# 	rows = []
# 	rsl = {}
# 	for row in csvreader:
# 	    rows.append(row)
# 	file.close()
# 	for i in rows:
# 		if i[2]=='product' and i[3]==str(id):
# 			rsl['id_desc']= i[4]
# 			rsl['handle'] = json.loads(i[7])['handle']
# 			return rsl
# response = requests.get('https://stamped.io/api/v2/192387/dashboard/reviews',
#             auth = HTTPBasicAuth('pubkey-c0814U121BHTKgUlzxzKj5L73q3j3L', 'key-yW5C80FY7rx7K04KIv51s56e0s0G4o')).json()

# for i in response['results']:
# 	fields=[findByidTarget(i['review']['productId'])['handle'],'published',i['review']['rating'],i['review']['title'],i['review']['author'],i['review']['email'],i['review']['location'],i['review']['body'],i['review']['reply'],i['review']['dateCreated'],i['review']['dateReplied']]
# 	with open(r'reviews_template.csv', 'a', encoding="utf-8") as f:
# 	    writer = csv.writer(f)
# 	    writer.writerow(fields)

# 3 0 2*0
# 4 2 2*1
# 5 6 2*3
# 6 12 2*6
i = 2
rsl = 6
plus = 6
while i < 5 :
	i+=1
	if i>3:
		plus +=2
	rsl += plus
print(rsl)