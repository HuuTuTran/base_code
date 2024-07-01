# def strip_html(self,html_string):
#     from bs4 import BeautifulSoup
#     soup = BeautifulSoup(html_string, 'html.parser')
#     return soup.get_text()

# import xmltodict
# import json

# def convert_xml_to_json(xml_data):
#     # Parse XML into a dictionary
#     data_dict = xmltodict.parse(xml_data)

#     # Convert the dictionary to JSON
#     json_data = json.dumps(data_dict)

#     return json_data


# import mysql.connector

# def connect_to_mysql():
#     try:
#         # Establish a connection to the remote MySQL server
#         connection = mysql.connector.connect(
#             host='45.33.0.186',
#             user='root',
#             password='LeCM$123Mysql',
#             database='jay_194414'
#         )

#         if connection.is_connected():
#             print('Connected to MySQL server')
#             return connection

#     except mysql.connector.Error as error:
#         print(f'Error connecting to MySQL server: {error}')

#     return None



# connection = connect_to_mysql()

# variants = []

# if connection:
#     id = 0
#     # Perform database operations using the connection
#     while True:
#         cursor = connection.cursor()
#         cursor.execute(f'SELECT * FROM image_data where id > {id} limit 10 ')
#         rows = cursor.fetchall()
#         if not rows:
#             break 
#         for row in rows:
#             id = row[0]
#             rsl = convert_xml_to_json(row[2])
#             product = json.loads(rsl)['product'] 
#             if 'variations' in product:
#                 for child in product['variations']['variants']['variant']:
#                     variants.append(child['@product-id'])
#                     print(child['@product-id'])
#             # print(product)

#         # Close the connection
#     connection.close()
#     self.log(variants,'variants')

# import datetime

# # Set the two dates to compare
# date1 = datetime.date(2022, 7, 1)
# date2 = datetime.date(2020, 3, 30)

# # Compare the two dates using the comparison operators
# if date1 < date2:
#     print("date1 is earlier than date2")
# elif date1 > date2:
#     print("date1 is later than date2")
# else:
#     print("date1 and date2 are the same")

# #WRITE, READ CSV

# import csv

# pro = []
# with open('Mariko.csv', newline='', encoding='utf8', errors='replace') as f:
#     reader = csv.reader(f)
#     data = list(reader)
# for line in data:
#     rsl = []
#     # if line[14] == 'Categorieen_Alle':
#     #     continue
#  #    # print(line[14])
#     # for row in line[14].split(' > '):
#     #     if ';' in row:
#     #         rsl = rsl +row.split(';')
#     #     else: 
#     #         if  row :
#     #             rsl.append(row)
#     # pro[line[2]] = rsl
#     pro.append({line[0]:line[6].replace('https://www.kaartjesvanmaaike.nl','')})
# print(pro)
	# break
#     emails.append(line[0])
# emails = list(set(emails))



# import requests
# import json

# since_id = 0
# while True:
#     url = f'https://allergy-buyers-club.myshopify.com/admin/products.json?limit=250&since_id={since_id}'
#     payload={}
#     headers = {
#       'X-Shopify-Access-Token': '',
#       'Cookie': '_master_udr=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxrWXpBearticlesE5XVmhOaTAxWW1GaExUUTRPRE10WVRSallTMWtZMkUzWXpJek5qRTBNMllHT2daRlJnPT0iLCJleHAiOiIyMDI0LTA4LTIyVDA5OjQwOjQ0LjA3MloiLCJwdXIiOiJjb29raWUuX21hc3Rlcl91ZHIifX0%3D--a085298c7e9ee3ac215ecc8c16a277a4dfa12dc0; _secure_admin_session_id=000e70bb048b787c32118932aa62d583; _secure_admin_session_id_csrf=000e70bb048b787c32118932aa62d583'
#     }
#     response = requests.request('GET', url, headers=headers, data=payload)
#     products = json.loads(response.text)['products']
#     fount = False 
#     if not products:
#         break
#     for product in products:
#         since_id= product['id']
#         if product['handle'] in emails:
#             requests.request('DELETE', f'https://allergy-buyers-club.myshopify.com/admin/products/{since_id}.json', headers=headers, data=payload)
#             print(since_id)


# with open('360_image.csv', newline='', encoding='utf8', errors='replace') as f:
#     reader = csv.reader(f)
#     data = list(reader)
# imported_data= []    
# for line in data:
#     if data.index(line) == 0:
#         continue
#     for i in range(1,37):
#         print(line[1]+f'/Filename_{i}.jpg')
#         file_name = f'/Filename_{i}.jpg' if i >= 10 else f'/Filename_0{i}.jpg'
#         write_data = [line[0],line[1]+ file_name ]
#         imported_data.append(write_data)
# with open('360detail.csv', 'w', encoding='utf8') as file:
#     # row[7] = row[7].replace(''',''') 
#     writer = csv.writer(file)
#     writer.writerows(imported_data)

# with open('bigC_review.csv', 'w', newline='', encoding='utf8') as outfile:
#     writer = csv.writer(outfile)
#     writer.writerows(data)
#  
# lst = [2,3,6,-5,-8]

# def subArrayExists(arr, N):
#     # traverse through array
#     # and store prefix sums
#     n_sum = 0
#     s = set()
 
#     for i in range(N):
#         n_sum += arr[i]
 
#         # If prefix sum is 0 or
#         # it is already present
#         if n_sum == 0 or n_sum in s:
#             return True
#         s.add(n_sum)
 
#     return False
# def check_sub_array(inp):
#     sum = 0
#     sums = set()
#     for i in inp:
#         sum = sum + i
#         print(sum)
#         if i in sums or sum == 0:
#             return True
#         sums.add(sum)
#         print(sums)
#     return False
# print(check_sub_array(lst))        
# print(subArrayExists(lst,5))

# Lists  = [i for i in  [2,2,2,2,2,2,3,2,2,2,2,2,3,4,5,7,6,6,4,2] if i != 2]
# print(Lists)
# poem='''
# If I can stop one heart from breaking,
# '''
# print(''.join(poem.splitlines()))
# ['NONINVENTORY', 'STANDARD', 'VOUCHER', 'SERIALIZED']

# import requests
# import json
# lst =[]
# imported = 0
# while True:
#     page = int((imported/1000))+1
#     url = f'https://cloudposapi.citruslime.com/api/item?pagingParameterModel.pageNumber={page}&pagingParameterModel.pageSize=1000&filterParameterModel.timestamp=0'
#     # print(url)
#     payload={}
#     headers = {
#       'accept': 'application/json',
#       'Authorization': 'a13a7d45-32d3-4c7e-a295-e3af2ea2656d',
#       'Cookie': 'ARRAffinity=d0cd888619ba46550a7f867de3f4826882610ac4e59f52608415db362753138a; ARRAffinitySameSite=d0cd888619ba46550a7f867de3f4826882610ac4e59f52608415db362753138a'
#     }

#     response = requests.request('GET', url, headers=headers, data=payload)
#     response = json.loads(response.text)
#     # print(imported)    
#     if not response:
#         break
#     for item in response:
#         # if item['ItemLookupCode']=='V338' : #item['ItemTypeAsString'] not in lst:
#         #     print(item)
#         #     lst.append(item['ItemTypeAsString'])
#         imported = imported + 1
# print(imported)             


# def flatten(self,multiline):
#     return multiline.replace('</br>',' ').replace('\r',' ')


# poem='''
# <p>Take a seat at the bar on the ultra modern Dart high stool. Teaming industrial cast iron legs with a durable wooden curved seat and backrest this functional and robust seating solution is the perfect addition for your stylish home.</p>\r</br><p>Size - H: 110cm x W: 44cm x D: 48cm</p>'''

# poem ='<ul>\r  <li>For reduction of allergens, asthma irritants, sub-micron particles and chemicals</li>\r  <li>Maximum coverage: up to 938 sq. ft. (2 air changes/hr)</li>\r  <li>Recommended coverage: up to 313 sq. ft. (6 air changes/hr)</li>\r  <li>Room air purifier</li>\r  <li>Removes 99.97% of all particles larger than 0.3 microns</li>\r  <li>Large particle pre-filter</li>\r  <li>Medium particle pre-filter</li>\r  <li>True medical grade HEPA filter</li>\r  <li>Activated Military Carbon Cloth HEGA filter</li>\r  <li>3 fan speeds</li>\r  <li>Manual controls</li>\r  <li>360° air intake, outflow from top side vent</li>\r  <li>4 casters (Not included on Junior model)</li>\r  <li>CSA, NRTL and CE approved</li>\r  <li>Colors: Sandstone, Black, Off-white, and Midnight blue</li>\r  <li>All steel construction with a powder coating paint finish</li>\r  <li>Made in the USA</li>\r</ul>'
# def flatten(multiline):
#     lst = multiline.split('</br>')
#     flat = ''
#     for line in lst:
#         flat += line
#     return flat
# print(flatten(poem))


# from datetime import datetime

# datetime_str = '2017-07-19 20:43:17'

# datetime_object = datetime.strptime(datetime_str, '%y-%m-%d %H:%M:%S')


# print(datetime_object.isoformat())
# import requests
# try:
#     response = requests.get('https://s0.2mdn.net/simgad/10571795013256893273',timeout=10)
# except Exception as e:
#     print(e) 

# import re

# lst =[{'id': 43674042073365, 'product_id': 7974379946261, 'title': '12 oz. Bag', 'price': '46.99', 'sku': '6rt', 'position': 1, 'inventory_policy': 'deny', 'compare_at_price': None, 'fulfillment_service': 'manual', 'inventory_management': 'shopify', 'option1': '12 oz. Bag', 'option2': None, 'option3': None, 'created_at': '2022-10-26T22:33:29-06:00', 'updated_at': '2022-10-26T22:33:31-06:00', 'taxable': False, 'barcode': '', 'grams': 363, 'image_id': None, 'weight': 0.8, 'weight_unit': 'lb', 'inventory_item_id': 45772136775957, 'inventory_quantity': -2, 'old_inventory_quantity': -2, 'requires_shipping': True, 'admin_graphql_api_id': 'gid://shopify/ProductVariant/43674042073365'}, {'id': 43674042138901, 'product_id': 7974379946261, 'title': '2 lb. Bag', 'price': '125.29', 'sku': '6ar', 'position': 2, 'inventory_policy': 'continue', 'compare_at_price': None, 'fulfillment_service': 'manual', 'inventory_management': None, 'option1': '2 lb. Bag', 'option2': None, 'option3': None, 'created_at': '2022-10-26T22:33:29-06:00', 'updated_at': '2022-11-02T20:13:45-06:00', 'taxable': False, 'barcode': '', 'grams': 953, 'image_id': None, 'weight': 2.1, 'weight_unit': 'lb', 'inventory_item_id': 45772136841493, 'inventory_quantity': 0, 'old_inventory_quantity': 0, 'requires_shipping': True, 'admin_graphql_api_id': 'gid://shopify/ProductVariant/43674042138901'}, {'id': 43674042106133, 'product_id': 7974379946261, 'title': '5 lb. Bag', 'price': '263.46', 'sku': '6vr', 'position': 3, 'inventory_policy': 'deny', 'compare_at_price': '309.95', 'fulfillment_service': 'manual', 'inventory_management': 'shopify', 'option1': '5 lb. Bag', 'option2': None, 'option3': None, 'created_at': '2022-10-26T22:33:29-06:00', 'updated_at': '2022-11-02T20:13:46-06:00', 'taxable': False, 'barcode': '', 'grams': 2313, 'image_id': None, 'weight': 5.1, 'weight_unit': 'lb', 'inventory_item_id': 45772136808725, 'inventory_quantity': 0, 'old_inventory_quantity': 0, 'requires_shipping': True, 'admin_graphql_api_id': 'gid://shopify/ProductVariant/43674042106133'}]


# lst = sorted(lst, key=lambda d: d['title']) 
# # print(lst)
# # lst.sort(key=lambda x: float(re.findall(r'\b\d+\b', x['title'])[0]))


# for i in lst:
#     print(i)

#     


# 



# import requests
# import json
# url = 'https://api.thebase.in/1/orders?offset=200&limit=100'

# payload={}
# headers = {
#   'Authorization': 'Bearer c569dbc23b3fb6401f8cec17efedf776'
# }
# d = []
# response = requests.request('GET', url, headers=headers, data=payload)


# orders = json.loads(response.text)
# orders = orders['orders']

# for order in orders:
#     d.append({order['terminated']:order['dispatch_status']})


# print(d)
# import requests
# import json
# url = 'https://artbyole.myshopify.com/admin/collections/188212871308/products.json'

# payload={}
# headers = {
#   'X-Shopify-Access-Token': ''
# }
# a= []
# response = requests.request('GET', url, headers=headers, data=payload)
# response = json.loads(response.text)
# for pro in response['products']:
#     a.append(pro['id'])
# print(a)

# lo = [5099486150796, 5099445715084, 7135519768716, 7135469437068, 7135451381900, 7135451086988, 7135450857612, 7135450661004, 7135449022604, 7135445483660, 7135445057676, 7135441387660, 7135439913100, 7135439585420, 7135439159436, 7135438504076, 7135438143628, 7135437815948, 7135437553804, 7135436341388, 7135435980940, 7135435620492, 7135435391116, 7135435030668, 7135434768524, 7135434473612, 7135434080396, 7135433818252, 7135433556108, 7135433162892, 7135428903052, 7135350194316, 5099626070156, 5099622432908, 5099555848332, 5099548803212, 5099543396492, 5099537989772, 5099475927180, 5099461902476, 5099454365836, 5089332887692, 5089324269708]
# print(len(a))
# output= ''
# for i in rsl:
#     output=output+'(''+i+''),'
# print(output)    


# 0 1
# 1 3
# 2 5
# 3 7
# 4 9
# 5

# param = 3
# import math


# def get_delta(a,b):
#     return a-b if a > b else b-a


# for i in range(param):
#     for j in range((param-1)*2+1):
#         current = math.floor(((param-1)*2+1)/ 2)
#         if j == current or get_delta(current,j) <= i :
#             print('*',end = ' ')
#         else:
#             print('',end = ' ')    
#     print('</br>')    

# 1 : 2^0 1 
# 2 : 2^1 2
# 3 : 2^2 4
# 4 : 8
# 5 : 16
# 6 : 32
# n : ?


# a[n] = a[n-1] * 2
# a[n] = 2^(n-1)

# a = 'pending,paid,pending,paid,paid,voided,refunded,voided,paid,pending,paid,pending,pending,pending,paid,paid,paid,pending,pending,pending,pending,partially_refunded,pending,paid,paid,pending'
# a ='Unfulfilled,Fulfilled,Scheduled,Fulfilled,Fulfilled,Unfulfilled,Fulfilled,On hold,Fulfilled,Unfulfilled,Fulfilled,Unfulfilled,Unfulfilled,Unfulfilled,Fulfilled,Scheduled,Scheduled,Unfulfilled,Unfulfilled,Unfulfilled,Unfulfilled,Fulfilled,Unfulfilled,Scheduled,On hold,On hold'
# rsl = {}
# for i in range(26):
#     rsl[str(i+1)] = a.split(',')[i].lower().replace(' ','_')
# print(rsl)
# a= ['250x175', '100x70', '150x105', '200x140', '400x280', '350x245', '300x210']
# a.sort()
# print(a)
# import requests

# url = 'https://openapi.etsy.com/v2/shops/20729820/listings/active/?limit=4&offset=96&oauth_consumer_key=51wipvka0bjm92d4ou0fea0g&oauth_token=7ca18649caaf2b4291cd6c5a1ea4e2&oauth_signature_method=HMAC-SHA1&oauth_timestamp=1672891223&oauth_nonce=u7f9rft5rKp&oauth_version=1.0&oauth_signature=IvU7XV21D2hdC2fzTRY5GlS%2FJAM%3D'

# payload={}
# headers = {
#   'Cookie': 'exp_hangover=YXXyJX_t81OA0C4w3YivQs08Du9jZACCpPMnVMH0Tea91UoFqUVpMfrlqUnxiUUlmWmZyZmJOfE5iSWpecmV8YWG8UYGRkZKVmmJOcWptQwA; fve=1657784357.0; uaid=GkcMO7PcmN_rqUoFNp6ugRnb0kRjZACCpBMvnoDoZDtXxWql0sTMFCUrpeIo_9SKUOOArLCKjCiziqCC8LCitGxnn9Iof1elWgYA; user_prefs=03YFCexFUO2gVqVRmnV-GPe3hkdjZACCpBPP_MD0-ROq0Uphfi5KOnmlOTk6Sql5uqHBSjpAIaiIEYTCRcQyAAA.'
# }

# response = requests.request('GET', url, headers=headers, data=payload)

# print(response.text)


# import calendar
# for i in range(1,13):
#     print(f''{calendar.month_name[i][:3]}':{i},')


# import http.client
# import json
# conn = http.client.HTTPSConnection('www.shelldesignshop.com')
# payload = ''
# headers = {}
# conn.request('GET', '/wp-json/wc/v3/products/36200?consumer_key=ck_4bba0017bd5ca78c2eb1e65e2f0089ef1cba2107&consumer_secret=cs_45c40b9b369a435cacaa3657d283673fbd4fcdb1', payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(json.loads(data.decode('utf-8')))


# import requests

# url = 'https://www.shelldesignshop.com/wp-json/wc/v3/products/36200'

# payload={}
# headers = {
#   'Authorization': 'Basic Y2tfNGJiYTAwMTdiZDVjYTc4YzJlYjFlNjVlMmYwMDg5ZWYxY2JhMjEwNzpjc180NWM0MGI5YjM2OWE0MzVjYWNhYTM2NTdkMjgzNjczZmJkNGZjZGIx'
# }

# response = requests.request('GET', url, headers=headers, data=payload)

# print(response.text)




# import requests

# url = 'https://www.shelldesignshop.com/wp-json/wc/v3/products/36200?consumer_key=ck_4bba0017bd5ca78c2eb1e65e2f0089ef1cba2107&consumer_secret=cs_45c40b9b369a435cacaa3657d283673fbd4fcdb1'

# payload={}
# headers = {}

# response = requests.get(url)

# print(response.text)


# from woocommerce import API

# wcapi = API(
#     url='https://www.shelldesignshop.com',
#     consumer_key='ck_4bba0017bd5ca78c2eb1e65e2f0089ef1cba2107',
#     consumer_secret='cs_45c40b9b369a435cacaa3657d283673fbd4fcdb1',
#     wp_api=True,
#     version='wc/v3'
# )
# print(wcapi.get('products/36200').json()['description'])


# import requests
# # print(requests.get('https://www.shelldesignshop.com/wp-json/wc/v3/products/36200?consumer_key=ck_4bba0017bd5ca78c2eb1e65e2f0089ef1cba2107&consumer_secret=cs_45c40b9b369a435cacaa3657d283673fbd4fcdb1').text)

# import json
# def api():
#     session = requests.Session()
#     session.headers = get_header()
#     return session

# def get_header():
#     return {
#         'Content-Type': 'application/json',
#         'Accept': 'application/json',
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
#         'X-Miva-API-Authorization': 'MIVA 8262fadf40292f0af484c3ec9597f695'
#     }

# def get_product_by_id(product_id, condition='EQ'):

#     payload = {
#         'Store_Code': 'API',
#         'Function': 'ProductList_Load_Query',
#         'Sort': 'id',
#         'Count': 4,
#         'Offset': 0,
#         'Filter': [
#             {
#                 'name': 'search',
#                 'value': [
#                     {
#                         'field': 'id',
#                         'operator': condition,
#                         'value': product_id
#                     }
#                 ]
#             },
#             {
#                 'name': 'ondemandcolumns',
#                 'value': [
#                     'descrip',
#                     'catcount',
#                     'attributes',
#                     'productimagedata',
#                     'categories',
#                     'productshippingrules',
#                     'relatedproducts',
#                     'uris',
#                     'productinventorysettings',
#                     'CustomField_Values:*',
#                     'product_inventory',
#                     'page_code',
#                     'cancat_code'
#                 ]
#             }
#         ]
#     }
#     result = api().post('https://www.arrowbookstore.com/Merchant5/json.mvc', json=payload)
#     return result.json()


# data = get_product_by_id(product_id=0, condition='GT')
# print(data)
# import json
# import requests


# url = 'https://heavymetaloffroad.com/admin/api/2023-01/orders.json'

# payload = json.dumps({
#   'order': {
#     'financial_status': 'refunded',
#     'confirmed': True,
#     'total_price': 1407.96,
#     'subtotal_price': 1407.96,
#     'currency': 'USD',
#     'processed_at': '2022-11-21 15:52:46-08:00',
#     'updated_at': '2022-11-28 17:55:17-08:00',
#     'send_receipt': False,
#     'send_fulfillment_receipt': False,
#     'suppress_notifications': True,
#     'taxes_included': False,
#     'shipping_lines': [
#       {
#         'price': 0,
#         'title': 'Free Shipping',
#         'code': 'Shipping'
#       }
#     ],
#     'customer': {
#       'id': 6490588676354
#     },
#     'billing_address': {
#       'first_name': 'test',
#       'last_name': 'test',
#       'address1': '711 University Ave',
#       'address2': '',
#       'city': 'san diego',
#       'province': 'California',
#       'country': 'United States',
#       'province_code': 'CA',
#       'country_code': 'US',
#       'zip': '92103',
#       'phone': '415889635897',
#       'name': 'test test',
#       'latitude': None,
#       'longitude': None,
#       'company': 'test'
#     },
#     'shipping_address': {
#       'first_name': 'test',
#       'last_name': 'test',
#       'address1': '711 University Ave',
#       'address2': '',
#       'city': 'san diego',
#       'province': 'California',
#       'country': 'United States',
#       'province_code': 'CA',
#       'country_code': 'US',
#       'zip': '92103',
#       'phone': '415889635897',
#       'name': 'test test',
#       'latitude': None,
#       'longitude': None,
#       'company': 'test'
#     },
#     'note': '',
#     'line_items': [
#       {
#         'variant_id': 43418260898050,
#         'title': '2005-2023 Toyota Tacoma Bed Bar 17 Inch 3 Set Heavy Metal Off-Road',
#         'price': 439.99,
#         'quantity': 2,
#         'sku': 'HMORBB03',
#         'product_id': 7884235079938,
#         'total_discount': 0,
#         'variant_title': None,
#         'name': '2005-2023 Toyota Tacoma Bed Bar 17 Inch 3 Set Heavy Metal Off-Road',
#         'properties': [],
#         'grams': '54.0000'
#       },
#       {
#         'variant_id': 43418261684482,
#         'title': '2005-2023 Toyota Tacoma Bed Bar 9 Inch Pair Heavy Metal Off-Road',
#         'price': 263.99,
#         'quantity': 2,
#         'sku': 'HMORBB05',
#         'product_id': 7884235407618,
#         'total_discount': 0,
#         'variant_title': None,
#         'name': '2005-2023 Toyota Tacoma Bed Bar 9 Inch Pair Heavy Metal Off-Road',
#         'properties': [],
#         'grams': '30.0000'
#       }
#     ]
#   }
# })
# headers = {
#   'X-Shopify-Access-Token': '',
#   'Content-Type': 'application/json',
#   'Accept': 'application/json',
#   'Cookie': 'request_method=POST'
# }

# response = requests.request('POST', url, headers=headers, data=payload)

# print(response.text)


#get all shopify
# import requests
# import json
# since_id = 0
# headers = {
#   'X-Shopify-Access-Token': '',
#   'Cookie': '_master_udr=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaEpJaWxpTmpGbE9UWmxNQzAyTUdObUxUUmlPREV0T0RZMk55MDRNalZqTURGa056QmhaV1FHT2daRlJnPT0iLCJleHAiOiIyMDI1LTAyLTA3VDAzOjI2OjM4Ljc1OVoiLCJwdXIiOiJjb29raWUuX21hc3Rlcl91ZHIifX0%3D--71a776a4da538b159dd9d0a84d76586be716315c; _secure_admin_session_id=938f79eff190696a2e4003e886c27239; _secure_admin_session_id_csrf=938f79eff190696a2e4003e886c27239; identity-state=BAhbBkkiJWI2NDdiOGJlYjY2MjhiNmYzYjFhZmMyM2I1MzViOTJlBjoGRUY%3D--22152f1128c4bddee3fb7efb2dfa1b223f52993b; identity-state-b647b8beb6628b6f3b1afc23b535b92e=BAh7DEkiDnJldHVybi10bwY6BkVUSSI4aHR0cHM6Ly9hbGxhcnRkaXJlY3QubXlzaG9waWZ5LmNvbS9hZG1pbi9hdXRoL2xvZ2luBjsAVEkiEXJlZGlyZWN0LXVyaQY7AFRJIkRodHRwczovL2FsbGFydGRpcmVjdC5teXNob3BpZnkuY29tL2FkbWluL2F1dGgvaWRlbnRpdHkvY2FsbGJhY2sGOwBUSSIQc2Vzc2lvbi1rZXkGOwBUOgxhY2NvdW50SSIPY3JlYXRlZC1hdAY7AFRmFzE2NzU3NDAzOTguNzkyMzk1NEkiCm5vbmNlBjsAVEkiJWVhNTVkNGZjNTEwNzJmNWIyMmM5ZWU5NzlkZjcyYmQ5BjsARkkiCnNjb3BlBjsAVFsPSSIKZW1haWwGOwBUSSI3aHR0cHM6Ly9hcGkuc2hvcGlmeS5jb20vYXV0aC9kZXN0aW5hdGlvbnMucmVhZG9ubHkGOwBUSSILb3BlbmlkBjsAVEkiDHByb2ZpbGUGOwBUSSJOaHR0cHM6Ly9hcGkuc2hvcGlmeS5jb20vYXV0aC9wYXJ0bmVycy5jb2xsYWJvcmF0b3ItcmVsYXRpb25zaGlwcy5yZWFkb25seQY7AFRJIjBodHRwczovL2FwaS5zaG9waWZ5LmNvbS9hdXRoL2JhbmtpbmcubWFuYWdlBjsAVEkiQmh0dHBzOi8vYXBpLnNob3BpZnkuY29tL2F1dGgvbWVyY2hhbnQtc2V0dXAtZGFzaGJvYXJkLmdyYXBocWwGOwBUSSI8aHR0cHM6Ly9hcGkuc2hvcGlmeS5jb20vYXV0aC9zaG9waWZ5LWNoYXQuYWRtaW4uZ3JhcGhxbAY7AFRJIjdodHRwczovL2FwaS5zaG9waWZ5LmNvbS9hdXRoL2Zsb3cud29ya2Zsb3dzLm1hbmFnZQY7AFRJIj5odHRwczovL2FwaS5zaG9waWZ5LmNvbS9hdXRoL29yZ2FuaXphdGlvbi1pZGVudGl0eS5tYW5hZ2UGOwBUSSIPY29uZmlnLWtleQY7AFRJIgxkZWZhdWx0BjsAVA%3D%3D--00bb50f07da10ea2d5629d2d05a827d56d5b756e'
# }

# while True:
#     products = requests.get(f'https://offdutystore.myshopify.com/admin/products.json?since_id={since_id}&limit=250',headers=headers,data={})
#     # print(products.text)
#     products = json.loads(products.text)
#     if not products['products']:
#         break
#     else:
#         for pro in products['products']:
#             since_id = pro['id']
#             if len(pro['images']) == 0:
#                 print(pro['id'])
			# pass
			# do sth
# status = []
# import requests
# import json

# payload={}
# headers = {
#   'x-api-key': '51wipvka0bjm92d4ou0fea0g',
#   'authorization': 'Bearer 849e79b452cb480bb7518df5bc1eac',
#   'Cookie': 'fve=1657784357.0; uaid=4i-I8YmXPg6M78cpQabi6F_sIe5jZACCpBMvnoDo5G2TA6qVShMzU5SslIqj_FMrQo0DssIqMqLMKoIKwsOK0rKdfUqj_F2VahkA; user_prefs=03YFCexFUO2gVqVRmnV-GPe3hkdjZACCpBPP_MD0-ROq0Uphfi5KOnmlOTk6Sql5uqHBSjpAIaiIEYTCRcQyAAA.'
# }

# offset = 0
# while True:
#     url = f'https://openapi.etsy.com/v3/application/shops/20729820/receipts?limit=100&offset={offset}'
#     response = requests.request('GET', url, headers=headers, data=payload)
#     response = json.loads(response.text)
#     if not response['results']:
#         break
#     for order in response['results']:
#         if      order['status'] not in status:
#             status.append(order['status'])
#     offset =offset + 100



# print(status)
# Simple Python program to compare dates
  
# importing datetime module
# import datetime
  
# # date in yyyy/mm/dd format
# d1 = datetime.datetime(2013, 4, 4)
# d2 = datetime.datetime(2022, 1, 1)
  
# # Comparing the dates will return
# # either True or False
# print('d1 is greater than d2 : ', d1 > d2)
# print('d1 is less than d2 : ', d1 < d2)
# print('d1 is not equal to d2 : ', d1 != d2)

# import datetime
# month_name = 'Jan'
# datetime_object = datetime.datetime.strptime(month_name, '%b')
# month_number = datetime_object.month
# print(month_number)

# import requests
# import json
# # from PIL import Image
# import io

# a=requests.get('https://dukaan-core-file-service.s3.ap-southeast-1.amazonaws.com/upload_file_service/7d245801-29fe-40aa-872e-23908754f669/00x-02a1e48e-e170-48bb-9506-ad5f5ec7256e-720x-webp')
# print(a.text)

# image_data = a.text # byte values of the image
# image = Image.open(io.BytesIO(image_data))
# print(image)
# image.show()

# import base64
# with open('my_image.jpg', 'rb') as img_file:
#     my_string = base64.b64encode(img_file.read())
# print(my_string)


# import boto3
# import io
# from PIL import Image

# s3 = boto3.resource('s3')

# # replace 'bucket-name' and 'image-key' with your S3 bucket and key
# obj = s3.Object('bucket-name', 'image-key')

# # read the object as bytes
# image_bytes = obj.get()['Body'].read()

# # create a BytesIO object for the image bytes
# image_file = io.BytesIO(image_bytes)

# # use Pillow (PIL) to open the WebP image
# image = Image.open(image_file)

# # show the image
# image.show()


# import boto3
# from PIL import Image
# import io
# import base64

# # initialize S3 client
# s3 = boto3.client('s3')

# # specify S3 bucket and key for the image
# bucket_name = 'dukaan-core-file-service'
# key = 'https://dukaan-core-file-service.s3.ap-southeast-1.amazonaws.com/upload_file_service/7d245801-29fe-40aa-872e-23908754f669/00x-02a1e48e-e170-48bb-9506-ad5f5ec7256e-720x-webp'

# # download image from S3
# response = s3.get_object(Bucket=bucket_name, Key=key)
# image_content = response['Body'].read()

# # open image and encode to base64
# image = Image.open(io.BytesIO(image_content))
# image_base64 = base64.b64encode(image.tobytes()).decode('utf-8')

# print(image_base64)


# convert binary to base64

# import requests
# import base64

# url = 'https://dukaan-core-file-service.s3.ap-southeast-1.amazonaws.com/upload_file_service/e2b67204-1e0b-4e0d-aced-38d3afcb3d41/KO1O.jpg'

# response = requests.get(url)
# image_bytes = response.content

# base64_bytes = base64.b64encode(image_bytes)
# base64_string = base64_bytes.decode('utf-8')

# print(base64_string)

# import requests
# def is_url_image(image_url):
#    image_formats = ('image/png', 'image/jpeg', 'image/jpg')
#    r = requests.head(image_url)
#    if r.headers['content-type'] in image_formats:
#       return True
#    return False
# print(is_url_image('https://dukaan-core-file-service.s3.ap-southeast-1.amazonaws.com/upload_file_service/e2b67204-1e0b-4e0d-aced-38d3afcb3d41/KO1O.jpg'))   


# from datetime import datetime

# date_str = '31 Jan 2023 11:44 PM'
# date_obj = datetime.strptime(date_str, '%d %b %Y %I:%M %p')
# formatted_date_str = date_obj.strftime('%Y-%m-%d %H:%M:%S')

# print(type(formatted_date_str))

# import requests
# import json
# url = 'https://api.etsy.com/v3/public/oauth/token'# self.log(url,'tk url')
# payload={
#     'grant_type':'refresh_token',
#     'client_id':'jr2r21np87n2dw43c2281nb3',
#     'refresh_token':'353418289.xXjjkBa-wHeT50vN7X72hxzK4-2Bau7Pt-O56Ac587MVgNKZSA-67N0v6qZEd4P2eZhwiX2VtFKKfm9ZZm22Dnz0Jp'
# }
# files=[

# ]
# headers = {
#   'Cookie': 'fve=1657784357.0; uaid=4i-I8YmXPg6M78cpQabi6F_sIe5jZACCpBMvnoDo5G2TA6qVShMzU5SslIqj_FMrQo0DssIqMqLMKoIKwsOK0rKdfUqj_F2VahkA; user_prefs=03YFCexFUO2gVqVRmnV-GPe3hkdjZACCpBPP_MD0-ROq0Uphfi5KOnmlOTk6Sql5uqHBSjpAIaiIEYTCRcQyAAA.'
# }

# response = requests.request('POST', url, headers=headers, data=payload, files=files)
# response = json.loads(response.text)
# print(response)


# order_data['comment_his'].sort(key = lambda x: datetime.strptime(x['date'], '%Y-%m-%d %H:%M:%S'))

# def replacer(s, newstring, index, nofail=False):
#     # raise an error if index is outside of the string
#     if not nofail and index not in range(len(s)):
#         raise ValueError('index outside given string')

#     # if not erroring, but the index is still not in the correct range..
#     if index < 0:  # add it to the beginning
#         return newstring + s
#     if index > len(s):  # add it to the end
#         return s + newstring

#     # insert the new string between 'slices' of the original
#     return s[:index] + newstring + s[index + 1:]

# from collections import OrderedDict
# # a = list('OrderedDict([('address', [OrderedDict([('@address-id', '209117'), ('@preferred', 'True'), ('salutation', None), ('title', None), ('first-name', 'ABDULHAKIM  A ALBAZIE'), ('second-name', None), ('last-name', None), ('suffix', None), ('company-name', None), ('job-title', None), ('address1', 'Al Qassim, Buraydah'), ('address2', 'alhay al'akhdar King Saud Road'), ('suite', None), ('postbox', None), ('city', 'Buraydah'), ('postal-code', '52391'), ('state-code', None), ('country-code', 'SA'), ('phone', '00966544947070')]), OrderedDict([('@address-id', 'Buraydah'), ('@preferred', 'False'), ('salutation', None), ('title', None), ('first-name', 'ABDULHAKIM'), ('second-name', None), ('last-name', 'A ALBAZIE'), ('suffix', None), ('company-name', None), ('job-title', None), ('address1', 'Al Qassim, Buraydah'), ('address2', 'alhay al'akhdar King Saud Road'), ('suite', None), ('postbox', None), ('city', 'Buraydah'), ('postal-code', '52391'), ('state-code', None), ('country-code', 'SA'), ('phone', '096666666666666')])])])')
# a = list('OrderedDict([('salutation', None), ('title', None), ('first-name', 'krishna'), ('second-name', None), ('last-name', 'kishore'), ('suffix', None), ('company-name', None), ('job-title', None), ('email', 'kkishore@pfsweb.com'), ('phone-home', None), ('phone-business', None), ('phone-mobile', None), ('fax', None), ('creation-date', '2016-07-08T09:08:29.000Z'), ('last-login-time', '2018-10-02T08:21:01.000Z'), ('last-visit-time', '2018-10-02T08:21:01.000Z'), ('preferred-locale', None), ('custom-attributes', OrderedDict([('custom-attribute', OrderedDict([('@attribute-id', 'hpProjectData'), ('value', ['{'id':'0307052615','name':'sample','path':'mike','content_context_token':'','state':'IN_CART'}', '{'id':'0307071543','name':'k1','path':'mike','content_context_token':'','state':'IN_CART'}', '{'id':'0307084926','name':'k2','path':'mike','content_context_token':'','state':'IN_CART'}', '{'id':'0307090851','name':'ff','path':'mike','content_context_token':'','state':'IN_CART'}', '{'id':'0307092229','name':'434','path':'mike','content_context_token':'','state':'IN_CART'}', '{'id':'1002082144','name':'kk','path':'mike','content_context_token':'','state':'IN_CART'}'])]))]))])')

# for i in range(len(a)):
#     if a[i] ==''' and a[i+1].isalpha() and a[i-1].isalpha():
#         a[i] = '''
# a = ''.join(a)        
# print(dict(eval(a)))


# for i in range(4,50):
#     if 103 %  i == 0:
#         print(i)
#         break

# import json
# a= '{\'type\':\'root\',\'children\':[{\'type\':\'paragraph\',\'children\':[{\'type\':\'text\',\'value\':\'\'},{\'url\':\'https://www.google.com.vn/\',\'title\':\'google\',\'target\':\'_blank\',\'type\':\'link\',\'children\':[{\'type\':\'text\',\'value\':\'google\'}]},{\'type\':\'text\',\'value\':\'\'}]},{\'type\':\'paragraph\',\'children\':[{\'type\':\'text\',\'value\':\'\'},{\'url\':\'https://www.facebook.com/\',\'title\':\'fb\',\'target\':\'_blank\',\'type\':\'link\',\'children\':[{\'type\':\'text\',\'value\':\'fb\'}]},{\'type\':\'text\',\'value\':\'\'}]}]}'
# a = json.loads(a)
# print(a)
# print('</br>')
# for i in a['children']:
#     print(i)
# a ='{'product-lineitem': [{'net-price': '4.17', 'tax': '0.83', 'gross-price': '5.00', 'base-price': '5.00', 'lineitem-text': 'Ink Duck Egg Ombre Mural Sample Pack', 'tax-basis': '5.00', 'position': '1', 'product-id': '111851SP', 'product-name': 'Ink Duck Egg Ombre Mural Sample Pack', 'quantity': {'@unit': '', '#text': '1.0'}, 'tax-rate': '0.2', 'shipment-id': '02693985', 'shipping-lineitem': {'net-price': '0.00', 'tax': '0.00', 'gross-price': '0.00', 'base-price': '0.00', 'lineitem-text': 'Item Shipping Cost (Fixed Price)', 'tax-basis': '0.00', 'quantity': {'@unit': '', '#text': '1.0'}, 'tax-rate': '0.2', 'type': 'fixed-price'}, 'gift': 'False', 'custom-attributes': {'custom-attribute': [{'@attribute-id': 'isSample', '#text': 'True'}, {'@attribute-id': 'isShipped', '#text': 'True'}]}}, {'net-price': '0.83', 'tax': '0.17', 'gross-price': '1.00', 'base-price': '1.00', 'lineitem-text': 'Candy Apple\xa0Peel & Stick Paint Sample', 'tax-basis': '1.00', 'position': '2', 'product-id': '116864', 'product-name': 'Candy Apple\xa0Peel & Stick Paint Sample', 'quantity': {'@unit': '', '#text': '1.0'}, 'tax-rate': '0.2', 'shipment-id': '02693985', 'shipping-lineitem': {'net-price': '0.00', 'tax': '0.00', 'gross-price': '0.00', 'base-price': '0.00', 'lineitem-text': 'Item Shipping Cost (Fixed Price)', 'tax-basis': '0.00', 'quantity': {'@unit': '', '#text': '1.0'}, 'tax-rate': '0.2', 'type': 'fixed-price'}, 'gift': 'False', 'custom-attributes': {'custom-attribute': [{'@attribute-id': 'EAN', '#text': '5011583504002'}, {'@attribute-id': 'UPC', '#text': '116864'}, {'@attribute-id': 'ct', '#text': 'CT-050-089'}, {'@attribute-id': 'isSample', '#text': 'True'}]}}, {'net-price': '0.83', 'tax': '0.17', 'gross-price': '1.00', 'base-price': '1.00', 'lineitem-text': 'Rowing Boat\xa0Peel & Stick Paint Sample', 'tax-basis': '1.00', 'position': '3', 'product-id': '116728', 'product-name': 'Rowing Boat\xa0Peel & Stick Paint Sample', 'quantity': {'@unit': '', '#text': '1.0'}, 'tax-rate': '0.2', 'shipment-id': '02693985', 'shipping-lineitem': {'net-price': '0.00', 'tax': '0.00', 'gross-price': '0.00', 'base-price': '0.00', 'lineitem-text': 'Item Shipping Cost (Fixed Price)', 'tax-basis': '0.00', 'quantity': {'@unit': '', '#text': '1.0'}, 'tax-rate': '0.2', 'type': 'fixed-price'}, 'gift': 'False', 'custom-attributes': {'custom-attribute': [{'@attribute-id': 'EAN', '#text': '5011583502640'}, {'@attribute-id': 'UPC', '#text': '116728'}, {'@attribute-id': 'ct', '#text': 'CT-060-061'}, {'@attribute-id': 'isSample', '#text': 'True'}]}}, {'net-price': '0.83', 'tax': '0.17', 'gross-price': '1.00', 'base-price': '1.00', 'lineitem-text': 'Chaser\xa0Peel & Stick Paint Sample', 'tax-basis': '1.00', 'position': '4', 'product-id': '116845', 'product-name': 'Chaser\xa0Peel & Stick Paint Sample', 'quantity': {'@unit': '', '#text': '1.0'}, 'tax-rate': '0.2', 'shipment-id': '02693985', 'shipping-lineitem': {'net-price': '0.00', 'tax': '0.00', 'gross-price': '0.00', 'base-price': '0.00', 'lineitem-text': 'Item Shipping Cost (Fixed Price)', 'tax-basis': '0.00', 'quantity': {'@unit': '', '#text': '1.0'}, 'tax-rate': '0.2', 'type': 'fixed-price'}, 'gift': 'False', 'custom-attributes': {'custom-attribute': [{'@attribute-id': 'EAN', '#text': '5011583503814'}, {'@attribute-id': 'UPC', '#text': '116845'}, {'@attribute-id': 'ct', '#text': 'CT-070-068'}, {'@attribute-id': 'isSample', '#text': 'True'}]}}]}'
# import json
# print(json.loads(a))

# a ='Product ID: 0, Product Qty: 1, Product SKU: 1682789197, Product Name: Bearded Butcher Blend Seasoning Variety 4 Pack with Sauce, Product Variation Details: , Product Unit Price: 48.99, Product Unit Cost: 0.00, Product Index: 1, Product Weight: 0.0000, Product Total Price: 48.99, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1|Product ID: 166, Product Qty: 1, Product SKU: 1682781633, Product Name: Victorinox Swiss Army Boning Knife | Bearded Butchers BRANDED Knife, Product Variation Details: , Product Unit Price: 46.99, Product Unit Cost: 0.00, Product Index: 2, Product Weight: 5.0000, Product Total Price: 46.99, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1'
# for i in a.split('|'):
#     # row = i.split(',')
#     # print(row)    
#     # print(i)
#     print(i.split(','))
# string = 'Product ID: 167, Product Qty: 1, Product SKU: 1682781632, Product Name: Bearded Butcher Smokewear Cap (For M, L & XL Big Green Egg), Product Variation Details: , Product Unit Price: 49.95, Product Unit Cost: 0.00, Product Index: 1, Product Weight: 32.0000, Product Total Price: 49.95, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1|Product ID: 178, Product Qty: 1, Product SKU: 1682781619, Product Name: Bearded Butcher Blend Seasoning Original - Single Shaker, Product Variation Details: , Product Unit Price: 10.99, Product Unit Cost: 0.00, Product Index: 2, Product Weight: 6.0000, Product Total Price: 10.99, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1|Product ID: 184, Product Qty: 1, Product SKU: 1682781616, Product Name: Bearded Butcher Blend Seasoning Black - Single Shaker, Product Variation Details: , Product Unit Price: 10.99, Product Unit Cost: 0.00, Product Index: 3, Product Weight: 6.0000, Product Total Price: 10.99, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1|Product ID: 194, Product Qty: 1, Product SKU: 1682900896, Product Name: Bearded Butcher Carnivore Heat and Cut Resistant BBQ Gloves, Product Variation Details: , Product Unit Price: 29.99, Product Unit Cost: 0.00, Product Index: 4, Product Weight: 1.5000, Product Total Price: 29.99, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1|Product ID: 201, Product Qty: 1, Product SKU: 1683004085, Product Name: Victorinox Handheld Knife Sharpener, Product Variation Details: , Product Unit Price: 29.99, Product Unit Cost: 0.00, Product Index: 5, Product Weight: 0.1500, Product Total Price: 29.99, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1|Product ID: 205, Product Qty: 1, Product SKU: 1683264239, Product Name: Bearded Butcher Blend Seasoning Butter Blend - Single Shaker, Product Variation Details: , Product Unit Price: 10.99, Product Unit Cost: 0.00, Product Index: 6, Product Weight: 6.0000, Product Total Price: 10.99, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1|Product ID: 224, Product Qty: 1, Product SKU: 638392100239, Product Name: Bearded Butcher Black Beef Jerky Bites, Product Variation Details: , Product Unit Price: 9.99, Product Unit Cost: 0.00, Product Index: 7, Product Weight: 3.0000, Product Total Price: 9.99, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1'
# string ='Product ID: 167, Product Qty: 1, Product SKU: 1682781632, Product Name: Bearded Butcher Smokewear Cap (For M, L & XL Big Green Egg), Product Variation Details: , Product Unit Price: 49.95, Product Unit Cost: 0.00, Product Index: 1, Product Weight: 32.0000, Product Total Price: 49.95, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1'
# string ='Product ID: 182, Product Qty: 1, Product SKU: 638392000010, Product Name: Hollywood Blend Seasoning, Delicious Flavor, Versatile, Gluten Free, Low Calorie, No MSGASIN : B08F3MJBH9, Product Variation Details: , Product Unit Price: 13.99, Product Unit Cost: 0.00, Product Index: 1, Product Weight: 6.0000, Product Total Price: 13.99, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1|Product ID: 184, Product Qty: 1, Product SKU: 638392000041, Product Name: Black Blend Seasoning, Delicious Flavor, Versatile, Gluten Free, Low Calorie, No MSG
# ASIN : B08F3LVZLH, Product Variation Details: , Product Unit Price: 13.99, Product Unit Cost: 0.00, Product Index: 2, Product Weight: 6.0000, Product Total Price: 13.99, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1'
# string ='Product ID: 0, Product Qty: 1, Product SKU: 3839200217, Product Name: Bearded Butcher 100% Beef Liver Treats for Dogs, Product Variation Details: , Product Unit Price: 8.99, Product Unit Cost: 0.00, Product Index: 1, Product Weight: 0.0000, Product Total Price: 8.99, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1|Product ID: 0, Product Qty: 2, Product SKU: 638392002212, Product Name: Bearded Butchers Pink Curing Salt (Sodium Nitrite) - 1 oz for 25 lb Meat, Product Variation Details: , Product Unit Price: 3.99, Product Unit Cost: 0.00, Product Index: 2, Product Weight: 0.0000, Product Total Price: 7.98, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1|Product ID: 0, Product Qty: 1, Product SKU: 638392002144, Product Name: Bearded Butcher Blend 6 Pack of Beef Jerky Bites and Sticks, Product Variation Details: , Product Unit Price: 49.99, Product Unit Cost: 0.00, Product Index: 3, Product Weight: 0.0000, Product Total Price: 49.99, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1|Product ID: 0, Product Qty: 1, Product SKU: 1682781642, Product Name: Bearded Butcher Hollywood Blend Bulk Seasoning Bucket w/Shaker - Hollywood Bulk Bucket w/shaker, Product Variation Details: , Product Unit Price: 79.99, Product Unit Cost: 0.00, Product Index: 4, Product Weight: 0.0000, Product Total Price: 79.99, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1|Product ID: 167, Product Qty: 1, Product SKU: 1682781632, Product Name: Bearded Butcher Smokewear Cap (For M, L & XL Big Green Egg), Product Variation Details: , Product Unit Price: 49.95, Product Unit Cost: 0.00, Product Index: 5, Product Weight: 32.0000, Product Total Price: 49.95, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1|Product ID: 171, Product Qty: 1, Product SKU: 781648179784, Product Name: Bearded Butcher Blend BBQ Sauce 1/2 Gallon (64 oz.), Product Variation Details: , Product Unit Price: 24.99, Product Unit Cost: 0.00, Product Index: 6, Product Weight: 64.0000, Product Total Price: 24.99, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1|Product ID: 245, Product Qty: 2, Product SKU: bearded-butcher-blend-seasoning-cinnamon-swirl-limited-edition-single-shaker, Product Name: Bearded Butcher Blend Seasoning Cinnamon Swirl **LIMITED EDITION** - Single Shaker, Product Variation Details: , Product Unit Price: 8.99, Product Unit Cost: 0.00, Product Index: 7, Product Weight: 6.0000, Product Total Price: 17.98, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1'
# string ='Product ID: 400, Product Qty: 1, Product SKU: 638392000416, Product Name: Bearded Butcher Brock Lesnar Summer Slam Special, Product Variation Details: BUY 2: Brock Lesnar Blend, GET 1: Brock Lesnar Blend, FREE!: Brock Lesnar Blend, Gift Box? Yes, please include a gift box, Product Unit Price: 23.98, Product Unit Cost: 9.00, Product Index: 1, Product Weight: 31.0000, Product Total Price: 23.98, Product Total Cost: 9.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1'



# string  ='Product ID: 0, Product Qty: 1, Product SKU: 638392179716, Product Name: Bearded Butcher Blend Seasoning Original 6 oz, Product Variation Details: , Product Unit Price: 8.99, Product Unit Cost: 0.00, Product Index: 1, Product Weight: 0.0000, Product Total Price: 8.99, Product Total Cost: 0.00, Peachtree General Ledger Account: , Peachtree Tax Type: 1'
# lst = string.split(',')
# for i in range(len(lst)):
#     if ':' not in lst[i]:
#         lst[i-1]  = lst[i-1] + ';' +lst[i]
#         lst[i] = ''
# lst = [i for i in lst if i]
# string = ','.join(lst)
# string = string.replace('|Product ID','>Product ID')
# lst = []
# for item in string.split('>'):
#     sub_dict = {}
#     for pair in item.split(', '):
#         print(pair.split(': '))
#         sub_dict[pair.split(': ')[0]]= pair.split(': ')[1] 
#     lst.append(sub_dict) 

# for row in lst:
#     print(row)
# import csv
# # my_list = [['Name', 'Age', 'Gender'], ['John', '35', 'Male'], ['Jane', '28', 'Female'], ['Bob', '42', 'Male']]
# my_list =[['Cờ tỷ phú cơ bản', '_Cờ Tỷ Phú - Trò chơi trí tuệ đã có mặ trên 80 quốc gia.</br>_Nằm trong TOP 50 brands yêu thích của các bà mẹ MỸ', 'active', 'Mykingdom Sandbox', 'https://cdn.shopify.com/s/files/1/0739/4692/3309/products/00009_00009_1.jpg?v=1682071034']]
# with open('test.csv', 'w', newline='', encoding='utf8') as file:
#     writer = csv.writer(file)
#     for row in my_list:
#         writer.writerow(row)


# my_list = ['0', '00', '10', '12', '14', '16', '2', '4', '6', '8']
# sorted_list = sorted(my_list, key=lambda x: int(x))
# print(sorted_list)


# import requests
# import json

# # Set up the API endpoint and headers
# api_endpoint = 'https://connect.squareup.com/v2/orders/search'
# headers = {
#     'Authorization': 'Bearer EAAAEOvxFIAozrkmFzigeg7LTul6SEL-eyVr8dl4RIlEBg0LnNFO2KG8e-s6WbXW',
#     'Content-Type': 'application/json',
# }

# # Set up the search parameters
# search_params = {
#     'location_ids': [
#         'L8T4TW0J00R99'
#     ],
#     'query': {
#         'filter': {
#             'states': [
#                 'COMPLETED',
#                 'CANCELED',
#                 'REFUNDED'
#             ]
#         }
#     },
#     'limit': 4
# }

# # Retrieve the first page of orders
# response = requests.post(api_endpoint, headers=headers, json=search_params)
# # Check the status code of the response
# if response.status_code != 200:
#     print('Error retrieving orders:')
#     print(json.dumps(response.json(), indent=4))
# else:
#     orders = response.json()['orders']
#     cursor = response.json()['cursor']
		  

# for order in orders:
#     print(order)



# import requests

# location_id = 'L8T4TW0J00R99'
# access_token = 'EAAAEOvxFIAozrkmFzigeg7LTul6SEL-eyVr8dl4RIlEBg0LnNFO2KG8e-s6WbXW'

# url = f'https://connect.squareup.com/v2/locations/{location_id}/orders'
# headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}

# response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     orders = response.json()['orders']
#     print(orders)
# else:
#     print(f'Error retrieving orders: {response.status_code} - {response.text}')



# # my_list = [['Name', 'Age', 'Gender'], ['John', '35', 'Male'], ['Jane', '28', 'Female'], ['Bob', '42', 'Male']]

# import requests

# # Set up the API endpoint and headers with your access token
# shop_url = 'bestpricenutrition.myshopify.com'
# access_token = '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'
# endpoint = f'https://{shop_url}/admin/api/2023-04/customers.json'
# headers = {'Content-Type': 'application/json', 'X-Shopify-Access-Token': access_token}

# # Make the API request to get the customer with the highest ID
# params = {'limit': 1, 'order': 'id desc'}
# response = requests.get(endpoint, headers=headers, params=params)
# response_data = response.json()
# highest_customer_id = response_data['customers'][0]['id']

# # Use the since_id parameter to retrieve the customers in batches until you reach the 300,000th customer
# batch_size = 250
# num_batches = 1200
# target_customer_id = highest_customer_id - 300000 + 1

# for i in range(num_batches):
#     since_id = target_customer_id + i * batch_size
#     params = {'limit': batch_size, 'since_id': since_id}
#     response = requests.get(endpoint, headers=headers, params=params)
#     response_data = response.json()
#     customers = response_data['customers']
#     if customers:
#         last_customer_id = customers[-1]['id']
#         if last_customer_id >= target_customer_id:
#             print(f'The ID of the 300,000th customer is {last_customer_id}')
#             break
# import re

# regex = r'<p>.*?</p>'

# test_str = '<p><strong>Dimensions:</strong><br />\\r\</br>Outside: H32 W35 D35<br />\\r\</br>Inside: H13 W20.5 D20.5<br />\\r\</br>Seat Height: 19<br />\\r\</br>Arm Height: 29.5</p>\\r\</br>\\r\</br><div><strong>Construction Information:</strong></div>\\r\</br>\\r\</br><div>&bull;<span class=\\\'Apple-tab-span\\\' style=\\\'white-space: pre;\\\'> </span>American made in North Carolina</div>\\r\</br>\\r\</br><div>&bull;<span class=\\\'Apple-tab-span\\\' style=\\\'white-space: pre;\\\'> </span>100% genuine leather </div>\\r\</br>\\r\</br><div>&bull;<span class=\\\'Apple-tab-span\\\' style=\\\'white-space: pre;\\\'> </span>7/8&rdquo; engineered hardwood frame</div>\\r\</br>\\r\</br><div>&bull;<span class=\\\'Apple-tab-span\\\' style=\\\'white-space: pre;\\\'> </span>8-way hand tied construction</div>\\r\</br>\\r\</br><div>&bull;<span class=\\\'Apple-tab-span\\\' style=\\\'white-space: pre;\\\'> </span>Zippers in all seats and backs</div>\\r\</br>\\r\</br><div>&bull;<span class=\\\'Apple-tab-span\\\' style=\\\'white-space: pre;\\\'> </span>Removable seat cushions</div>\\r\</br>\\r\</br><div>&bull;<span class=\\\'Apple-tab-span\\\' style=\\\'white-space: pre;\\\'> </span>Channeled back cushions</div>\\r\</br>\\r\</br><div>&bull;<span class=\\\'Apple-tab-span\\\' style=\\\'white-space: pre;\\\'> </span>Seat cushion options</div>\\r\</br>\\r\</br><div>&bull;<span class=\\\'Apple-tab-span\\\' style=\\\'white-space: pre;\\\'> </span>Manufacture&rsquo;s warranty</div>\\r\</br>\\r\</br><p> </p>\\r\</br>\\r\</br><p> </p>\\r\</br>'

# matches = re.finditer(regex, test_str.replace('\\r','').replace('\</br>',''), re.MULTILINE)

# for matchNum, match in enumerate(matches, start=1):
#     print (match.group())
	

# import re

# string = 'US-MN Rate (6.875%)'

# number = re.search(r'\d+\.\d+', string)

# if number:
#     print(number.group())
# else:
#     print('No number found in the string')



# import requests
# import json
# url = 'https://apirest.3dcart.com/3dCartWebAPI/v2/OrderStatus?limit=100&offset=0&countonly=0'

# payload = {}
# headers = {
#   'Content-Type': 'application/json; charset=UTF-8',
#   'Accept': 'application/json',
#   'SecureUrl': 'https://www.tegstools.com/',
#   'PrivateKey': '3024382a677d8e48464dfacf9c80a566',
#   'Token': '034f47f6f8b38a937d7a331527732889'
# }

# response = requests.request('GET', url, headers=headers, data=payload)

# for row in json.loads(response.text):
#     print(str(row['OrderStatusID'])+':'+row['StatusText'])
# convert binary to base64

# import requests
# import base64

# url = 'https://img1.wsimg.com//isteam//ip//1fefdd0e-9062-4d3e-bc79-61e1734e2cfd//ols//PHOTO-2020-10-02-00-20-34.jpg'

# response = requests.get(url)
# image_bytes = response.content

# base64_bytes = base64.b64encode(image_bytes)
# base64_string = base64_bytes.decode('utf-8')

# print(base64_string)
# from bs4 import BeautifulSoup

# def strip_html(text):
#     soup = BeautifulSoup(text, 'html.parser')
#     return soup.get_text()

# # example usage
# html_text = '<div data-content-type=\'html\' data-appearance=\'default\' data-element=\'main\'>&lt;h2&gt;Square D BDA260302 2 Pole Circuit Breaker&lt;/h2&gt;\r</br>\r</br>&lt;p&gt;The Square D BDA260302 is a 2 Pole thermal magnetic molded case circuit breaker with a current rating of 30 Amps and a voltage rating of 600Y/347VAC. It has an interrupting rating of 18kAIC at 480V. The BDA260302 has an I-line style plug-in connection type and includes long time and instantaneous trip functions.&lt;/p&gt;\r</br>\r</br>&lt;p class=”indent”&gt;&lt;b&gt;Specifications :&lt;/b&gt;\r</br>&lt;br /&gt;&amp;#149; Series: BDA\r</br>&lt;br /&gt;&amp;#149; Amperage: 30\r</br>&lt;br /&gt;&amp;#149; Poles: 2\r</br>&lt;br /&gt;&amp;#149; GTIN: 3606481152107\r</br>&lt;br /&gt;&amp;#149; MPN: BDA260302\r</br>&lt;br /&gt;&amp;#149; Voltage: 600Y/347VAC\r</br>&lt;br /&gt;&amp;#149; Phase: 1\r</br>&lt;br /&gt;&amp;#149; Frame Type: BDA\r</br>&lt;br /&gt;&amp;#149; Connection Type: I-Line Style Plug-In\r</br>&lt;br /&gt;&amp;#149; Functions: Long Time and Instantaneous Trip\r</br>&lt;br /&gt;&amp;#149; Protection: Thermal Magnetic\r</br>&lt;br /&gt;&amp;#149; Application: Reverse Fed\r</br>&lt;br /&gt;&amp;#149; Terminal Connection: Line and Load Side Lug\r</br>&lt;br /&gt;&amp;#149; Wire Gauge: AWG 14 to AWG 2/0, Aluminum/Copper\r</br>&lt;br /&gt;&amp;#149; Actuator Type: Toggle\r</br>&lt;br /&gt;&amp;#149; Color: Gray\r</br>&lt;br /&gt;&amp;#149; Interrupting Rating: 18kAIC at 480V\r</br>&lt;br /&gt;&amp;#149; Size: 5.39\'H x 2.13\'W x 3.50\'D\r</br>&lt;br /&gt;&amp;#149; Approval: CE, UL, GB, NEMA, EN/IEC, CSA, NMX, CCC, EAC, NOM, RoHS\r</br>&lt;br /&gt;&amp;#149; Standards: RoHS\r</br>&lt;/p&gt;</div>'
# plain_text = strip_html(html_text)
# print(plain_text)
# import requests
# import json
# for i in range(1,21):
#     url = f'https://amethyst-fiddle-6hd6.squarespace.com/api/content-collections?type={i}&limit=100&start='

#     payload = {}
#     headers = {
#       'cookie': 'SS_ANALYTICS_ID=4603544e-9227-4e7b-b283-9cc9d2005ab3; notice_behavior=none; _gcl_au=1.1.1604070085.1685465423; _fbp=fb.1.1685500033460.512022961; _gid=GA1.2.912351478.1685500034; _clck=kw5jdd|2|fc2|0|1246; SS_SESSION_ID=93c05f53-9b78-474e-9121-ca9a9f5dbb8e; IR_gbd=squarespace.com; _clsk=6ro7um|1685500798739|3|1|r.clarity.ms/collect; _ga_CQVWFGJ7WD=GS1.1.1685500031.1.1.1685500803.0.0.0; member-session=1|WXtG/ODBfBN7un7pEBTYaVWxivu/7yrLQfAQtMwKS3v5|sOT7mSuMRlIXgFQhBQSRZ5BJx5QfNj0cF6MD1zg4LNI=; crumb=3NvIpydY1jx36bDIOtwR7cQtTU/iwZC7ksA05GCrCujX; _ga=GA1.1.1694205025.1685465423; seerses=e; seerid=03cc2abe-8577-48f6-93a5-cb4ad51c537d; __stripe_mid=f55e4fbf-42c4-46d1-a458-5c44e1325d686646ec; __stripe_sid=4d30a118-b896-49d0-935c-cf1282fcda8e6c8c0a; ss_lastid=eyJpZGVudGlmaWVyIjoiYW1ldGh5c3QtZmlkZGxlLTZoZDYifQ%3D%3D; IR_9084=1685507402155%7C0%7C1685507402155%7C%7C; _ga_1L8CXRNJCG=GS1.1.1685507027.3.1.1685507402.5.0.0; _uetsid=12fdc3b0ff0a11ed8f6933f567401759; _uetvid=12fe1af0ff0a11ed8d485da51fbfe54b',
#       'x-csrf-token': 'efoAlCN5MSTFEl05pRcGlSwXuHlyvG1+Dl1Gl/gQ5U6B',
#       'content-type': 'application/json',
#       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
#     }

#     response = requests.request('GET', url, headers=headers, data=payload)
#     if 'CHPO' in response.text:
#         print(response.text)



# html_code = '<div data-content-type='html' data-appearance='default' data-element='main'></br><h2>Square D BDA260302 2 Pole Circuit Breaker</h2></br><p>The Square D BDA260302 is a 2 Pole thermal magnetic molded case circuit breaker with a current rating of 30 Amps and a voltage rating of 600Y/347VAC. It has an interrupting rating of 18kAIC at 480V. The BDA260302 has an I-line style plug-in connection type and includes long time and instantaneous trip functions.</p></br><p class='”indent”'><b>Specifications :</b> <br> Series: BDA <br> Amperage: 30 <br> Poles: 2 <br> GTIN: 3606481152107 <br> MPN: BDA260302 <br> Voltage: 600Y/347VAC <br> Phase: 1 <br> Frame Type: BDA <br> Connection Type: I-Line Style Plug-In <br> Functions: Long Time and Instantaneous Trip <br> Protection: Thermal Magnetic <br> Application: Reverse Fed <br> Terminal Connection: Line and Load Side Lug <br> Wire Gauge: AWG 14 to AWG 2/0, Aluminum/Copper <br> Actuator Type: Toggle <br> Color: Gray <br> Interrupting Rating: 18kAIC at 480V <br> Size: 5.39'H x 2.13'W x 3.50'D <br> Approval: CE, UL, GB, NEMA, EN/IEC, CSA, NMX, CCC, EAC, NOM, RoHS <br> Standards: RoHS</p></br></div>'

# # Find the index of the string 'SPECIFICATION' in the HTML code
# index = html_code.find('SPECIFICATION')

# # If the string is found, extract the substring up to that point
# if index != -1:
#     html_code = html_code[:index]

# # Print the modified HTML code
# print(html_code)
# a ='\r</br>\r</br>The Square D BDA260302 is a 2 Pole thermal magnetic molded case circuit breaker with a current rating of 30 Amps and a voltage rating of 600Y/347VAC. It has an interrupting rating of 18kAIC at 480V. The BDA260302 has an I-line style plug-in connection type and includes long time and instantaneous trip functions.\r</br>\r</br>Specifications :\r</br>• Series: BDA\r</br>• Amperage: 30\r</br>• Poles: 2\r</br>• GTIN: 3606481152107\r</br>• MPN: BDA260302\r</br>• Voltage: 600Y/347VAC\r</br>• Phase: 1\r</br>• Frame Type: BDA\r</br>• Connection Type: I-Line Style Plug-In\r</br>• Functions: Long Time and Instantaneous Trip\r</br>• Protection: Thermal Magnetic\r</br>• Application: Reverse Fed\r</br>• Terminal Connection: Line and Load Side Lug\r</br>• Wire Gauge: AWG 14 to AWG 2/0, Aluminum/Copper\r</br>• Actuator Type: Toggle\r</br>• Color: Gray\r</br>• Interrupting Rating: 18kAIC at 480V\r</br>• Size: 5.39\'H x 2.13\'W x 3.50\'D\r</br>• Approval: CE, UL, GB, NEMA, EN/IEC, CSA, NMX, CCC, EAC, NOM, RoHS\r</br>• Standards: RoHS\r</br>'
# print(a.replace('\\r','').replace('\</br>',''))
# import re
# regex = r'\[.*?\]'
# test_str = ('<p>[et_pb_section fb_built=&#8221;1&#8243; module_id=&#8221;sticky&#8221; _builder_version=&#8221;4.3.2&#8243; background_color=&#8221;#ede7e0&#8243; positioning=&#8221;fixed&#8221; position_origin_f=&#8221;top_center&#8221; vertical_offset=&#8221;80px&#8221; z_index=&#8221;99998&#8243; vertical_offset_tablet=&#8221;0px&#8221; vertical_offset_phone=&#8221;&#8221; vertical_offset_last_edited=&#8221;on|phone&#8221; position_origin_a_tablet=&#8221;top_center&#8221; position_origin_a_phone=&#8221;&#8221; position_origin_a_last_edited=&#8221;on|desktop&#8221; position_origin_f_tablet=&#8221;&#8221; position_origin_f_phone=&#8221;&#8221; position_origin_f_last_edited=&#8221;on|tablet&#8221; position_origin_r_tablet=&#8221;&#8221; position_origin_r_phone=&#8221;&#8221; position_origin_r_last_edited=&#8221;on|desktop&#8221; width_tablet=&#8221;100%&#8221; width_phone=&#8221;&#8221; width_last_edited=&#8221;on|tablet&#8221; custom_margin_tablet=&#8221;&#8221; custom_margin_phone=&#8221;&#8221; custom_margin_last_edited=&#8221;on|tablet&#8221; custom_padding=&#8221;0px||0px||True|False&#8221; positioning_tablet=&#8221;none&#8221; positioning_phone=&#8221;none&#8221; positioning_last_edited=&#8221;on|desktop&#8221; saved_tabs=&#8221;all&#8221; positioning__hover_enabled=&#8221;off|desktop&#8221; position_origin_a__hover_enabled=&#8221;off|desktop&#8221; position_origin_f__hover_enabled=&#8221;off|desktop&#8221; position_origin_r__hover_enabled=&#8221;off|desktop&#8221;][et_pb_row _builder_version=&#8221;4.3.2&#8243; width=&#8221;100%&#8221; max_width=&#8221;1245px&#8221; custom_padding=&#8221;0px||0px||True|False&#8221;][et_pb_column type=&#8221;4_4&#8243; _builder_version=&#8221;4.3.2&#8243;][et_pb_slider show_arrows=&#8221;off&#8221; show_pagination=&#8221;off&#8221; _builder_version=&#8221;4.3.2&#8243; body_font=&#8221;Questrial|600|||||||&#8221; body_font_size=&#8221;13px&#8221; body_letter_spacing=&#8221;1px&#8221; background_color=&#8221;#ede7e0&#8243; custom_padding=&#8221;0px||0px||True|False&#8221; animation_direction=&#8221;right&#8221; auto=&#8221;on&#8221; auto_speed=&#8221;3000&#8243;][et_pb_slide _builder_version=&#8221;4.3.2&#8243; header_text_color=&#8221;#000000&#8243; body_text_color=&#8221;#000000&#8243; background_color=&#8221;#ede7e0&#8243; background_enable_color=&#8221;on&#8221; background_layout=&#8221;light&#8221; custom_padding=&#8221;10px||10px||True|False&#8221;]</p></br><p>&#8211; 2 years warranty &#8211;</p></br><p>[/et_pb_slide][et_pb_slide _builder_version=&#8221;4.3.2&#8243; header_text_color=&#8221;#000000&#8243; body_text_color=&#8221;#000000&#8243; background_color=&#8221;#ede7e0&#8243; background_enable_color=&#8221;on&#8221; background_layout=&#8221;light&#8221; custom_padding=&#8221;10px||10px||True|False&#8221;]</p></br><p>&#8211; 60 days return period &#8211;</p></br><p>[/et_pb_slide][et_pb_slide _builder_version=&#8221;4.3.2&#8243; header_text_color=&#8221;#000000&#8243; body_text_color=&#8221;#000000&#8243; background_color=&#8221;#ede7e0&#8243; background_enable_color=&#8221;on&#8221; background_layout=&#8221;light&#8221; custom_padding=&#8221;10px||10px||True|False&#8221;]</p></br><p>&#8211; Free shipping in NL &#8211;</p></br><p>[/et_pb_slide][/et_pb_slider][/et_pb_column][/et_pb_row][/et_pb_section][et_pb_section fb_built=&#8221;1&#8243; _builder_version=&#8221;4.3.2&#8243; custom_padding=&#8221;0px||0px||True|False&#8221;][et_pb_row column_structure=&#8221;2_5,3_5&#8243; use_custom_gutter=&#8221;on&#8221; gutter_width=&#8221;1&#8243; _builder_version=&#8221;4.3.2&#8243; width=&#8221;100%&#8221; max_width=&#8221;100%&#8221; custom_padding=&#8221;0px||0px||True|False&#8221; custom_css_main_element_last_edited=&#8221;on|phone&#8221; custom_css_main_element_phone=&#8221;display: flex;||flex-wrap: wrap;&#8221;][et_pb_column type=&#8221;2_5&#8243; _builder_version=&#8221;4.3.2&#8243; custom_padding=&#8221;150px|50px|0px|50px|False|True&#8221; custom_padding_tablet=&#8221;&#8221; custom_padding_phone=&#8221;106px||100px||False|False&#8221; custom_padding_last_edited=&#8221;on|desktop&#8221; custom_css_main_element_last_edited=&#8221;on|phone&#8221; custom_css_main_element_phone=&#8221;order: 2;&#8221;][et_pb_text _builder_version=&#8221;4.3.2&#8243; text_font=&#8221;Day roman||||||||&#8221; header_3_font=&#8221;Day roman||||||||&#8221; header_3_text_align=&#8221;center&#8221; header_3_text_color=&#8221;#000000&#8243; header_3_font_size=&#8221;45px&#8221; header_3_line_height=&#8221;1.4em&#8221; hover_enabled=&#8221;0&#8243; header_3_font_size_tablet=&#8221;&#8221; header_3_font_size_phone=&#8221;30px&#8221; header_3_font_size_last_edited=&#8221;on|phone&#8221;]</p></br><p>&nbsp;</p></br><p>&nbsp;</p></br><p>&nbsp;</p></br><p>&nbsp;</p></br><p>Qoppel is a Dutch design brand born from a passion for design and natural materials.</p></br><p>It is our goal to design modern and functional interior accessories that you can enjoy for a long time. We do this together with a team of experienced designers and craftsmen. Everything we create is done with attention to detail.</p></br><p>We strongly believe that good design is where function and beauty come together. In addition, good design should make you feel comfortable.</p></br><p>By using mainly natural materials and working according to our values, we can create unique products that last a lifetime. We hope you enjoy them as much as we do.</p></br><p>[/et_pb_text][/et_pb_column][et_pb_column type=&#8221;3_5&#8243; _builder_version=&#8221;4.3.2&#8243; custom_css_main_element_last_edited=&#8221;on|phone&#8221; custom_css_main_element_phone=&#8221;order: 1;&#8221;][et_pb_image src=&#8221;https://qoppel.com/wp-content/uploads/2022/03/DSC7057-scaled.jpg&#8221; url=&#8221;https://qoppel.com/product/bookstand-travertine-jep/&#8221; _builder_version=&#8221;4.3.2&#8243;][/et_pb_image][/et_pb_column][/et_pb_row][/et_pb_section]</p></br>')
# subst = ''
# # You can manually specify the number of replacements by changing the 4th argument
# result = re.sub(regex, subst, test_str, 0, re.MULTILINE)
# if result:
#     print (result)

# import re

# string = '''Buttons / Metal Pins->1' Buttons (97)'''

# # Replace non-alphanumeric characters with commas
# string = re.sub(r'[^a-zA-Z\s\']+', ',', string)

# print(string)  # Output: Hello,This,is,a,test,string,with,special,characters

# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/hello')
# def hello():
#     return jsonify({'message': 'Hello, World!'})

# if __name__ == '__main__':
#     app.run(debug=True)
#     
# a={'Size':'bfau-pr.dimentions', 'Product Blurb':'bfau-pr.short-desc', 'Product Snapshot':'Default Product Description', 'Cooling':'bfau-pr.cooling', 'Location & Suitability':'bfau-pr.suitability', 'Power Consumptions':'bfau-pr.power-consumption', 'Running Cost':'bfau-pr.running-cost', 'Noise Level':'bfau-pr.noise-level', 'Brand Parts Used':'bfau-pr.brand-parts-used', 'Weight':'bfau-pr.weight', 'Tasty Information':'bfau-pr.tasty_information', 'Energy Saving Feature':'bfau-pr.energy-savings', 'Adjustable Feet':'bfau-pr.adjustable-feet', 'Lockable':'bfau-pr.lockable', 'Glass Door Information':'bfau-pr.glass-door-info', 'Door Hinged':'bfau-pr.door-hinged', 'Shelvings':'bfau-pr.shelvings', 'Body Colour':'bfau-pr.body-colour', 'Door / Grill Finish':'bfau-pr.door-finish', 'Interior Finish':'bfau-pr.interior-finish', 'Model Code':'bfau-pr.model-code', 'Brand Information':'bfau-pr.brand-info', 'Approvals':'bfau-pr.approvals', 'Litres':'bfau-pr.capacity-litres', 'Corona Bottle':'bfau-pr.capacity-corona', 'Standard 375ml Cans':'bfau-pr.capacity-375ml-cans', 'Standard Wine Bottles':'bfau-pr.capacity-wine-bottles', 'Shelvings':'bfau-pr.sheving', 'Width':'bfau-pr.ex-width', 'Depth':'bfau-pr.ex-depth', 'Height':'bfau-pr.ex-height', 'Width':'bfau-pr.in-width', 'Depth':'bfau-pr.in-depth', 'Height':'bfau-pr.in-height', 'Width':'bfau-pr.cd-width', 'Depth':'bfau-pr.cd-depth', 'Height':'bfau-pr.cd-height', 'Each Side':'bfau-pr.mv-each-side', 'Rear':'bfau-pr.mv-rear', 'Top':'bfau-pr.mv-top', 'Other Size Information':'bfau-pr.size-info', 'Brochure':'bfau-pr-pdf.brochure', 'Warranty information':'bfau-pr-pdf.warranty', 'Stainless steel care guide':'bfau-pr-pdf.steel-care-guide', 'Fridges and sunlight':'bfau-pr-pdf.sunlight', 'Product Video':'bfau-pr.video', 'Suitability':'bfau-pr.suitability-info'}        
# for key in a:
#     print(key)
# a={'Cooling Info':'cooling','Suitability':'suitability','Power Consumption':'power-consumption','Energy Saving Features':'energy-savings','Colour Body Finish':'body-colour',"*Interior":"dimentions", "Product Blurb":"short-desc", "Product Snapshot":"Default Product Description", "Cooling":"cooling", "Location & Suitability":"suitability", "Power Consumptions":"power-consumption", "Running Cost":"running-cost", "Noise Level":"noise-level", "Brand Parts Used":"brand-parts-used", "Weight":"weight", "Tasty Information":"tasty_information", "Energy Saving Feature":"energy-savings", "Adjustable Feet":"adjustable-feet", "Lockable":"lockable", "Glass Door Information":"glass-door-info", "Door Hinged":"door-hinged", "Shelvings":"shelvings", "Body Colour":"body-colour", "Door / Grill Finish":"door-finish", "Interior Finish":"interior-finish", "Model Code":"model-code", "Brand Information":"brand-info", "Approvals":"approvals", "Litres (Gross)":"capacity-litres", "Corona Bottle":"capacity-corona", "Standard 375ml Cans":"capacity-375ml-cans", "Standard Wine Bottles":"capacity-wine-bottles", "Shelvings":"sheving", "Width":"ex-width", "Depth":"ex-depth", "Height":"ex-height", "Width":"in-width", "Depth":"in-depth", "Height":"in-height", "Width":"cd-width", "Depth":"cd-depth", "Height":"cd-height", "Each Side":"mv-each-side", "Rear":"mv-rear", "Top":"mv-top", "Other Size Information":"size-info", "Brochure":"bfau-pr-pdf.brochure", "Warranty information":"bfau-pr-pdf.warranty", "Stainless steel care guide":"bfau-pr-pdf.steel-care-guide", "Fridges and sunlight":"bfau-pr-pdf.sunlight", "Product Video":"video", "Suitability":"suitability-info"}        
# for key in a:
#     print(a[key])

# def remove_accents(input_str):
#     s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
#     s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'    
#     s = ''
#     for c in input_str:
#         if c in s1:
#             s += s0[s1.index(c)]
#         else:
#             s += c
#     return s
# remove_accents('Từ 3-6 tuổi')    


# import mysql.connector

# mydb = mysql.connector.connect(
#   host="45.33.0.186",
#   user="root",
#   password="LeCM$123Mysql",
#   database="jay_198892",
#   port="3306",
#   connect_timeout=120
  
# )

# lst = ['Iron Maiden', 'Queen', 'Live Aid', 'Slayer', 'Humble Pie', 'Chuck Berry', 'Procol Harum', 'Elton John', 'Grateful Dead', 'Cold Blood', 'Mike Bloomfield', 'Fleetwood Mac', 'Elvin Bishop', 'Jethro Tull', 'Black Sabbath', 'Van Morrison', 'Ten Years After', 'Steve Miller Band', 'Jefferson Airplane', 'Chicago', 'David Bowie', 'Neil Diamond', 'Simon and Garfunkel', 'Staind', 'INXS', 'Linkin Park', 'Stereophonics', 'Yes', 'Brand', 'Will Young', 'Westlife', 'Led Zeppelin', 'Country Joe And The Fish', 'Dana', 'Midge Ure', 'The Goon Show', "Hazel O'Connor", 'Big Brother', 'Johnny Mathis', 'David Essex', 'Jools Holland', "Gilbert O'Sullivan", 'Acker Bilk', 'Joe Brown', 'Gloria Gaynor', 'Dustin Hoffman', 'Dave Berry', 'Chris De Burgh', 'Kylie Minogue', 'Filmore', 'Barbara Dickson', 'Lisa Stansfield', 'Bonnie Tyler', 'Alfie Boe', 'Chris Montez', 'Charley Pride', 'Eden Kane', 'Jessie Ware', 'Christy Moore', 'John Leyton', "Daniel O'Donnell", 'Paul Carrack', 'Jack Jones', 'Mark Wynter', 'Jess Conrad', 'Def Leppard', 'Max Bygraves', 'Tom Paxton', 'Michael Bolton', 'John Mayall', 'Boney M', 'Spirit', 'Tim Curry', 'U2', 'Brinsley Schwarz', 'The Eagles', 'Paul Young', 'Gladys Knight', 'Ted Nugent', 'War', 'The Floaters', 'CCS', 'Gap Band', 'Marillion', 'Curiosity Killed The Cat', 'Leapy Lee', 'Sting', 'Steve Winwood', 'John Alderton', 'Little River Band', 'Fizz', 'Gordon Lightfoot', 'Fairport Convention', 'Michael Jackson', 'Hawkwind', 'The Christians', 'Deep Purple', 'Waysted', 'John Glover', 'Sex Pistols', 'Limp Bizkit', 'McGuinness', 'Re-Flex', 'The Damned', 'UFO', 'The Offspring', 'Alien Sex Fiend', 'James Taylor', 'Ozzy Osbourne', 'Peter Skellern', 'Slade', "Guns n' Roses", 'Oasis', 'Dwayne Johnson', 'James', 'S Club 7', 'Blue', 'Alice Cooper', 'George Michael', 'Take That', 'Billy Connolly', '311', 'Christina Aguilera', 'Busted', 'Tina Turner', 'Jason Donovan', 'Donny Osmond', 'Coldplay', "Hear'Say", 'Genesis', 'Travis', 'Emma Bunting', 'Slipknott', 'Bad Company', 'KISS', 'Thin Lizzy', 'Rainbow', 'AC DC', 'ZZ Top', 'Incubus', 'Blue Murder', 'Boston', 'Eric Clapton', 'Pink Floyd', 'Ash', 'Meatloaf', 'Gary Moore', 'WASP', 'Thunder', 'Dio', 'Motorhead', 'Status Quo', 'MSG', 'Foeigner', 'Aerosmith', 'Scorpions', 'Krokus', 'Captain Beefheart', 'Suede', 'The Wombats', 'Phantom of the Opera', 'The Vaccines', 'The Pineapple Thief', 'Slaughter', 'Brenda Lee', 'Pet Shop Boys', 'Jah Wobble', 'Guns N Roses', 'Buddy Holly', 'Depeche Mode', 'Bebe Buell', 'Judas Priest', 'Whitesnake', 'The Beatles', 'Nirvana', 'Nightwish', 'T-Rex', 'Queensryche', 'Lindisfarne', 'DC', 'The Police', 'Marti Pellow', 'Ms Dynamite', 'Unbranded', 'MC Lars', 'Scouting For Girls', 'Cliff Richard', 'LULU', 'The Tubes', 'The Who', 'Gillan', 'ELO', 'Small Faces', 'The Shadows', 'Steve Harley & Cockney Rebel', 'Gary Numan', 'Be-Bop Deluxe', 'Lynyrd Skynyrd', 'Eddie and the Hot Rods', 'The Darkness', 'Gloria Estefan', 'Velvet Revolver', 'Foreigner', 'ELP', 'SAHB', 'Rolling Stones', 'Dire Straits', 'Uriah Heap', 'EMI', 'Cookaway Music Limited', '2 Tribes', 'Quireboys', 'David Sylvian', 'Terrorvision', 'Chumbawamba', 'Simple Minds', 'The Wedding Present', 'The The', 'Elastica', 'Peter Gabriel', 'Anndore', 'Big O', 'Trooper', 'Be Bop Deluxe', 'Undertones', 'Rough Trade', 'Tori Amos', 'Gang Of Four', 'Franz Ferdinand', 'Neil Young', 'Focus', 'Budgie', 'Yello', 'A Band Called O', 'Raw Power', 'Jack Lancaster', 'Lightning Seeds', 'Zimmers Hole', 'Miley Cyrus', 'Neville Garrick', 'David Gates', 'Dumpys Rusty Nuts', 'Big Pig Music', 'Tampasm', 'Hothouse Flowers', 'Three Dog Night', '1910 Fruitgum Company', 'Talking Heads', 'Pulp', 'Black Rebel Motorcycle Club', 'Keel', 'Danbury Mint', 'Bananarama', 'Howard Jones', 'Mega City Four', 'Paul Hague', 'Information Society', 'Betty Buckley', 'Barbra Streisand', 'The Proclaimers', 'Blue Brothers', 'Fish', 'Sadista Sisters', 'HongKong Syndikat', 'Seal', 'Anthrax', 'Alvin Stardust', 'Culture Club', 'ABBA', 'Eddit Rabbitt', 'Alfalfa', 'Indecent Obsession', 'Diana Ross', 'Brian Ferry', 'House of Love', 'Bon Jovi', 'Engelbert Humperdinck', 'Mary Wilson', 'Kevin Saunderson', 'David Soul', 'Alison Moyet', 'Val Doonican', 'Toyah Willcox', 'Toyah Wilcox', 'Rick Astley', 'Steve Hackett', 'Madonna', 'Swinging Blue Jeans', 'Tony Christie', 'Ozzy', 'Russel Watson', 'Bob Dylan', 'Lemmy', 'Yargo', 'The Flying Pickets', 'Melissa Manchester', 'Frankie', 'Potato 5', 'Love Jungle', 'Lies Damned Lies', 'Andy Sheppard', 'Comsat Angels', 'Kirsty MacColl', 'Weddings, Parties, Anything', 'Bad Manners', 'Meat Loaf', 'Hue and Cry', 'Kalima', 'Julie Birchill', 'The Oyster Band', 'Yazz', 'Sydney Youngblood', 'The Beat', 'Sade', 'Bono', 'Tony Orlando', 'Marquee', 'Cream', 'Bowie', 'Four Tops', 'Mott The Hoople', 'Kylie', 'Ricky Nelson', 'Boomtown Rats', 'Van Halen', 'Faster Pussycat', 'Chelsea', 'Colosseum', 'Nitin Sawhney', 'Happy Mondays', 'Bonzo Dog', 'Herbie Hancock', 'Tom Jones', 'Boyzone', 'Flyer', 'Britney Spears', 'Andrea Bocelli', 'Mel B', 'Sum 41', 'Spandau Ballet', 'Ian Hunter And Mick Ronson', 'David Coverdale', '10CC', 'Sgt. Peppers Lonely Hearts Club', 'Wishbone Ash', 'Girl', 'Pentangle', 'Jeff Wayne', 'The Kinks', 'Manfred Mann', 'Jeff Beck', 'Stone Temple Pilots', 'Twisted Sister', 'The Mekons', 'NEeMA', 'Argent', 'Go! Discs', 'Abbey Road', 'Vanderquest', 'Parlophone', 'Loudon Wainwright', 'The Fall', 'The Pogues', 'D C Thompson', 'RZO Productions', 'Bloomsbury Publishing', 'Warren G', 'Crosby Stills', 'David Gray', 'Steve Miller', 'Michele Records', 'RCA', 'Santana', 'Jimi Hendrix']
# mycursor = mydb.cursor()

# mycursor.execute('SELECT distinct(secondary_store_category) FROM `relics_in_rock_custom_export` where     secondary_store_category is not null ')

# myresult = mycursor.fetchall()

# for x in myresult:
#     if x[0].split('/')[-1] not in lst:
#         lst.append(x[0].split('/')[-1])        
#     # cate =  x[0].split('/')
#     # cate = [item.strip() for item in cate if item.strip()][0]
#     # if cate not in lst:
#     #     lst.append(cate)
#   # print(x[0])
#   # if x[0].split('/')[0] not in lst and x[0].split('/')[0] :
#   #   lst.append(x[0].split('/')[0])        
# print(lst)



######################################


# from bs4 import BeautifulSoup

# def strip_html(html):
#     soup = BeautifulSoup(html, "html.parser")
#     return soup.get_text()


# html_string = '''<p>Die neue Shampoo-Creme ist eine Mischung aus flüssig und fest.</p>

# <p>Seine konzentrierte Formel sorgt für DREImal so viele Haarwäschen wie ein flüssiges Shampoo!&nbsp;</p>

# <p>&nbsp;</p>

# <p>Das vegane&nbsp;Shampoo für alle Haartypen geeignet. Aufgrund der sorgfältig zusammengestellten Formel wirkt es besonders sanft zum Haar und ist sehr mild zu Haut und Augen. Es funktioniert auch gut in weichem und hartem Wasser.</p>

# <p>&nbsp;</p>

# <p>Geeignet für Afro-Haare, coloriertes Haar, trockenes und fettiges Haar.</p>

# <p>&nbsp;</p>

# <p>Duft: Frischer, herber, sportlicher Duft (unisex).</p>

# 2023/06/20 14:48:45 : <p>Recycelbare Kartonschachtel,&nbsp;Glasbehälter mit Aluminiumdeckel</p>

# 2023/06/20 14:48:45 : <p>100 % NATÜRLICHE ZUTATEN:</p>

# <p>Natriummethylcocoyltaurat, Natriumcocoylisethionat, Aqua, Cocos Nucifera (Kokosnuss) Fruchtöl, Rosmarinus Officinalis (Rosmarin) Blattöl, Schinus Terebinthifolia Samenextrakt, Mentha Piperita (Pfefferminze) Blattöl, Citrus Grandis (Grapefruit) Schalenöl, Lavandula Angustifolia (Lavendel) Blütenöl, Cedrus Atlantica (Zedernholz) Rindenöl, Eugenia Caryophyllus (Nelke) Blütenöl, Glycerylcaprylat, Natriumlevulinat, Natriumanisat, Maltodextrin, Limonen*, Linalool*.</p>

# <p><br>
# *Natürlicher Bestandteil der aufgeführten ätherischen Öle.</p> '''
# stripped_text = strip_html(html_string)
# print(stripped_text)
# import decimal

# num = decimal.Decimal('8.244')
# rounded_num = num.quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_HALF_UP)
# print(rounded_num)
# import requests

# url = "https://api.lightspeedapp.com/API/V3/Account/256785/Item.json"

# payload = {}
# headers = {
#   'Authorization': 'Bearer a57d8f84788e86b1bc84eb0aa10d389f82b8cf57'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup

# url = 'https://www.pop-gateway.com/page-zslS44?store-page=Aaa-New-Damaged-Template-NEW-WITH-BOX-DAMAGE-p544549357'

# # Use headless Chrome browser
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# # Load the URL and wait for page to load
# driver.get(url)
# driver.implicitly_wait(10)

# # Get the page source and parse using BeautifulSoup
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# images = soup.find_all('img')

# for img in images:
#     print(img['src'])

# # Close the browser
# driver.quit()


# import requests
# import json

# # Set up API endpoint and parameters
# url = 'https://api.zyro.com/v1/products'
# params = {
#     'status': 'all',
#     'limit': 40
# }

# # Set up headers with your API key
# headers = {
#     'Authorization': 'Bearer YOUR_API_KEY',
#     'Content-Type': 'application/json'
# }

# # Send GET request to API endpoint
# response = requests.get(url, headers=headers, params=params)

# # Parse JSON response and print product data
# products = json.loads(response.text)
# for product in products:
#     print(product)

# import requests
# import json

# min_id= 351910
# imported = 0

# payload = {}
# headers = {
#   'Accept': 'application/json',
#   'Content-Type': 'application/json',
#   'X-Auth-Client': '9pmnsfr5396d299s664x5ly8b8k68fu',
#   'X-Auth-Token': 'cxjdpm6hd7cdgzgqnd52ssjinxgfznz'
# }


# while imported < 300000 :
#     url = f"https://api.bigcommerce.com/stores/p0otkti/v2/orders.json?min_id={min_id}&sort=id&limit=250"

#     response = requests.request("GET", url, headers=headers, data=payload)
#     response = json.loads(response.text)
#     min_id = response[-1]['id']
#     imported = imported + 250
#     print(imported)
# print(min_id)
# # 351910

# p ='07585648656'
# if '+' not in p:
#     p = '+44' + p[1:]
# print(p)        
# import urllib.request
# import os

# url = 'https://store.turbify.net/yhst-130513093127159/catalog.xml'  # Replace with your URL
# folder_path = 'D:'  # Replace with your desired folder path
# file_name = 'cata.xml'  # Replace with your desired file name

# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)

# file_path = os.path.join(folder_path, file_name)
# urllib.request.urlretrieve(url, file_path)

# from datetime import datetime

# original_date_str = "6/18/2011 02:43:58"
# original_date_obj = datetime.strptime(original_date_str, '%m/%d/%Y %H:%M:%S')
# converted_date_str = '{}/{}/{} {}:{}:{}'.format(original_date_obj.year, original_date_obj.month, original_date_obj.day, original_date_obj.hour, original_date_obj.minute, original_date_obj.second)

# print(converted_date_str)

# import pandas as pd

# # read the csv file into a pandas dataframe
# df = pd.read_csv('OrderExportTue-07-11-080435.CSV')

# # drop the rows with all null values (blank rows)
# df = df.dropna(how='all')

# # write the dataframe back to a csv file
# df.to_csv('new_file.csv', index=False)

# a = '/assembleon-yamaha/'
# a = a.replace('/','-')
# print(a)
# print(a.strip('-'))

# from bs4 import BeautifulSoup

# html_code = '<table align="left" border="0" cellpadding="7" cellspacing="0" style="border-collapse: collapse; color: #313439; font-family: Helvetica, Arial, sans-serif; line-height: 20.4px; width: 527px;"><tbody><tr><td style="width: 241px;"><strong>Dimensions:</strong><br> Outside: H46 W34 D36<br> Inside: H28 W20 D20<br> Seat Height: 22<br> Arm Height: 26<br> Leg Height: 9"<span style="line-height: 20.3999996185303px;"></span><br> </td><td style="width: 252px;"><strong style="margin: 0px; padding: 0px; border: 0px; outline: 0px; background: transparent;">Ottoman </strong><strong style="margin: 0px; padding: 0px; border: 0px; outline: 0px; background: transparent;">Dimensions:</strong><br> Outside: H 20 W 21 D 24<br> $1230.00<br> <br> <br> <br> </td></tr></tbody></table><p style="margin: 0px 0px 15px; padding: 0px; border: 0px; outline: 0px; font-size: 13.1999998092651px; color: #313439; font-family: Helvetica, Arial, sans-serif; line-height: 20.3999996185303px; background-image: initial; background-attachment: initial; background-size: initial; background-origin: initial; background-clip: initial; background-position: initial; background-repeat: initial;"> </p><p style="margin: 0px 0px 15px; padding: 0px; border: 0px; outline: 0px; font-size: 13.1999998092651px; color: #313439; font-family: Helvetica, Arial, sans-serif; line-height: 20.3999996185303px; background-image: initial; background-attachment: initial; background-size: initial; background-origin: initial; background-clip: initial; background-position: initial; background-repeat: initial;"><br> </p><div style="margin: 0px; padding: 0px; border: 0px; outline: 0px; color: #313439; font-family: Helvetica, Arial, sans-serif; line-height: 20.3999996185303px; background-image: initial; background-attachment: initial; background-size: initial; background-origin: initial; background-clip: initial; background-position: initial; background-repeat: initial;"><br> <br> <br> <span style="color: #ff0000;"><br> Choose From 4 Different Leg Styles</span><br> <br> <strong>Construction Information:</strong><br> • Handmade in America<br> • 100% genuine top grain leather<br> • Kiln Dried Hardwood Frames<br> • New Advanced Tempered Spring Technology<br> • Zippers in all seat and back pillows<br> • Channeled back cushions<br> • Reinforced corner blocks<br> • Sustainable furniture council<br> • Manufacturer’s warranty<br> • Removable seat cushions (where applicable)</div><p> </p><p> </p><div><br> </div>'

# soup = BeautifulSoup(html_code, 'html.parser')

# construction_info = soup.find('div', {'style': 'margin: 0px; padding: 0px; border: 0px; outline: 0px; color: #313439; font-family: Helvetica, Arial, sans-serif; line-height: 20.3999996185303px; background-image: initial; background-attachment: initial; background-size: initial; background-origin: initial; background-clip: initial; background-position: initial; background-repeat: initial;'})

# print(construction_info.text)
# import requests

# url = "https://shop.allergybuyersclub.com/mm5/json.mvc"

# payload = "{\r</br>    \"Store_Code\": \"ABG\",\r</br>    \"Function\": \"CustomerList_Load_Query\",\r</br>    \"Sort\": \"id\",\r</br>    \"Count\": 4,\r</br>    \"Offset\": 0,\r</br>    \"Filter\": [\r</br>        {\r</br>            \"name\": \"search\",\r</br>            \"value\": [\r</br>                {\r</br>                    \"field\": \"id\",\r</br>                    \"operator\": \"GT\",\r</br>                    \"value\": \"0\"\r</br>                }\r</br>            ]\r</br>        },\r</br>        {\r</br>            \"name\": \"ondemandcolumns\",\r</br>            \"value\": [\r</br>                \"CustomField_Values:*\"\r</br>            ]\r</br>        }\r</br>    ]\r</br>}"
# headers = {
#   'Content-Type': 'application/json',
#   'Accept': 'application/json',
#   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
#   'X-Miva-API-Authorization': 'MIVA 483f8b50f6d372e0fe00817ce299e1f2',
#   'Cookie': '_cmp_a=%7B%22purposes%22%3A%7B%22a%22%3Atrue%2C%22p%22%3Atrue%2C%22m%22%3Atrue%2C%22t%22%3Atrue%7D%2C%22display_banner%22%3Afalse%2C%22merchant_geo%22%3A%22USUSVA%22%2C%22sale_of_data_region%22%3Afalse%7D; _shopify_y=c9d32713-376c-459e-ae72-cad6e38e851a; _y=c9d32713-376c-459e-ae72-cad6e38e851a'
# }

# response = requests.request("POST", url, headers=headers, data=payload, verify=False)

# print(response.text)

# import datetime

# timestamp = 1490150385  # Replace with the actual Unix timestamp

# # Convert the Unix timestamp to a datetime object
# dt = datetime.datetime.fromtimestamp(timestamp)
# print(dt)
# Create a datetime object representing May 1, 2023
# target_date = datetime.datetime(2023, 5, 1)

# Compare the datetime objects
# if dt > target_date:
#     print("The timestamp is later than May 1, 2023.")
# else:
#     print("The timestamp is not later than May 1, 2023.")
# import requests
# import json

# url = "https://www.wixapis.com/oauth/access"

# payload = json.dumps({
#   "grant_type": "refresh_token",
#   "client_id": "c6289953-d61c-4db6-90e0-efd23ca62642",
#   "client_secret": "ec9b86cb-fcc7-4973-a388-d1e0b1343987",
#   "refresh_token": "OAUTH2.eyJraWQiOiJkZ0x3cjNRMCIsImFsZyI6IkhTMjU2In0.eyJkYXRhIjoie1wiaWRcIjpcIjA0NDk2YmM0LWJkYjYtNGM5NS05NTBlLThkMzA1Y2E4MWEzMlwifSIsImlhdCI6MTY4OTEwMzc5NCwiZXhwIjoxNzUyMTc1Nzk0fQ.bbM-C7IY6UZY3mDHEwJnFPUkgfdvUVEEgT-VjtL16rg"
# })
# headers = {
#   'Authorization': 'OAUTH2.eyJraWQiOiJLaUp3NXZpeSIsImFsZyI6IlJTMjU2In0.eyJkYXRhIjoie1wiYXBwSWRcIjpcImM2Mjg5OTUzLWQ2MWMtNGRiNi05MGUwLWVmZDIzY2E2MjY0MlwiLFwiaW5zdGFuY2VJZFwiOlwiYTQ3Y2Y4OWEtODczMS00MDQ5LWFjMDYtMDVmMjA0MTdjNDJlXCIsXCJzY29wZVwiOltcIlNJVEVfU0VUVElOR1MuVklFV1wiLFwiRUNPTS5SRUFEX1RSQU5TQUNUSU9OU1wiLFwiV0lYX1NUT1JFUy5NT0RJRllfT1JERVJTXCIsXCJFQ09NLlJFQURfQ0FSVFNcIixcIldJWF9ERVZFTE9QRVJTLkdFVF9TSVRFX09XTkVSXCIsXCJFQ09NLlJFQURfRlVMRklMTE1FTlRTXCIsXCJDVVJSRU5DWV9DT05WRVJURVIuUkVBRF9DVVJSRU5DSUVTXCIsXCJXSVhfU1RPUkVTLlJFQURfSElEREVOX1NVQlNDUklQVElPTl9PUFRJT05TXCIsXCJFQ09NLlJFQURfT1JERVJTXCIsXCJDT05UQUNUUy5WSUVXX05FV1wiLFwiV0lYX1NUT1JFUy5SRUFEX1BST0RVQ1RTXCIsXCJFQ09NLlJFQURfQ0hFQ0tPVVRTXCIsXCJXSVhfREVWRUxPUEVSUy5HRVRfRURJVE9SX0RFRVBfTElOS1wiLFwiV0lYX1NUT1JFUy5SRUFEX0hJRERFTl9QUk9EVUNUU1wiLFwiV0lYX1NUT1JFUy5NT0RJRllfSU5WRU5UT1JZXCIsXCJXSVhfREVWRUxPUEVSUy5TRU5EX0JJX0VWRU5UU1wiLFwiV0lYX1NUT1JFUy5SRUFEX09SREVSU1wiLFwiV0lYX1NUT1JFUy5DUkVBVEVfT1JERVJTXCIsXCJXSVhfREVWRUxPUEVSUy5BUFBfUFVSQ0hBU0VfSElTVE9SWVwiLFwiU0NPUEVfU0hBUkVfVVJMLk1BTkFHRVwiLFwiV0lYX1NUT1JFUy5NT0RJRllfUFJPRFVDVFNcIixcIkNPTlRBQ1RTLlZJRVdcIixcIldJWF9TVE9SRVMuTU9ESUZZX1NVQlNDUklQVElPTl9PUFRJT05TXCIsXCJXSVhfU1RPUkVTLlJFQURfQ0FSVFNcIixcIldJWF9TVE9SRVMuUkVBRF9TVUJTQ1JJUFRJT05fT1BUSU9OU1wiLFwiRUNPTS5HRVRfRUxJR0lCTEVfVFJJR0dFUlNcIixcIkVDT00uTU9ESUZZX0ZVTEZJTExNRU5UU1wiLFwiV0lYX0RFVkVMT1BFUlMuQ1JFQVRFX0NIRUNLT1VUXCIsXCJXSVhfREVWRUxPUEVSUy5NQU5BR0VfQVBQX0lOU1RBTkNFXCIsXCJXSVhfU1RPUkVTLk1PRElGWV9GVUxGSUxMRVJTXCIsXCJXSVhfU1RPUkVTLlJFQURfRlVMRklMTEVSU1wiLFwiV0lYX1NUT1JFUy5SRUFEX0lOVkVOVE9SWVwiLFwiY29udGFjdHMubW9kaWZ5XCIsXCJERVZfQ0VOVEVSLlNJVEVfUEFZTUVOVF9NRVRIT0RcIixcIkNPTlRBQ1RTLk1FUkdFXCIsXCJXSVhfU1RPUkVTLlJFQURfQUJBTkRPTkVEX0NBUlRTXCIsXCJFQ09NLkdFVF9BUFBMSUVEX0RJU0NPVU5UU1wiXX0iLCJpYXQiOjE2NjAyNzgwMTUsImV4cCI6MTY2MDI3ODMxNX0.APYyb0WTD59FaGY_TCCHeOunm5jMn1audH5VlMNjDKJKxRbLZZ8ljZPvCt4LW6rfZWbS58ahCoaJ89QQsviw4oLvYEUNVBFdk69PYi0wPHxhIIM2VLZhwE2yLfDJeIxWkumzQ7Pd9LKUw4wTEJKwWpM27EKUhBn-LxG0IsS0aaN6Uecdx7KJCDGq-44RGmYykIUCu3c5-ks9D38AEirOKREFaBIMB302fbrCbXsoi6fTB2RzuJ0JejOZuNAyw9zexu0_lAweskFGtqc-NZILl91-rQn01Z-3vKsTqQ1wunk_ieeX_yofHmGF1abyBsc1BfYvI_uu4lbN1ibDFs5ypw',
#   'Content-Type': 'application/json',
#   'Cookie': 'XSRF-TOKEN=1692718661|IXHyzea14ztI'
# }

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)

# def calculate_bills_to_use(amount):
#     rsl = {500:0, 100: 0, 50: 0, 25: 0, 10: 0, 5: 0, 1: 0}
#     balance = amount
#     while balance > 0:
#         for row in rsl:
#             # print('row')

#             # print(row)
#             if balance >= row:
#                 amt = balance//row
#                 # print(amt)
#                 rsl[row] = amt
#                 balance = balance - amt*row
#     return rsl

# print(calculate_bills_to_use(355))


#     def calculate_bills_to_use_advanced(amount,bills):
#         rsl = {500:0, 100: 0, 50: 0, 25: 0, 10: 0, 5: 0, 1: 0}
#         balance = amount
#         while balance > 0:
#             for row in rsl:
#                 # print('row')

#                 # print(row)
#                 if balance >= row:
#                     amt = balance//row
#                     if bills[row] < amt:
#                         amt = bills[row]
#                     # print(amt)
#                     rsl[row] = amt
#                     balance = balance - amt*row
#         return rsl
# print(calculate_bills_to_use_advanced(163, {
#         500: 1,
#         100: 0,
#         50: 10,
#         25: 10,
#         10: 10,
#         5: 10,
#         1: 10
#     }))

# import re

# def extract_youtube_link(text):
#     # Regular expression pattern to match a YouTube video URL
#     pattern = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=|embed\/|v\/)?([\w-]+)'

#     # Find the YouTube video URL using regular expression
#     match = re.search(pattern, text)

#     if match:
#         # Extract the YouTube video ID from the matched group
#         youtube_id = match.group(1)
#         youtube_url = f"https://www.youtube.com/watch?v={youtube_id}"
#         return youtube_url

#     return None

# content = '''<span style="font-weight: 400;">The best Quality  HDPE 12×12 Cylindrical Grow Bag is ideal for growing vegetables, flowering plants, and indoor plants for home gardening. These Best Round Grow Bags 260 GSM are UV stabilized of premium quality, which can easily last for 6 to 7 years in sunlight and rain after planting. You can use these plant bags for all types of vegetables, herbs, and flowering plants that can be easily grown in a home garden, terrace garden, kitchen garden, and rooftop balcony garden.</span>
# <h2><strong>Product's Highlights</strong></h2>
# <ul>
#      <li style="font-weight: 400;" aria-level="1"><b>Width</b><span style="font-weight: 400;">: 30cm</span></li>
#      <li style="font-weight: 400;" aria-level="1"><b>Height</b><span style="font-weight: 400;">: 30cm </span></li>
#      <li style="font-weight: 400;" aria-level="1"><b>Color</b><span style="font-weight: 400;">: Green</span></li>
#      <li style="font-weight: 400;" aria-level="1"><b>Thickness:</b><span style="font-weight: 400;"> 260 GSM HDPE Material.</span></li>
#      <li style="font-weight: 400;" aria-level="1"><b>Water drainage holes:</b><span style="font-weight: 400;"> Drain Holes are available at the bottom of the bags.</span></li>
#      <li style="font-weight: 400;" aria-level="1"><b>Ideal For:</b><span style="font-weight: 400;"> Home garden, terrace gardening, kitchen gardening, terrace poly house gardening &amp; rooftop balcony gardening.</span></li>
#      <li style="font-weight: 400;" aria-level="1"><b>Usage:</b><span style="font-weight: 400;"> You can grow almost all kinds of vegetables, herbs, and flower plants.</span></li>
#      <li style="font-weight: 400;" aria-level="1"><b>Stability:</b><span style="font-weight: 400;"> UV Stabilized Grow Bag for longer life in hot and cold weather.</span></li>
#      <li style="font-weight: 400;" aria-level="1"><b>Durability:</b><span style="font-weight: 400;"> The durability of the bag is 5-7 years &amp; it can use many times in your garden.</span></li>
#      <li style="font-weight: 400;" aria-level="1"><b>Weight: </b><span style="font-weight: 400;">It’s very Light Weight and Portable. It can be easily moved anywhere around the Home Garden or Terrace Garden. </span></li>
#      <li style="font-weight: 400;" aria-level="1"><b>Benefits:</b><span style="font-weight: 400;"> Thick, Durable, Washable, Non-Tearable, Reusable, UV-treated, and Premium Quality. You can use it on the open terrace.</span></li>
# </ul>
# https://youtu.be/17IPIplZ4Tg
# <h2><strong>Plants That Can Be Grown</strong></h2>
# <ul>
#      <li>Tomato</li>
#      <li>Brinjal or Eggplant</li>
#      <li>Green Chilli</li>
#      <li>Onion</li>
#      <li style="font-size: 18px;">Pea</li>
#      <li>Ladies Finger (Okra)</li>
#      <li>Green Cucumber</li>
#      <li>Lobia (Green Long Bean)</li>
#      <li>Radish</li>
#      <li>Sponge Gourd</li>
#      <li>Cabbage</li>
#      <li>Broccoli</li>
#      <li>Beetroot</li>
#      <li>Capsicum</li>
#      <li>Turnip</li>
#      <li>Cauliflower</li>
#      <li style="font-size: 18px;">Zucchini</li>
#      <li style="font-size: 18px;">French Beans</li>
#      <li style="font-size: 18px;">Cluster Beans</li>
#      <li style="font-size: 18px;">Bell Pepper</li>
#      <li style="font-size: 18px;">Potato</li>
#      <li style="font-size: 18px;">Ginger</li>
#      <li>Mint</li>
#      <li>Aloe Vera</li>
#      <li>Tulsi</li>
#      <li>Lavender</li>
#      <li>Celeriac</li>
# </ul>
# <h2>Why You Can Use HDPE Grow Bags</h2>
# HDPE grow bags are a type of container used for growing plants, typically vegetables or herbs. They are made from high-density polyethylene (HDPE), a durable plastic material that is resistant to UV radiation, moisture, and pests. HDPE grow bags have several advantages over traditional pots or containers for growing plants.

# One advantage is that they are lightweight and easy to move around, which makes it convenient to change the location of your plants as needed. They also have good drainage and air circulation, which helps to promote healthy plant growth. HDPE grow bags are also reusable, which makes them an environmentally friendly option for growing plants.

# There are several factors to consider when using HDPE grow bags for plant growth. One important factor is the size of the bag. HDPE grow bags come in a range of sizes, and it is important to choose a size that is appropriate for the plants you are growing. You should also consider the type of plants you are growing, as some plants may require a specific type of soil or growing medium.

# Overall, HDPE grow bags can be a convenient and effective way to grow plants, particularly for those with limited space or who are looking for an alternative to traditional pots or containers.

# <em><strong>Note: The plants are not included in the package's grow bag. Customers will only get grow bags in the package.</strong></em>'''
# print(extract_youtube_link(content))


# import re

# def convert_math_alphanumeric_symbols(text):
#     # Define a mapping of Mathematical Alphanumeric Symbols to regular ASCII characters
#     symbol_mapping = {
#         '𝗔': 'A', '𝗕': 'B', '𝗖': 'C', '𝗗': 'D', '𝗘': 'E', '𝗙': 'F', '𝗚': 'G', '𝗛': 'H',
#         '𝗜': 'I', '𝗝': 'J', '𝗞': 'K', '𝗟': 'L', '𝗠': 'M', '𝗡': 'N', '𝗢': 'O', '𝗣': 'P',
#         '𝗤': 'Q', '𝗥': 'R', '𝗦': 'S', '𝗧': 'T', '𝗨': 'U', '𝗩': 'V', '𝗪': 'W', '𝗫': 'X',
#         '𝗬': 'Y', '𝗭': 'Z',
#         '𝗮': 'a', '𝗯': 'b', '𝗰': 'c', '𝗱': 'd', '𝗲': 'e', '𝗳': 'f', '𝗴': 'g', '𝗵': 'h',
#         '𝗶': 'i', '𝗷': 'j', '𝗸': 'k', '𝗹': 'l', '𝗺': 'm', '𝗻': 'n', '𝗼': 'o', '𝗽': 'p',
#         '𝗾': 'q', '𝗿': 'r', '𝘀': 's', '𝘁': 't', '𝘂': 'u', '𝘃': 'v', '𝘄': 'w', '𝘅': 'x',
#         '𝘆': 'y', '𝘇': 'z',
#         '𝟬': '0', '𝟭': '1', '𝟮': '2', '𝟯': '3', '𝟰': '4', '𝟱': '5', '𝟲': '6', '𝟳': '7',
#         '𝟴': '8', '𝟵': '9'
#     }

#     # Use regular expressions to find and replace the symbols in the text
#     pattern = re.compile('|'.join(re.escape(symbol) for symbol in symbol_mapping.keys()))
#     converted_text = pattern.sub(lambda match: symbol_mapping[match.group(0)], text)

#     return converted_text
# # cont = '''<br>𝗘𝘂𝗿𝗼𝗽𝗲𝗮𝗻 𝗖𝘂𝘀𝘁𝗼𝗺𝗲𝗿𝘀 𝗣𝗹𝗲𝗮𝘀𝗲 𝗡𝗼𝘁𝗲 :</br>𝗔𝗹𝗹 𝗢𝗿𝗱𝗲𝗿𝘀 𝗳𝗼𝗿 𝗘𝘂𝗿𝗼𝗽𝗲 𝗕𝗮𝘀𝗲𝗱 𝗖𝗼𝘂𝗻𝘁𝗿𝗶𝗲𝘀 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗦𝗵𝗶𝗽𝗽𝗲𝗱 𝗳𝗿𝗼𝗺 𝗜𝗻𝘁𝗲𝗿𝗻𝗮𝘁𝗶𝗼𝗻𝗮𝗹 𝗟𝗼𝗰𝗮𝘁𝗶𝗼𝗻. 𝗪𝗲 𝗔𝗿𝗲 𝗡𝗼𝘁 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗶𝗯𝗹𝗲 𝗙𝗼𝗿 𝗜𝗺𝗽𝗼𝗿𝘁 𝗧𝗮𝘅𝗲𝘀 𝗔𝗻𝗱 𝗖𝘂𝘀𝘁𝗼𝗺𝘀 𝗗𝘂𝘁𝘆</br>(𝗶𝗳 𝗮𝗻𝘆)'''  
# # print(convert_math_alphanumeric_symbols(cont)) 

# import requests
# import json
# url = "https://api.bigcommerce.com/stores/fu5mt4ftdu/v3/catalog/products/1105"

# payload = json.dumps({
#   "description":  convert_math_alphanumeric_symbols(des) 
# })
# headers = {
#   'Accept': 'application/json',
#   'Content-Type': 'application/json',
#   'X-Auth-Token': 'm0ijhco5ejp996gx8gxxfaqg6ninsu'
# }

# response = requests.request("PUT", url, headers=headers, data=payload)

# print(response.text)


# import os
# import requests

# url = "https://us.merchantos.com/exports.php?form_name=listing&name=item.listings.local_matches&__tab=single&__sort=description&__sort_dir=ASC&shop_id=1&disp_year=off&show_catalog_results=off&qoh_positive=off&qoh_zero=off&publish_to_ecom=off&archived=off&vendor_id=68&show_all_shops=off&ajax=0"
# folder_path = "D:\\LiteMigration"  # Replace with the desired folder path
# filename = "downloaded_file.csv"
# file_path = os.path.join(folder_path, filename)

# response = requests.get(url)

# if response.status_code == 200:
#     with open(file_path, "wb") as file:
#         file.write(response.content)
#     print("File downloaded successfully.")
# else:
#     print("Failed to download the file.")
# def sql_unescape(self, text: str):
#     replace_data = {
#         r"\"": r'"',
#         r"\\\"": r"\"",
#         r"\%": r"%",
#         r"\\\\/": r"/",
#         r'\\"': r"\"",
#     }

#     pattern = re.compile("|".join(re.escape(key) for key in replace_data.keys()))
#     return pattern.sub(lambda match: replace_data[match.group(0)], text)

# from bs4 import BeautifulSoup

# def strip_html_tags(html):
#     soup = BeautifulSoup(html, "html.parser")
#     stripped_text = soup.get_text()
#     return stripped_text

# from html.parser import HTMLParser

# class HTMLStripper(HTMLParser):
#     def __init__(self):
#         super().__init__()
#         self.stripped_text = []

#     def handle_data(self, data):
#         self.stripped_text.append(data)

#     def get_stripped_text(self):
#         return ' '.join(self.stripped_text)

# import re

# def strip_html_tags(html):
#     # Remove HTML tags using regex
#     clean_text = re.sub('<.*?>', '', html)
#     return clean_text

# # Example usage


# # Example usage
# # html_string = "<p>This is <b>bold</b> and <i>italic</i> text.</p>"
# # stripped_text = strip_html_tags(html_string)
# # print(stripped_text)

# # Example usage
# html_string = '''<h2 style="font-size: 17px;">Ce sunt culorile acrilice?</h2>
# <p>Culorile acrilice sunt vopsele obtinute prin amestecul pigmentilor cu un liant pe baza de emulsie acrilica pe baza de apa. Particularitatea culorilor acrilice consta in aceea ca odata uscate, ele devin insolubile in apa, formand o pelicula elastica, puternic aderenta la suport. De fapt dupa uscare, aceste culori sunt foarte greu de eliminat.</p>
# <p>Se poate spune despre culorile acrilice ca sunt culorile secolului XXI, datorita succesului pe care l-au capatat in ultimii ani in randul pictorilor din intreaga lume.</p>
# <h2 style="font-size: 17px;">Specificatii culori acrilice</h2>
# <p>Pe langa faptul ca multi artisti contemporani aleg sa utilizeze aceste “acuarele acrilice”, exista numeroase motive pentru care si tu ar trebui sa iti indrepti atentia asupra acestor culori:</p>
# <ul style="list-style-type: disc;">
# <li><strong>Sunt culori versatile.</strong> Acest lucru inseamna ca poti picta pe orice tip de suprafata, de la panza, lemn, hartie, piatra, sticla, chiar si metal sau plastic.</li>
# <li><strong>Pot fi diluate cu apa</strong> si aplicate in laviuri asemeni acuarelei sau amestecate cu diverse medii de pictura pentru aplicari grosiere asemeni picturii in cutit ce folosea culori de ulei.</li>
# <li><strong>Se usuca repede.</strong> Spre deosebire de alte tipuri de culori, cele acrilice au un timp de uscare scazut, fapt care iti permite sa finalizezi proiectele mai repede. In functie de grosimea stratului, acestea se pot usca de la cateva minute la cateva ore. Aceasta calitate poate fi un avantaj, dar in cazul picturii la sevalet, este si un dezavantaj. Pentru impiedicarea uscarii acrilicelor pe paleta se foloseste mediul de intarziere ce are ca rol prelungirea timpului de uscare al culorilor.</li>
# <li><strong>Nu sunt toxice.</strong> Gratie compusilor care stau la baza tuburilor de culori acrilice, nu se emana substante toxice. Prin urmare, sunt sigure pentru copii si se pot folosi in orice tip de incapere.</li>
# <li><strong>Sunt extrem de maleabile.</strong> Poti controla simplu consistenta si textura in functie de preferinte. Tot ce trebuie sa faci este sa testezi pana ajungi la formula ideala pentru tine si pentru proiectul tau.</li>
# <li><strong>Sunt culori durabile.</strong> Dupa ce ai terminat pictura, nu trebuie sa iti faci griji cu privire la degradarea vopselei. Vopseaua acrilica este rezistenta la apa, nu crapa si nici nu isi pierde din stralucire.</li>
# </ul>
# <h2 style="font-size: 17px;">Ce tip de culori acrilice sa alegi?</h2>
# <p>Atunci cand cumperi culori acrilice tine cont de: calitatea, culoarea, rezistenta in timp, vascozitatea, tipul de flacon, timpul de uscare si, bineinteles, brandul. Te ajutam sa aduci creativitatea la un nou nivel cu vopselele acrilice de la cele mai cunoscute branduri de <a title="materiale pictura" href="https://www.colorit.ro/materiale-pictura.html" target="_blank" rel="noopener">materiale pictura</a>: Royal Talens, Jacquard, Raphael sau Sennelier.</p>
# <p>Calitatea culorilor acrilice:</p>
# <ul style="list-style-type: disc;">
# <li><strong>Culori acrilice extrafine:</strong> culori profesionale, maxim de calitate - folosesc pigmenti autentici in concentratie maxima. De regula o culoare este formata dintr-un singur pigment. Prin amestecul a doua culori monopigmentare veti obtine nuante mai vii si mai "curate". Enumeram aici: <a title="culori acrilice Rembrandt" href="https://www.colorit.ro/culori-acrilice-rembrandt.html" target="_blank" rel="noopener">Culorile acrilice Rembrandt</a> sau <a title="Amsterdam Expert" href="https://www.colorit.ro/culori-acrilice-amsterdam-expert-23531.html" target="_blank" rel="noopener">Amsterdam Expert</a>.</li>
# <li><strong>Culorile de calitate “studio”:</strong> culori cu o concentratie mare de pigment din a caror paleta cromatica s-au scos pigmentii rari (cadmiu, cobalt), acestia fiind inlocuiti de versiuni sintetice, mai ieftine, dar de buna calitate. Aici se incadreaza gamele: <a title="Amsterdam" href="https://www.colorit.ro/culori-acrilice-amsterdam.html" target="_blank" rel="noopener">Amsterdam</a>, <a title="Van Gogh" href="https://www.colorit.ro/culori-acrilice-van-gogh-20852.html" target="_blank" rel="noopener">Van Gogh</a> de la Royal Talens, <a title="Abstract" href="https://www.colorit.ro/culori-acrilice-abstract.html" target="_blank" rel="noopener">Abstract</a> sau <a title="Abstract Mat" href="https://www.colorit.ro/culori-acrilice-abstract-matt.html" target="_blank" rel="noopener">Abstract Mat</a> de la Sennelier.</li>
# <li><strong>Culori de calitate “student”:</strong> culori acrilice folosite pentru exercitii sau pentru pictura in scopuri recreative. Astfel de culori sunt: <a title="Art Creation" href="https://www.colorit.ro/culori-acrilice-talens-art-creation.html" target="_blank" rel="noopener">Art Creation</a> sau <a title="Campus" href="https://www.colorit.ro/culori-acrilice-campus.html" target="_blank" rel="noopener">Campus</a> de la Raphael.</li>
# </ul>
# <h2 style="font-size: 17px;">Cum poti sterge urmele de culori acrilice uscate?</h2>
# <p>Se stie faptul ca acrilicele dupa uscare nu se mai dizolva cu apa si nici cu majoritatea solventilor din comert. Am descoperit recent ca aceste culori se curata usor cu alcool isopropilic sau cu solutia de curatat pensule.</p>'''
# stripped_text = strip_html_tags(html_string)
# print(stripped_text)

# import os

# file_path = 'https://organicbazar.net/wp-content/uploads/2021/06/HDPE-Grow-Bag-18-x-09.jpg'
# file_name = os.path.basename(file_path)

# print(file_name)  # Output: file.txt
# import re

# text = '[vc_row][vc_column][vc_custom_heading text="Unraveling the Mysterious and Mischievous World of the Artivist Extraordinaire!" font_container="tag:h2|text_align:left|color:%23000000" use_theme_fonts="yes"][vc_column_text]Today, we are diving headfirst into the mind-boggling world of none other than the elusive street art legend himself - and long term hero of mine – Banksy. Grab your spray cans, activate the right side of your brain, and let\'s dive down a rabbit hole of creativity and mischief!'

# cleaned_text = re.sub(r'\[.*?\]', '', text)
# print(cleaned_text)

# from bs4 import BeautifulSoup

# def remove_css(html):
#     soup = BeautifulSoup(html, 'html.parser')

#     # Remove all <style> tags
#     for style in soup('style'):
#         style.decompose()

#     # Remove all inline style attributes
#     for tag in soup(recursive=True):
#         if tag.has_attr('style'):
#             del tag['style']

#     # Remove all <link> tags with a 'stylesheet' type attribute
#     for link in soup('link'):
#         if link.get('rel') == ['stylesheet']:
#             link.decompose()

#     return soup.prettify()

# # Example usage:
# html = '''
# <table align="center" cellpadding="1" class="cke-table editor_table_with_border" style="border: 0px solid transparent; font-family: verdana,arial,helvetica; font-size: 12px; line-height: 16.8px; resize: none;">
# <tbody style="border-style: solid; border-width: inherit;">
# <tr style="line-height: 16.8px; resize: none; border-width: inherit; border-style: solid; border-image: initial; border-spacing: 0px; border-collapse: collapse; color: inherit;">
# <td class="editor_td_with_border" style="line-height: 16.8px; resize: none; border: 0px solid transparent; border-spacing: 0px; border-collapse: collapse; font-family: Verdana, Arial, Helvetica; font-size: 12px; text-align: center;"><span style="line-height: 19.6px; resize: none; font-size: 14px;"><span style="line-height: 19.6px; resize: none; color: #404348; font-family: verdana, arial, helvetica; font-weight: bold;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">COMPOSITION - TECHNICAL SPECIFICATIONS</span></span></span></span></span></span></td>
# <td class="editor_td_with_border" style="line-height: 16.8px; resize: none; border: 0px solid transparent; border-spacing: 0px; border-collapse: collapse; font-family: Verdana, Arial, Helvetica; font-size: 12px; text-align: center;"><span style="line-height: 19.6px; resize: none; font-size: 14px;"><span style="line-height: 19.6px; resize: none; color: #404348; font-family: verdana, arial, helvetica; font-weight: bold; text-align: center;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">PRODUCTION</span></span></span></span></span></span></td>
# </tr>
# <tr style="line-height: 16.8px; resize: none; border-width: inherit; border-style: solid; border-image: initial; border-spacing: 0px; border-collapse: collapse; color: inherit;">
# <td class="editor_td_with_border" style="line-height: 16.8px; resize: none; border: 0px solid transparent; border-spacing: 0px; border-collapse: collapse; font-family: Verdana, Arial, Helvetica; font-size: 12px; text-align: center;"><span style="line-height: 19.6px; resize: none; font-size: 14px;"><span style="line-height: 19.6px; resize: none; color: #404348;"><span style="line-height: 19.6px; resize: none; font-family: verdana, arial, helvetica;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">100% Cotton - Yarn 76x68 30/1 30/1</span></span></span></span></span></span></span></td>
# <td class="editor_td_with_border" style="line-height: 16.8px; resize: none; border: 0px solid transparent; border-spacing: 0px; border-collapse: collapse; font-family: Verdana, Arial, Helvetica; font-size: 12px; text-align: center;"><span style="line-height: 19.6px; resize: none; color: #404348; font-family: verdana, arial, helvetica; font-size: 14px;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">100% Made in Italy</span></span></span></span></span></td>
# </tr>
# <tr style="line-height: 16.8px; resize: none; border-width: inherit; border-style: solid; border-image: initial; border-spacing: 0px; border-collapse: collapse; color: inherit;">
# <td class="editor_td_with_border" style="line-height: 16.8px; resize: none; border: 0px solid transparent; border-spacing: 0px; border-collapse: collapse; font-family: Verdana, Arial, Helvetica; font-size: 12px; text-align: center;"><span style="line-height: 11.2px; resize: none; font-family: verdana, arial, helvetica; font-size: 8px;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">.................................................. .................................................. .................................................. ..</span></span></span></span></span></td>
# <td class="editor_td_with_border" style="line-height: 16.8px; resize: none; border: 0px solid transparent; border-spacing: 0px; border-collapse: collapse; font-family: Verdana, Arial, Helvetica; font-size: 12px; text-align: center;"><span style="line-height: 11.2px; resize: none; font-family: verdana, arial, helvetica; font-size: 8px;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">.................................................. .................................................. ..................................................</span></span></span></span></span></td>
# </tr>
# <tr style="line-height: 16.8px; resize: none; border-width: inherit; border-style: solid; border-image: initial; border-spacing: 0px; border-collapse: collapse; color: inherit;">
# <td class="editor_td_with_border" colspan="2" style="line-height: 16.8px; resize: none; border: 0px solid transparent; border-spacing: 0px; border-collapse: collapse; font-family: Verdana, Arial, Helvetica; font-size: 12px; text-align: center;">
# <p style="line-height: 16.8px; resize: none; margin: 0px 0px 6px;"><span style="line-height: 19.6px; resize: none; color: #404348; font-family: verdana, arial, helvetica; font-size: 14px; font-weight: bold;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">CHARACTERISTICS:</span></span></span></span></span></p>
# </td>
# </tr>
# <tr>
# <td class="editor_td_with_border" colspan="2" style="border: 0px solid transparent;">
# <div style="text-align: center;"><span style="font-size: 14px;"><span style="font-family: verdana,arial,helvetica;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">Complete set of sheets with an excellent quality/price ratio.</span></span></span></span></span></span></div>
# <div style="text-align: center;"> </div>
# <div style="text-align: center;"><span style="font-size: 12px;"><span style="font-family: verdana,arial,helvetica;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">All suppliers used for the production of these items are Oeko-Tex certified: for the </span></span></span></span></span><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"> textile sector the</span></span></span></span></span></div>
# <div style="text-align: center;"><span style="font-size: 12px;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">evaluation criteria are finally uniform and scientifically proven for the human-ecological safety of the products</span></span></span></span></span></div>
# <div style="text-align: center;"><span style="font-size: 12px;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">textiles, Oeko-Tex certification indicates textile products which have as added value the guarantee of having been</span></span></span></span></span></div>
# <div style="text-align: center;"><span style="font-size: 12px;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">analyzed to evaluate their harmlessness to human health, it therefore represents an important decision-making tool for purchasing.</span></span></span></span></span></div>
# <div style="text-align: center;"> </div>
# <div style="text-align: center;"><span style="font-size: 12px;"><span style="font-family: verdana,arial,helvetica;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">Furthermore, all suppliers comply with the Reach regulation regarding the content of chemical substances in the </span></span></span></span></span><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"> dyes</span></span></span></span></span></div>
# <div style="text-align: center;"><span style="font-size: 12px;"><span style="font-family: verdana,arial,helvetica;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">used for printing, in particular the components used for processing the products do not contain the  </span></span></span></span></span><span style="font-family: verdana, arial, helvetica;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">listed SVHC substances</span></span></span></span></span></span></div>
# <div style="text-align: center;"><span style="font-size: 12px;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">in the ECHA Candidate List and are not covered by the market and use restrictions of certain dangerous substances, preparations and articles.</span></span></span></span></span></div>
# </td>
# </tr>
# <tr style="line-height: 16.8px; resize: none; border-width: inherit; border-style: solid; border-image: initial; border-spacing: 0px; border-collapse: collapse; color: inherit;">
# <td class="editor_td_with_border" colspan="2" style="line-height: 16.8px; resize: none; border: 0px solid transparent; border-spacing: 0px; border-collapse: collapse; font-family: Verdana, Arial, Helvetica; font-size: 12px; text-align: center;"><span style="line-height: 11.2px; resize: none; font-family: verdana, arial, helvetica; font-size: 8px;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">.................................................. .................................................. .................................................. .................................................. .................................................. .................................................. ...</span></span></span></span></span></td>
# </tr>
# <tr style="line-height: 16.8px; resize: none; border-width: inherit; border-style: solid; border-image: initial; border-spacing: 0px; border-collapse: collapse; color: inherit;">
# <td class="editor_td_with_border" colspan="2" style="line-height: 16.8px; resize: none; border: 0px solid transparent; border-spacing: 0px; border-collapse: collapse; font-family: Verdana, Arial, Helvetica; font-size: 12px; text-align: center;"> </td>
# </tr>
# <tr style="line-height: 16.8px; resize: none; border-width: inherit; border-style: solid; border-image: initial; border-spacing: 0px; border-collapse: collapse; color: inherit;">
# <td class="editor_td_with_border" colspan="2" style="line-height: 16.8px; resize: none; border: 0px solid transparent; border-spacing: 0px; border-collapse: collapse; font-family: Verdana, Arial, Helvetica; font-size: 12px; text-align: center;">
# <p style="line-height: 16.8px; resize: none; margin: 0px 0px 6px;"><span style="line-height: 19.6px; resize: none; font-size: 14px;"><span style="line-height: 19.6px; resize: none; color: #404348; font-family: verdana, arial, helvetica; font-weight: bold;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">SIZE CHART</span></span></span></span></span></span></p>
# </td>
# </tr>
# <tr style="line-height: 16.8px; resize: none; border-width: inherit; border-style: solid; border-image: initial; border-spacing: 0px; border-collapse: collapse; color: inherit;">
# <td class="editor_td_with_border" colspan="2" style="line-height: 16.8px; resize: none; border: 0px solid transparent; border-spacing: 0px; border-collapse: collapse; font-family: Verdana, Arial, Helvetica; font-size: 12px; text-align: center;"><span style="line-height: 11.2px; resize: none; font-family: verdana, arial, helvetica; font-size: 8px;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">.................................................. .................................................. .................................................. .................................................. .................................................. .................................................. ....</span></span></span></span></span></td>
# </tr>
# <tr>
# <td class="editor_td_with_border" colspan="2" style="line-height: 16.8px; resize: none; border: 0px solid transparent; border-spacing: 0px; border-collapse: collapse; font-family: Verdana, Arial, Helvetica; font-size: 12px; text-align: center;">
# <pre class="line-height-75 cke-line-height" style="font-size: 12px;"><strong style="font-size: 12px;"><span style="font-size: 14px; font-family: verdana, arial, helvetica; color: #404348;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">Items included in the Complete Single Sheet Set - Single:</span></span></span></span></span></strong><span></span>
# <span></span>
# <span style="font-size: 14px; font-family: verdana, arial, helvetica; color: #404348;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">- Fitted bottom sheet measuring 90x200cm - Cordonetto top sheet measuring 150x300cm - 1 pillowcase 52x82cm</span></span></span></span></span></pre>
# <p> </p>
# <pre class="line-height-75 cke-line-height" style="font-size: 12px; text-align: center;"><strong style="font-size: 12px;"><span style="font-size: 14px; font-family: verdana, arial, helvetica; color: #404348;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">Items included in the Complete Single Sheet Set:</span></span></span></span></span></strong><span></span>
# <span></span>
# <span style="font-size: 14px; font-family: verdana, arial, helvetica; color: #404348;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">- Fitted bottom sheet measures 120x200cm - Cordonetto top sheet measures 180x300cm - 1 pillowcase 52x82cm</span></span></span></span></span></pre>
# <p> </p>
# <pre class="line-height-75 cke-line-height" style="font-size: 12px; text-align: center;"><strong style="font-size: 12px;"><span style="font-size: 14px; font-family: verdana, arial, helvetica; color: #404348;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">Items included in the Complete French Queen Sheet Set:</span></span></span></span></span></strong><span></span>
# <span></span>
# <span style="font-size: 14px; font-family: verdana, arial, helvetica; color: #404348;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">- Fitted bottom sheet measuring 140x200cm - Cordonetto top sheet measuring 200x300cm - 2 pillowcases 52x82cm</span></span></span></span></span></pre>
# <p> </p>
# <pre class="line-height-75 cke-line-height" style="font-size: 12px; text-align: center;"><strong style="font-size: 12px;"><span style="font-size: 14px; font-family: verdana, arial, helvetica; color: #404348;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">Items included in the Complete Double Sheet Set - Double:</span></span></span></span></span></strong><span></span>
# <span></span>
# <span style="font-size: 14px; font-family: verdana, arial, helvetica; color: #404348;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">- Fitted bottom sheet measuring 180x200cm - Cordonetto top sheet 250x300cm - 2 pillowcases 52x82cm</span></span></span></span></span></pre>
# <p> </p>
# <pre class="line-height-75 cke-line-height" style="font-size: 12px; text-align: center;"><strong style="font-size: 12px;"><span style="font-size: 14px; font-family: verdana, arial, helvetica; color: #404348;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">Items included in the Complete Double Sheet Set - Maxi Double:</span></span></span></span></span></strong><span></span>
# <span></span>
# <span style="font-size: 14px; font-family: verdana, arial, helvetica; color: #404348;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">- Fitted bottom sheet without corners measuring 270x300cm - Cordonetto top sheet measuring 270x300cm - 2 pillowcases 52x82cm</span></span></span></span></span></pre>
# </td>
# </tr>
# <tr>
# <td class="editor_td_with_border" colspan="2" style="line-height: 16.8px; resize: none; border: 0px solid transparent; border-spacing: 0px; border-collapse: collapse; font-family: Verdana, Arial, Helvetica; font-size: 12px; text-align: center;"><span style="font-family: verdana, arial, helvetica; font-size: 8px; text-align: center;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">.................................................. .................................................. .................................................. .................................................. .................................................. .................................................. ....</span></span></span></span></span></td>
# </tr>
# <tr>
# <td class="editor_td_with_border" colspan="2" style="line-height: 16.8px; resize: none; border: 0px solid transparent; border-spacing: 0px; border-collapse: collapse; font-family: Verdana, Arial, Helvetica; font-size: 12px; text-align: center;">
# <pre class="line-height-75 cke-line-height" style="font-size: 12px; text-align: center;"><strong style="font-size: 12px;"><span style="font-size: 14px; font-family: verdana, arial, helvetica; color: #404348;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">TYPE OF PRODUCTION:</span></span></span></span></span></strong><span></span>
# <span></span>
# <span style="font-size: 14px; font-family: verdana, arial, helvetica; color: #404348;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">Continuous production item, available all year round.</span></span></span></span></span></pre>
# </td>
# </tr>
# <tr>
# <td class="editor_td_with_border" colspan="2" style="line-height: 16.8px; resize: none; border: 0px solid transparent; border-spacing: 0px; border-collapse: collapse; font-family: Verdana, Arial, Helvetica; font-size: 12px; text-align: center;"><span style="font-family: verdana, arial, helvetica; font-size: 8px; text-align: center;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">.................................................. .................................................. .................................................. .................................................. .................................................. .................................................. ....</span></span></span></span></span></td>
# </tr>
# <tr>
# <td class="editor_td_with_border" colspan="2" style="line-height: 16.8px; resize: none; border: 0px solid transparent; border-spacing: 0px; border-collapse: collapse; font-family: Verdana, Arial, Helvetica; font-size: 12px; text-align: center;">
# <pre class="line-height-75 cke-line-height" style="font-size: 12px; text-align: center;"><strong style="font-size: 12px;"><span style="font-size: 14px; font-family: verdana, arial, helvetica; color: #404348;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">RELATED ARTICLES FROM THE SAME LINE (Continuous or seasonal)</span></span></span></span></span></strong><span></span>
# <span></span>
# <span style="font-size: 14px; font-family: verdana, arial, helvetica; color: #404348;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">Sheet set, flannel sheet set, light bedspread, duvet cover, 100g quilt, 300g quilt,</span></span></span></span></span></pre>
# <p><span style="font-size: 14px; font-family: verdana, arial, helvetica; color: #404348;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">bed pillowcases, furnishing cushions, tablecloths, napkins, chair covers, placemats, coasters, furnishing towels, dressing gowns, aprons.</span></span></span></span></span></p>
# <p><span style="font-size: 12px;"><em><span style="font-family: verdana, arial, helvetica; color: #404348;"><strong><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;">NB</span></span></span></span></strong><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"><span style="vertical-align: inherit;"> Use the search on the homepage to find all the products in the same line.</span></span></span></span></span></em></span></p>
# </td>
# </tr>
# </tbody>
# </table>
# '''

# html_without_css = remove_css(html)
# print(html_without_css)


# import requests

# from bs4 import BeautifulSoup

# import re

# def extract_image_urls(text):
#     # Create BeautifulSoup object for parsing HTML
#     soup = BeautifulSoup(text, 'html.parser')

#     # Find all image URLs within <img> tags
#     img_tags = soup.find_all('img')
#     img_urls_in_tags = [img['src'] for img in img_tags]

#     # Find all image URLs not within <img> tags using regular expressions
#     pattern = r'(https?://\S+\.png|https?://\S+\.jpg|https?://\S+\.jpeg|https?://\S+\.gif|https?://\S+\.bmp)'
#     img_urls_not_in_tags = re.findall(pattern, text)

#     # Filter out image URLs that are already within <img> tags
#     img_urls = [url for url in img_urls_not_in_tags if url not in img_urls_in_tags]

#     return img_urls

# # Example usage
# text = """
# https://fournil.ca/wp-content/uploads/2017/03/lefournil-58-web-1024x683.jpg<br><strong>What is levain?</strong><br>In English, levain is called sourdough. Levain is the culture of naturally occurring yeast in our environment; yeast is present on practically all surfaces, from our skin, fruits, counters, to the flour we use for baking and the air we breathe. When cultivating the yeast for bread making, water is added to flour, and this mixture is left to slowly ferment at room temperature for 5 days or so. During this time, small amounts of water and flour are added to the mix to “feed” the culture.&nbsp;When the levain is bubbly and has a pleasant order with a hint of acidity, the levain is ready for use.<br><br><strong>How to use levain to make bread?</strong><br>From this point on, the levain can be used directly in your bread recipe, or it can be used as a seed to start a different levain, according to your recipe. We refer to the levain your purchased from us as LfB (Le fournil Bakery) levain.<br>Important note: Make sure to always use a recipe scaled in grams as it is the best and most precise way of measuring ingredients, and use a digital kitchen scale (an inexpensive one will suffice). Note that one gram is a very, very small amount, so don’t be too rigid when scaling as a couple of grams won’t make a huge difference. (1 ounce = 28 grams)<br><strong>To use LfB levain as a “seed” or “starter”:</strong>
# <ul>
# <li>Scale out the amount of “seed” or “starter” as stated in your recipe and follow its directions.</li>
# <li>If you have some LfB levain left, add 25 g water and 25 g flour to it, mix by hand until the flour is absorbed, and place it in an airtight container in your refrigerator until you need it next.</li>
# </ul>
# <strong>To use it as is in a recipe:</strong>
# <ul>
# <li>Scale out the total amount of levain in the recipe from your LfB levain and follow the recipe’s directions.</li>
# <li>If you have some LfB levain left, feed it, and store it as mentioned above.</li>
# </ul>
# <strong>To use LfB levain from the refrigerator:</strong>
# <ul>
# <li>Take out the levain from the refrigerator 8 to 12 hours before using it.</li>
# <li>Feed it in the proportions of ½ flour and ½ warm water of the total amount of levain you will need in the recipe (either as a starter or as the total amount of levain).</li>
# </ul>
# <strong>How long can I keep levain?</strong><br>You can keep your levain in your refrigerator, in an airtight container, for up to one week. If you want to keep it longer, take it out after the week, feed it 25 g flour and 25 g warm water and leave it out overnight. Feed it again (same quantities) in the morning and put it back in the refrigerator. The longer the levain stays in the refrigerator, the more sour and acidic it will become; try to use your levain at least once a week.<br>Alternatively, use up all the levain when you receive it and purchase more the next time you want to make bread.<br>Levain will be ready to use 8 to 12 hours after feeding it and leaving it at room temperature. It will die off sometime after being left 18 to 24 hours at room temperature without being fed.<br>There is a LOT more to say about levain, but this information should get you started.<br><strong>Happy baking!</strong>
# """

# image_urls = extract_image_urls(text)
# for url in image_urls:
#     print(url)

# from bs4 import BeautifulSoup

# def extract_href_values(html_text):
#     # Create BeautifulSoup object
#     soup = BeautifulSoup(html_text, 'html.parser')

#     # Find all <a> tags
#     a_tags = soup.find_all('a')

#     # Extract href attribute values
#     href_values = [a.get('href') for a in a_tags]

#     return href_values

# html_text = """
# Votre éventail Véra Pilo mérite un sac de protection de qualité. Celui-ci est fabriqué en France, à la main, par une maison réputée par son savoir-faire.

# <a href="https://verapilo.com/categorie-produit/accessoires/sacs-a-sac/">VOIR TOUS LES SACS À SAC</a>
# """

# href_values = extract_href_values(html_text)

# # Print the href attribute values
# for href in href_values:
#     print(href)    


# import json
# import re
# def modify_product_data(data):
#         try:
#             data = json.loads(sql_unescape(data.strip('"')))
#         except:
#             data = json.loads(data.strip('"'))
#         return data
# def sql_unescape(text: str):
#         replace_data = {
#             r"\"": r'"',
#             r"\\\"": r"\"",
#             r"\%": r"%",
#             r"\\\\/": r"/",
#             r'\\"': r"\"",
#         }
#         pattern = re.compile("|".join(re.escape(key) for key in replace_data.keys()))
#         return pattern.sub(lambda match: replace_data[match.group(0)], text)


# val = '''{"@product-id": "ABS-RB", "ean": null, "upc": "841249115380", "unit": null, "unit-quantity": "0", "min-order-quantity": "1", "step-quantity": "1", "display-name": {"@xml:lang": "x-default", "#text": "Airbrush Stylus with No-Mess Tip"}, "short-description": {"@xml:lang": "x-default", "#text": "<p>This detailed airbrush stylus features industry-leading, professional beauty technology giving you the most precise application using the unique Soft-touch No-Mess tip. \r\n</p>"}, "long-description": {"@xml:lang": "x-default", "#text": "<p>LUMINESS brings you industry-leading, professional beauty technology with the most precise airbrush stylus featuring the unique Soft-touch No-Mess Tip applicator. Our unique design gives you complete control with no overspray and no mess. The perfect tool to achieve flawless long-lasting coverage, whether it\u2019s for personal use or for your beauty clients. \r\n</p>"}, "store-force-price-flag": "false", "store-non-inventory-flag": "false", "store-non-revenue-flag": "false", "store-non-discountable-flag": "false", "online-flag": ["false", {"@site-id": "Luminess_Beauty", "#text": "true"}], "available-flag": "true", "searchable-flag": ["true", {"@site-id": "Luminess_Beauty", "#text": "true"}], "images": {"image-group": [{"@view-type": "hi-res", "image": [{"@path": "HiRes/Rose-Gold-And-Black New-Stylus-WIth-NoMess/Product/1_1500_Airbrush_Rose_Gold_And_Black_New_Stylus_With_No_Mess_TIp.jpg"}, {"@path": "HiRes/Systems/Icon/Product/2_1500_Icon_Airbrush_System_Black.jpeg"}, {"@path": "HiRes/Stylus/1500_Airbrush_Stylus_No_Mess_tip.jpg"}, {"@path": "HiRes/Systems/Icon/Product/5_1500_Icon_Airbrush_System_Stylus.jpg"}, {"@path": "HiRes/Systems/Icon/Product/7_1500_Icon_Airbrush_System_Stylus.jpg"}]}, {"@view-type": "large", "image": {"@path": "LargeImages/Rose-Gold-And-Black-New-Stylus-WIth-No-Mess/Product/1_350__Airbrush_Rose_Gold_And_Black_New_Stylus_With_No_Mess_TIp_1.jpg"}}]}, "sitemap-included-flag": {"@site-id": "Luminess_Beauty", "#text": "true"}, "page-attributes": {"page-title": {"@xml:lang": "x-default", "#text": "Get Airbrush Stylus with No-Mess Tip | Luminess Cosmetics"}, "page-description": {"@xml:lang": "x-default", "#text": "Say goodbye to messy airbrushing with the luminess no-mess airbrush makeup machine stylus tip for a flawless look with ease. Order now at luminess cosmetic."}, "page-keywords": {"@xml:lang": "x-default", "#text": "Airbrush Makeup Machine"}}, "custom-attributes": {"custom-attribute": [{"@attribute-id": "GTIN", "#text": "00841249115380"}, {"@attribute-id": "allowBundleCustomization", "#text": "true"}, {"@attribute-id": "autoDeliveryEligible", "#text": "true"}, {"@attribute-id": "dimHeight", "#text": "5.5"}, {"@attribute-id": "dimLength", "#text": "2.875"}, {"@attribute-id": "dimWeight", "#text": "2.72"}, {"@attribute-id": "dimWidth", "#text": "1.062"}, {"@attribute-id": "enableTrialOption", "#text": "true"}, {"@attribute-id": "form", "#text": "Airbrush"}, {"@attribute-id": "googleProductCat", "#text": "2548"}, {"@attribute-id": "googleTaxonomy", "#text": "Health & Beauty > Personal Care > Cosmetics > Cosmetic Tools > Makeup Tools"}, {"@attribute-id": "hasshelflife", "#text": "24"}, {"@attribute-id": "inGoogleFeed", "#text": "true"}, {"@attribute-id": "isHazardous", "#text": "false"}, {"@attribute-id": "isNew", "#text": "false"}, {"@attribute-id": "isSale", "#text": "false"}, {"@attribute-id": "longName", "#text": "Airbrush Stylus with No-Mess Tip"}, {"@attribute-id": "paymentOption", "#text": "both"}, {"@attribute-id": "productVideo", "value": "https://res.cloudinary.com/luminess/video/upload/v1612198624/LuminessCosmetics/PDPVideo/How-To_Airbrush_Stylist_ibigvr.mp4"}, {"@attribute-id": "productVideoimages", "value": "https://res.cloudinary.com/luminess/image/upload/v1611892121/LuminessCosmetics/PDPVideo/Thumbnails/HOW-TO-TBN.jpg"}, {"@attribute-id": "quickDescription", "#text": "Target skin imperfections and achieve even coverage"}, {"@attribute-id": "refinementColor", "value": ["Gold", "Pink"]}, {"@attribute-id": "shortName", "#text": "Airbrush Stylus with No-Mess Tip"}, {"@attribute-id": "tabDescription", "#text": "<video id=\"pdp-vid\" height=\"343px\" width=\"100\%\" controls=\"\" poster=\"https://res.cloudinary.com/luminess/image/upload/v1612286114/LuminessCosmetics/Video-Logo/350x350_logo-link.png\" class=\"pdp-video\">\r\n<source src=\"https://res.cloudinary.com/luminess/video/upload/v1612198624/LuminessCosmetics/PDPVideo/How-To_Airbrush_Stylist_ibigvr.mp4\"> Your browser does not support\r\nvideo.</video>\r\n\r\n\r\n\r\n<ul>\r\n\t<li>Start by putting 6-8 drops of your favorite airbrush product into the well.</li>\r\n\t<li>Next, turn on your system and gently pull back on the trigger to release the product keeping your stylus moving for even coverage!</li>\r\n\t<li>Finish by passing over the entire face again or only in those areas where you'd like a little more.&nbsp;</li>\r\n</ul>"}, {"@attribute-id": "tabDetails", "#text": "<p><strong>What it is:</strong> This stylus makes product application easy and ensures accuracy. The precise tip allows you to target certain imperfections and achieve even coverage.</p>\r\n\r\n<p><strong>What it does:</strong> Our unique design gives you complete control with no overspray and no mess. A high-quality tool that helps cover imperfections with great precision? Sign me up!</p>\r\n\r\n<p><strong>Why you'll love it:</strong> Feel in control and confident in your application and enjoy effectively covering imperfections leaving no mess on your Stylus.</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>Compatible with Icon, Icon Pro and Legend Airbrush Systems</p>"}, {"@attribute-id": "usewith", "value": ["LMCLSB60", "STYTL-GEN"]}]}, "classification-category": {"@catalog-id": "luminess-beauty-storefront", "#text": "airbrush-accesories"}, "pinterest-enabled-flag": "false", "facebook-enabled-flag": "false", "store-attributes": {"force-price-flag": "false", "non-inventory-flag": "false", "non-revenue-flag": "false", "non-discountable-flag": "false"}}'''        
# val = modify_product_data(val)
# print(val)
# import xmltodict
# import json
# def convert_xml_to_json(xml_data):
#     # Parse XML into a dictionary
#     data_dict = xmltodict.parse(xml_data)

#     # Convert the dictionary to JSON
#     json_data = json.dumps(data_dict)

#     return json_data

# string= '''

#     <product product-id="BRZRH-GEN">
#         <ean/>
#         <upc/>
#         <unit/>
#         <unit-quantity>0</unit-quantity>
#         <min-order-quantity>1</min-order-quantity>
#         <step-quantity>1</step-quantity>
#         <display-name xml:lang="x-default">Breeze Airbrush Haircare Root &amp; Hair Cover-Up Kit</display-name>
#         <short-description xml:lang="x-default">Featuring an exclusive No-Mess Tip, the BREEZE offers control and precision during application for the most natural results that blend seamlessly with your hair. The LUMINESS BREEZE Airbrush Haircare System dramatically enhances your haircare routine by using proven technology to transform concentrated hair color formulas into a micro droplet mist. This mist is then precisely propelled directly onto your scalp &amp; hair where the active ingredients can be absorbed and deliver results. Discover the difference of Air-Delivered Beauty from the industry leading makers of Airbrush Beauty technology for almost 25 years.&lt;/p&gt;</short-description>
#         <long-description xml:lang="x-default">Featuring an exclusive No-Mess Tip, the BREEZE offers control and precision during application for the most natural results that blend seamlessly with your hair. The LUMINESS BREEZE Airbrush Haircare System dramatically enhances your haircare routine by using proven technology to transform concentrated hair color formulas into a micro droplet mist. This mist is then precisely propelled directly onto your scalp &amp; hair where the active ingredients can be absorbed and deliver results. Discover the difference of Air-Delivered Beauty from the industry leading makers of Airbrush Beauty technology for almost 25 years.&lt;/p&gt;</long-description>
#         <store-force-price-flag>false</store-force-price-flag>
#         <store-non-inventory-flag>false</store-non-inventory-flag>
#         <store-non-revenue-flag>false</store-non-revenue-flag>
#         <store-non-discountable-flag>false</store-non-discountable-flag>
#         <online-flag>true</online-flag>
#         <online-flag site-id="Luminess_Beauty">true</online-flag>
#         <available-flag>false</available-flag>
#         <searchable-flag>false</searchable-flag>
#         <images>
#             <image-group view-type="hi-res">
#                 <image path="HiRes/Airbrush_Haircare/Device_Kit/1_1500_Root-Hair-Cover-Up_Device-Kit_Brunette.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Model/1500_Airbrush_Haircare_Model_Brunette-1.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/2_Pack/1_1500_Airbrush_Root-Hair-Cover-Up_2-Pack_Brunette.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Light_Brown/1_1500_Airbrush_Root-&amp;-Hair-Cover-Up_Light-Brown.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Light_Brown/3_1500_Airbrush_Root-Hair-Cover-Up_Hair-Swatch_Light-Brown.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Light_Brown/2_1500_Airbrush_Root-Hair-Cover-Up_Swatch_Light-Brown.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Medium_Brown/1_1500_Airbrush_Root-&amp;-Hair-Cover-Up_Medium-Brown.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Medium_Brown/3_1500_Airbrush_Root-Hair-Cover-Up_Hair-Swatch_Medium-Brown.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Medium_Brown/2_1500_Airbrush_Root-Hair-Cover-Up_Swatch_Medium-Brown.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Before_and_Afters/1500_Airbrush_Root_and_Hair_BNA-1.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Before_and_Afters/1500_Airbrush_Root_and_Hair_BNA-3.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Before_and_Afters/1500_Airbrush_Root_and_Hair_BNA-4.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup_with-Hand.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup_Back.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup-Angle.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup_Top-View.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Model/1500_Airbrush_Haircare_Model_DarkBlonde-1.jpg"/>
#             </image-group>
#             <image-group view-type="hi-res" variation-value="Auburn">
#                 <image path="HiRes/Airbrush_Haircare/Device_Kit/1_1500_Root-Hair-Cover-Up_Device-Kit_Auburn.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Model/1500_Airbrush_Haircare_Model_Brunette-1.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/2_Pack/1_1500_Airbrush_Root-Hair-Cover-Up_2-Pack_Auburn.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Light_Red/1_1500_Airbrush_Root-&amp;-Hair-Cover-Up_Light-Red.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Light_Red/3_1500_Airbrush_Root-Hair-Cover-Up_Hair-Swatch_Light-Red.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Light_Red/2_1500_Airbrush_Root-Hair-Cover-Up_Swatch_Light-Red.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Dark_Red/1_1500_Airbrush_Root-&amp;-Hair-Cover-Up_Dark-Red.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Dark_Red/3_1500_Airbrush_Root-Hair-Cover-Up_Hair-Swatch_Dark-Red.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Dark_Red/2_1500_Airbrush_Root-Hair-Cover-Up_Swatch_Dark-Red.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Before_and_Afters/1500_Airbrush_Root_and_Hair_BNA-1.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Before_and_Afters/1500_Airbrush_Root_and_Hair_BNA-3.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Before_and_Afters/1500_Airbrush_Root_and_Hair_BNA-4.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup_with-Hand.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup_Back.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup-Angle.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup_Top-View.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Model/1500_Airbrush_Haircare_Model_DarkBlonde-1.jpg"/>
#             </image-group>
#             <image-group view-type="hi-res" variation-value="Black">
#                 <image path="HiRes/Airbrush_Haircare/Device_Kit/1_1500_Root-Hair-Cover-Up_Device-Kit_Black.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Model/1500_Airbrush_Haircare_Model_Brunette-1.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/2_Pack/1_1500_Airbrush_Root-Hair-Cover-Up_2-Pack_Black.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Jet_Black/1_1500_Airbrush_Root-&amp;-Hair-Cover-Up_Jet-Black.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Jet_Black/3_1500_Airbrush_Root-Hair-Cover-Up_Hair-Swatch_Jet-Black.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Jet_Black/2_1500_Airbrush_Root-Hair-Cover-Up_Swatch_Jet-Black.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Charcoal/1_1500_Airbrush_Root-&amp;-Hair-Cover-Up_Charcoal.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Charcoal/3_1500_Airbrush_Root-Hair-Cover-Up_Hair-Swatch_Charcoal.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Charcoal/2_1500_Airbrush_Root-Hair-Cover-Up_Swatch_Charcoal.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Before_and_Afters/1500_Airbrush_Root_and_Hair_BNA-1.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Before_and_Afters/1500_Airbrush_Root_and_Hair_BNA-3.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Before_and_Afters/1500_Airbrush_Root_and_Hair_BNA-4.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup_with-Hand.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup_Back.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup-Angle.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup_Top-View.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Model/1500_Airbrush_Haircare_Model_DarkBlonde-1.jpg"/>
#             </image-group>
#             <image-group view-type="hi-res" variation-value="Blonde">
#                 <image path="HiRes/Airbrush_Haircare/Device_Kit/1_1500_Root-Hair-Cover-Up_Device-Kit_Blonde.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Model/1500_Airbrush_Haircare_Model_Brunette-1.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/2_Pack/1_1500_Airbrush_Root-Hair-Cover-Up_2-Pack_Blonde.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Light_Blonde/1_1500_Airbrush_Root-&amp;-Hair-Cover-Up_Light-Blonde.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Light_Blonde/3_1500_Airbrush_Root-Hair-Cover-Up_Hair-Swatch_Light-Blonde.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Light_Blonde/2_1500_Airbrush_Root-Hair-Cover-Up_Swatch_Light-Blonde.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Dark_Blonde/1_1500_Airbrush_Root-&amp;-Hair-Cover-Up_Dark-Blonde.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Dark_Blonde/3_1500_Airbrush_Root-Hair-Cover-Up_Hair-Swatch_Dark-Blonde.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Dark_Blonde/2_1500_Airbrush_Root-Hair-Cover-Up_Swatch_Dark-Blonde.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Device_Kit/1500_Airbrush_Breeze-2-Makeup-Device.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Before_and_Afters/1500_Airbrush_Root_and_Hair_BNA-3.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Before_and_Afters/1500_Airbrush_Root_and_Hair_BNA-1.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Before_and_Afters/1500_Airbrush_Root_and_Hair_BNA-4.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup_with-Hand.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup_Back.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup-Angle.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup_Top-View.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Model/1500_Airbrush_Haircare_Model_DarkBlonde-1.jpg"/>
#             </image-group>
#             <image-group view-type="hi-res" variation-value="Brunette">
#                 <image path="HiRes/Airbrush_Haircare/Device_Kit/1_1500_Root-Hair-Cover-Up_Device-Kit_Brunette.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Model/1500_Airbrush_Haircare_Model_Brunette-1.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/2_Pack/1_1500_Airbrush_Root-Hair-Cover-Up_2-Pack_Brunette.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Light_Brown/1_1500_Airbrush_Root-&amp;-Hair-Cover-Up_Light-Brown.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Light_Brown/3_1500_Airbrush_Root-Hair-Cover-Up_Hair-Swatch_Light-Brown.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Light_Brown/2_1500_Airbrush_Root-Hair-Cover-Up_Swatch_Light-Brown.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Medium_Brown/1_1500_Airbrush_Root-&amp;-Hair-Cover-Up_Medium-Brown.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Medium_Brown/3_1500_Airbrush_Root-Hair-Cover-Up_Hair-Swatch_Medium-Brown.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Medium_Brown/2_1500_Airbrush_Root-Hair-Cover-Up_Swatch_Medium-Brown.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Before_and_Afters/1500_Airbrush_Root_and_Hair_BNA-1.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Before_and_Afters/1500_Airbrush_Root_and_Hair_BNA-3.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Before_and_Afters/1500_Airbrush_Root_and_Hair_BNA-4.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup_with-Hand.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup_Back.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup-Angle.jpg"/>
#                 <image path="HiRes/Airbrush_Systems/Breeze/Haircare/1500_Airbrush_Breeze_Makeup_Top-View.jpg"/>
#                 <image path="HiRes/Airbrush_Haircare/Model/1500_Airbrush_Haircare_Model_DarkBlonde-1.jpg"/>
#             </image-group>
#             <image-group view-type="large">
#                 <image path="HiRes/Airbrush_Haircare/Device_Kit/1_350_Root-Hair-Cover-Up_Device-Kit_Brunette.jpg"/>
#             </image-group>
#             <image-group view-type="large" variation-value="Auburn">
#                 <image path="HiRes/Airbrush_Haircare/Device_Kit/1_350_Root-Hair-Cover-Up_Device-Kit_Auburn.jpg"/>
#             </image-group>
#             <image-group view-type="large" variation-value="Black">
#                 <image path="HiRes/Airbrush_Haircare/Device_Kit/1_350_Root-Hair-Cover-Up_Device-Kit_Black.jpg"/>
#             </image-group>
#             <image-group view-type="large" variation-value="Blonde">
#                 <image path="HiRes/Airbrush_Haircare/Device_Kit/1_350_Root-Hair-Cover-Up_Device-Kit_Blonde.jpg"/>
#             </image-group>
#             <image-group view-type="large" variation-value="Brunette">
#                 <image path="HiRes/Airbrush_Haircare/Device_Kit/1_350_Root-Hair-Cover-Up_Device-Kit_Brunette.jpg"/>
#             </image-group>
#             <image-group view-type="swatch">
#                 <image path="HiRes/Airbrush_Haircare/Device_Kit/Swatches/Root-Hair-Cover-Up_Color-Swatch_Brunette.jpg"/>
#             </image-group>
#             <image-group view-type="swatch" variation-value="Auburn">
#                 <image path="HiRes/Airbrush_Haircare/Device_Kit/Swatches/Root-Hair-Cover-Up_Color-Swatch_Auburn.jpg"/>
#             </image-group>
#             <image-group view-type="swatch" variation-value="Black">
#                 <image path="HiRes/Airbrush_Haircare/Device_Kit/Swatches/Root-Hair-Cover-Up_Color-Swatch_Black.jpg"/>
#             </image-group>
#             <image-group view-type="swatch" variation-value="Blonde">
#                 <image path="HiRes/Airbrush_Haircare/Device_Kit/Swatches/Root-Hair-Cover-Up_Color-Swatch_Blonde.jpg"/>
#             </image-group>
#             <image-group view-type="swatch" variation-value="Brunette">
#                 <image path="HiRes/Airbrush_Haircare/Device_Kit/Swatches/Root-Hair-Cover-Up_Color-Swatch_Brunette.jpg"/>
#             </image-group>
#         </images>
#         <page-attributes/>
#         <custom-attributes>
#             <custom-attribute attribute-id="description1">&lt;div class="row home-page-v2-main skin-care-dt-mb-com"&gt;&#13;
# &lt;div class="sys-container skin-care-mob-p-0"&gt;&#13;
# &lt;div class="row"&gt;&#13;
# &lt;div class="col-lg-12 mt-5"&gt;&#13;
#     &lt;span class="d-lg-block d-none"&gt;&#13;
#     &lt;img class="w-100" src="https://res.cloudinary.com/luminess/image/upload/v1657653898/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_banner.jpg"&gt;&#13;
#     &lt;/span&gt;&#13;
#     &lt;span class="d-lg-none d-block"&gt;&#13;
#     &lt;img class="w-100" src="https://res.cloudinary.com/luminess/image/upload/v1657653868/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/mobile/haircare_upgrade_kit_banner.jpg"&gt;&#13;
#     &lt;/span&gt;&#13;
# &lt;/div&gt;&#13;
# &#13;
# &lt;div class="col-lg-6 my-lg-5 vertical-center"&gt;&#13;
# &lt;div class="image-side-description ml-lg-3"&gt;&#13;
# &lt;p class="tabDescription-main-title"&gt;WHY IT WORKS&lt;/p&gt;&#13;
# &#13;
# &lt;p class="new-product-description"&gt;Our Breeze Haircare Airbrush has been designed to transform hair-mimicking pigments to an ultra-controlled and precise soft spray mist allowing you to target gray roots, thinning hair, and even add highlights and lowlights.&lt;/p&gt;&#13;
# &lt;span class="d-lg-block d-none"&gt;&#13;
#     &lt;img class="w-100" src="https://res.cloudinary.com/luminess/image/upload/v1657653899/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_why_it_works_icon.jpg"&gt;&#13;
# &lt;/span&gt;&#13;
# &lt;span class="d-lg-none d-block"&gt;&#13;
#     &lt;img class="w-100" src="https://res.cloudinary.com/luminess/image/upload/v1657653868/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/mobile/haircare_upgrade_kit_why_it_works_icon.jpg"&gt;&#13;
# &lt;/span&gt;&#13;
# &lt;/div&gt;&#13;
# &lt;/div&gt;&#13;
# &#13;
# &lt;div class="col-lg-6 text-right my-lg-5 mt-4"&gt;&#13;
# &lt;div class="d-lg-block d-none"&gt;&#13;
# &lt;picture&gt; &lt;source class="w-100" data-srcset="https://res.cloudinary.com/luminess/image/upload/v1657653899/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_why_it_works_model.webp" loading="lazy" type="image/webp" srcset="https://res.cloudinary.com/luminess/image/upload/v1657653899/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_why_it_works_model.webp"&gt; &lt;img alt="" class="w-100 lazyloaded" data-src="https://res.cloudinary.com/luminess/image/upload/v1657653899/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_why_it_works_model.jpg" loading="lazy" src="https://res.cloudinary.com/luminess/image/upload/v1657653899/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_why_it_works_model.jpg"&gt; &lt;/picture&gt;&#13;
# &lt;/div&gt;&#13;
# &lt;div class="d-lg-none d-block"&gt;&#13;
# &lt;picture&gt; &lt;source class="w-100" data-srcset="https://res.cloudinary.com/luminess/image/upload/v1657653868/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/mobile/haircare_upgrade_kit_why_it_works_image.webp" loading="lazy" type="image/webp"&gt; &lt;img alt="" class="w-100 lazyload" data-src="https://res.cloudinary.com/luminess/image/upload/v1657653868/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/mobile/haircare_upgrade_kit_why_it_works_image.jpg" loading="lazy"&gt; &lt;/picture&gt;&#13;
# &lt;/div&gt;&#13;
# &lt;/div&gt;&#13;
# &lt;div class="d-flex skin-care-every-concern-mob"&gt;&#13;
# &lt;div class="col-lg-6 text-right mt-lg-5 mt-4"&gt;&#13;
# &lt;div class="d-lg-block d-none"&gt;&#13;
# &lt;picture&gt; &lt;source class="w-100" data-srcset="https://res.cloudinary.com/luminess/image/upload/v1657653898/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_concern_image.webp" loading="lazy" type="image/webp" srcset="https://res.cloudinary.com/luminess/image/upload/v1657653898/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_concern_image.webp"&gt; &lt;img alt="" class="w-100 lazyloaded" data-src="https://res.cloudinary.com/luminess/image/upload/v1657653898/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_concern_image.jpg" loading="lazy" src="https://res.cloudinary.com/luminess/image/upload/v1657653898/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_concern_image.jpg"&gt; &lt;/picture&gt;&#13;
# &lt;/div&gt;&#13;
# &lt;div class="d-lg-none d-block"&gt;&#13;
# &lt;picture&gt; &lt;source class="w-100" data-srcset="https://res.cloudinary.com/luminess/image/upload/v1657653867/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/mobile/haircare_upgrade_kit_concern_image.webp" loading="lazy" type="image/webp"&gt; &lt;img alt="" class="w-100 lazyload" data-src="https://res.cloudinary.com/luminess/image/upload/v1657653867/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/mobile/haircare_upgrade_kit_concern_image.jpg" loading="lazy"&gt; &lt;/picture&gt;&#13;
# &lt;/div&gt;&#13;
# &lt;/div&gt;&#13;
# &#13;
# &lt;div class="col-lg-6 vertical-center sec-skin-loving-formula-main free-trial-skin-loving-sec"&gt;&#13;
# &lt;p class="tabDescription-main-title mb-4 w-100"&gt;HAIRCARE FOR EVERY CONCERN&lt;/p&gt;&#13;
# &lt;div class="pb-2 mb-0"&gt;&#13;
# &lt;div class="row no-gutters"&gt;&#13;
# &lt;div class="col-lg-2 col-2 pt-lg-2 pr-lg-3 mob-skin-care-concern-icon"&gt;&#13;
# &lt;span class="d-lg-block d-none"&gt;&#13;
# &lt;picture&gt; &lt;source class="img-fluid" data-srcset="https://res.cloudinary.com/luminess/image/upload/v1657653898/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_concern_icon_1.webp" loading="lazy" type="image/webp" srcset="https://res.cloudinary.com/luminess/image/upload/v1657653898/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_concern_icon_1.webp"&gt; &lt;img alt="" class="img-fluid lazyloaded" data-src="https://res.cloudinary.com/luminess/image/upload/v1657653898/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_concern_icon_1.jpg" loading="lazy" src="https://res.cloudinary.com/luminess/image/upload/v1657653898/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_concern_icon_1.jpg"&gt; &#13;
# &lt;/picture&gt;&#13;
# &lt;/span&gt;&#13;
# &lt;span class="d-lg-none d-block"&gt;&#13;
# &lt;picture&gt; &lt;source class="img-fluid" data-srcset="https://res.cloudinary.com/luminess/image/upload/v1657653867/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/mobile/haircare_upgrade_kit_concern_icon_1.webp" loading="lazy" type="image/webp"&gt; &lt;img alt="" class="img-fluid lazyload" data-src="https://res.cloudinary.com/luminess/image/upload/v1657653867/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/mobile/haircare_upgrade_kit_concern_icon_1.jpg" loading="lazy"&gt; &#13;
# &lt;/picture&gt;&#13;
# &lt;/span&gt;&#13;
# &lt;/div&gt;&#13;
# &#13;
# &lt;div class="col-lg-10 col-10"&gt;&#13;
# &lt;div&gt;&#13;
# &lt;div class="sec-skin-loving-formula-title"&gt;100\% WATER-BASED HAIRCARE&lt;/div&gt;&#13;
# &#13;
# &lt;p class="sec-skin-loving-formula-description mb-0"&gt;Formulated with hair-mimicking pigments evenly and precisely applied with airbrush to provide easy, fast, and long-lasting coverage.&lt;/p&gt;&#13;
# &lt;/div&gt;&#13;
# &lt;/div&gt;&#13;
# &lt;/div&gt;&#13;
# &lt;/div&gt;&#13;
# &#13;
# &lt;div class="pb-2 my-3"&gt;&#13;
# &lt;div class="row no-gutters"&gt;&#13;
# &lt;div class="col-lg-2 col-2 pt-lg-2 pr-lg-3 mob-skin-care-concern-icon"&gt;&#13;
# &lt;span class="d-lg-block d-none"&gt;&#13;
# &lt;picture&gt; &lt;source class="img-fluid" data-srcset="https://res.cloudinary.com/luminess/image/upload/v1657653898/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_concern_icon_2.webp" loading="lazy" type="image/webp" srcset="https://res.cloudinary.com/luminess/image/upload/v1657653898/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_concern_icon_2.webp"&gt; &lt;img alt="" class="img-fluid lazyloaded" data-src="https://res.cloudinary.com/luminess/image/upload/v1657653898/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_concern_icon_2.jpg" loading="lazy" src="https://res.cloudinary.com/luminess/image/upload/v1657653898/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_concern_icon_2.jpg"&gt; &#13;
# &lt;/picture&gt;&#13;
# &lt;/span&gt;&#13;
# &lt;span class="d-lg-none d-block"&gt;&#13;
# &lt;picture&gt; &lt;source class="img-fluid" data-srcset="https://res.cloudinary.com/luminess/image/upload/v1657653867/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/mobile/haircare_upgrade_kit_concern_icon_2.webp" loading="lazy" type="image/webp"&gt; &lt;img alt="" class="img-fluid lazyload" data-src="https://res.cloudinary.com/luminess/image/upload/v1657653867/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/mobile/haircare_upgrade_kit_concern_icon_2.jpg" loading="lazy"&gt; &#13;
# &lt;/picture&gt;&#13;
# &lt;/span&gt;&#13;
# &lt;/div&gt;&#13;
# &#13;
# &lt;div class="col-lg-10 col-10"&gt;&#13;
# &lt;div&gt;&#13;
# &lt;div class="sec-skin-loving-formula-title"&gt;FILLS &amp; COVERS&lt;/div&gt;&#13;
# &#13;
# &lt;p class="sec-skin-loving-formula-description mb-0"&gt;Instantly achieve the look of volume, cover grays or simply add fun highlights &amp; more to dramatically transform your look easily and effortlessly.&lt;/p&gt;&#13;
# &lt;/div&gt;&#13;
# &lt;/div&gt;&#13;
# &lt;/div&gt;&#13;
# &lt;/div&gt;&#13;
# &#13;
# &lt;div class="pb-2 mb-0"&gt;&#13;
# &lt;div class="row no-gutters"&gt;&#13;
# &lt;div class="col-lg-2 col-2 pt-lg-2 pr-lg-3 mob-skin-care-concern-icon"&gt;&#13;
# &lt;span class="d-lg-block d-none"&gt;&#13;
# &lt;picture&gt; &#13;
# &lt;source class="img-fluid" data-srcset="https://res.cloudinary.com/luminess/image/upload/v1657653898/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_concern_icon_3.webp" loading="lazy" type="image/webp" srcset="https://res.cloudinary.com/luminess/image/upload/v1657653898/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_concern_icon_3.webp"&gt; &#13;
# &lt;img alt="" class="img-fluid lazyloaded" data-src="https://res.cloudinary.com/luminess/image/upload/v1657653898/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_concern_icon_3.jpg" loading="lazy" src="https://res.cloudinary.com/luminess/image/upload/v1657653898/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_concern_icon_3.jpg"&gt; &#13;
# &lt;/picture&gt;&#13;
# &lt;/span&gt;&#13;
# &lt;span class="d-lg-none d-block"&gt;&#13;
# &lt;picture&gt; &#13;
# &lt;source class="img-fluid" data-srcset="https://res.cloudinary.com/luminess/image/upload/v1657653867/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/mobile/haircare_upgrade_kit_concern_icon_3.webp" loading="lazy" type="image/webp"&gt; &#13;
# &lt;img alt="" class="img-fluid lazyload" data-src="https://res.cloudinary.com/luminess/image/upload/v1657653867/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/mobile/haircare_upgrade_kit_concern_icon_3.jpg" loading="lazy"&gt; &#13;
# &lt;/picture&gt;&#13;
# &lt;/span&gt;&#13;
# &lt;/div&gt;&#13;
# &#13;
# &lt;div class="col-lg-10 col-10"&gt;&#13;
# &lt;div&gt;&#13;
# &lt;div class="sec-skin-loving-formula-title"&gt;FORMULATED FOR ALL HAIR TYPES &amp; SHADES&lt;/div&gt;&#13;
# &#13;
# &lt;p class="sec-skin-loving-formula-description mb-0"&gt;LUMINESS Root &amp; Hair Cover-Up is formulated to look like natural healthy hair. Blend and mix any of our adapting 9 shades for the most real color match.&lt;/p&gt;&#13;
# &lt;/div&gt;&#13;
# &lt;/div&gt;&#13;
# &lt;/div&gt;&#13;
# &lt;/div&gt;&#13;
# &#13;
# &lt;/div&gt;&#13;
# &lt;/div&gt;&#13;
# &lt;div class="col-lg-12 my-lg-5"&gt;&#13;
# &lt;p class="tabDescription-main-title text-center" style="margin-left: 0 !important; text-align: center !important;"&gt;HAIR-LOVING FORMULAS&lt;/p&gt;&#13;
# &lt;span class="d-lg-block d-none"&gt;&#13;
# &lt;img class="w-100" src="https://res.cloudinary.com/luminess/image/upload/v1657653898/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/desktop/haircare_upgrade_kit_loving_formulas.jpg"&gt;&#13;
# &lt;/span&gt;&lt;/div&gt;&#13;
# &lt;span class="d-lg-none d-block"&gt;&#13;
# &lt;img class="w-100" src="https://res.cloudinary.com/luminess/image/upload/v1657653868/LuminessCosmetics/PDP/Haircare/Root_and_Hair_Upgrade_Kit/mobile/haircare_upgrade_kit_loving_formulas.jpg"&gt;&#13;
# &lt;/span&gt;&lt;/div&gt;&#13;
# &lt;/div&gt;&#13;
# &lt;/div&gt;</custom-attribute>
#             <custom-attribute attribute-id="form">Liquid</custom-attribute>
#             <custom-attribute attribute-id="googleProductCat">8452</custom-attribute>
#             <custom-attribute attribute-id="googleTaxonomy">Health &amp; Beauty &gt; Personal Care &gt; Hair Care &gt; Hair Care Kits</custom-attribute>
#             <custom-attribute attribute-id="longName">Breeze Airbrush Haircare Root &amp; Hair Cover-Up Kit</custom-attribute>
#             <custom-attribute attribute-id="maxQuantityPerCart">1</custom-attribute>
#             <custom-attribute attribute-id="productVideo">
#                 <value>https://res.cloudinary.com/luminess/video/upload/v1658175248/Haircare-makeup/Desktop/PDPVideo/Root_HairPDPVId_pdggyv.mp4</value>
#             </custom-attribute>
#             <custom-attribute attribute-id="productVideoimages">
#                 <value>https://res.cloudinary.com/luminess/image/upload/v1658177754/LuminessCosmetics/PDPVideo/Thumbnails/HOW-TO-TBN4.png</value>
#             </custom-attribute>
#             <custom-attribute attribute-id="quickDescription">Instantly cover gray roots and fill in thinning areas</custom-attribute>
#             <custom-attribute attribute-id="shortName">Breeze Airbrush Haircare Root &amp; Hair Cover-Up Kit</custom-attribute>
#             <custom-attribute attribute-id="tabAutoDelivery">&lt;p style="padding: 0 30px" &gt;Your starter kit includes two bottles of Airbrush Skincare Formula and comes with our convenient membership program with auto-delivery.&lt;/p&gt;&#13;
# &#13;
# &lt;p style="padding: 0 30px" &gt;Your first auto-delivery will ship 30 days after you receive your initial order with your selected shades. Your auto-delivery shipment is based on the membership that you enrolled in at the time of your purchase. Please refer to your order confirmation for payment and billing details. Membership will be billed monthly as indicated in your order confirmation includes the following exclusive benefits:&lt;/p&gt;&#13;
# &#13;
# &lt;ul style="margin-left: 40px;padding: 0 30px;"&gt;&#13;
#     &lt;li&gt;LUMINESS Care extended device warranty that covers accidental damage, repairs, and parts for your airbrush system ($175 value)&lt;/li&gt;&#13;
#     &lt;li&gt;Access to a FREE replacement airbrush stylus every 6 months (up to $198 value)&lt;/li&gt;&#13;
#     &lt;li&gt;Access to a FREE replacement of your existing airbrush device every year (up to $240 value) or a discounted offer to upgrade to the latest system&lt;/li&gt;&#13;
#     &lt;li&gt;Get your orders faster! Skip to the front of the line with priority order processing&lt;/li&gt;&#13;
#     &lt;li&gt;Priority access to premium customer care support with a dedicated toll-free line&lt;/li&gt;&#13;
#     &lt;li&gt;Unlimited access to makeup artists to get beauty advice, discover new looks and shop products&lt;/li&gt;&#13;
#     &lt;li&gt;Never pay full price again! Save up to 80\% on full-size cosmetics with your member-only discount - COMING SOON&lt;/li&gt;&#13;
#     &lt;li&gt;Earn store credit for each month you&amp;rsquo;re a member to use towards product - COMING SOON&lt;/li&gt;&#13;
# &lt;/ul&gt;&#13;
# &#13;
# &lt;p style="padding: 0 30px" &gt;&lt;br /&gt;&#13;
# Promotional pricing is only applicable with auto-delivery. Early cancellation of auto-delivery will result in price adjustments - regular price will apply. To customize this program or future shipments, call customer service toll-free 1-877-749-5777.&lt;/p&gt;</custom-attribute>
#             <custom-attribute attribute-id="tabDescription">&lt;p&gt;&#13;
# &lt;video class="pdp-video" controls="" height="343px" id="pdp-vid" poster="https://res.cloudinary.com/luminess/image/upload/q_auto/v1612286114/LuminessCosmetics/Video-Logo/350x350_logo-link.png" width="100\%"&gt;&lt;source src="https://res.cloudinary.com/luminess/video/upload/v1658175248/Haircare-makeup/Desktop/PDPVideo/Root_HairPDPVId_pdggyv.mp4" /&gt; Your browser does not support video.&lt;/video&gt;&#13;
# &lt;/p&gt;&#13;
# &#13;
# &lt;p&gt;&lt;strong&gt;How to Use&lt;/strong&gt;&lt;/p&gt;&#13;
# &#13;
# &lt;ul style="margin-left: 40px;"&gt;&#13;
#     &lt;li&gt;Separation is normal, shake product well to ensure it's fully mixed.&lt;/li&gt;&#13;
#     &lt;li&gt;Dispense 6-8 drops of chosen color into the product well.&lt;/li&gt;&#13;
#     &lt;li&gt;Gently pull back on the device trigger to release product onto hair.&amp;nbsp;&lt;/li&gt;&#13;
# &lt;/ul&gt;&#13;
# &#13;
# &lt;hr /&gt;&#13;
# &lt;p&gt;&lt;strong&gt;Application&lt;/strong&gt;&lt;/p&gt;&#13;
# &#13;
# &lt;ul style="margin-left: 40px;"&gt;&#13;
#     &lt;li&gt;For root coverage and thinning areas, move in circular motions spraying light layers until desired coverage is achieved.&amp;nbsp;&lt;/li&gt;&#13;
#     &lt;li&gt;For highlights, move in vertical motions spraying several light layers on to desired area.&amp;nbsp;&lt;/li&gt;&#13;
#     &lt;li&gt;Clean airbrush stylus head after each use following the cleaning instructions.&lt;/li&gt;&#13;
# &lt;/ul&gt;&#13;
# &#13;
# &lt;hr /&gt;&#13;
# &lt;p&gt;&lt;strong&gt;Battery Charging&amp;nbsp;-&amp;nbsp;&lt;/strong&gt;ENSURE DEVICE IS FULLY CHARGED FOR 4&amp;nbsp;HOURS BEFORE USE FOR OPTIMAL PERFORMANCE.&lt;/p&gt;&#13;
# &#13;
# &lt;ul style="margin-left: 40px;"&gt;&#13;
#     &lt;li&gt;To charge, connect charging cable into a USB charging box.&lt;/li&gt;&#13;
#     &lt;li&gt;Remove silicone stopper from charging port and connect charging cable onto USB charging port on base of device.&lt;/li&gt;&#13;
#     &lt;li&gt;Power button light will blink during charging.&lt;/li&gt;&#13;
#     &lt;li&gt;When indicator light stops blinking and turns on, the system has been fully charged.&lt;/li&gt;&#13;
#     &lt;li&gt;Device battery indicator light will flash red when the batter power has been depleted.&lt;/li&gt;&#13;
# &lt;/ul&gt;&#13;
# &#13;
# &lt;hr /&gt;&#13;
# &lt;p&gt;&lt;strong&gt;Multi-Speed Setting&lt;/strong&gt;&lt;/p&gt;&#13;
# &#13;
# &lt;ul style="margin-left: 40px;"&gt;&#13;
#     &lt;li&gt;1- Speed:&amp;nbsp;Press ON/OFF button once to turn device on and activate first speed&lt;/li&gt;&#13;
#     &lt;li&gt;&lt;i&gt;LED light will illuminate solid&lt;/i&gt;&lt;/li&gt;&#13;
#     &lt;li&gt;2-Speed*:&amp;nbsp;Press ON/OFF button twice to&amp;nbsp;turn device to activate two speed&lt;/li&gt;&#13;
#     &lt;li&gt;&lt;i&gt;Both LED lights will illuminate solid&lt;/i&gt;&lt;/li&gt;&#13;
#     &lt;li&gt;Clean mode*:&amp;nbsp;Press and hold the ON/OFF button until LED lights turn on or for about 5 seconds&lt;/li&gt;&#13;
#     &lt;li&gt;&lt;i&gt;All LED lights will illuminate and blink&lt;/i&gt;&lt;/li&gt;&#13;
# &lt;/ul&gt;&#13;
# &#13;
# &lt;p&gt;*Available in select models&lt;/p&gt;&#13;
# &#13;
# &lt;hr /&gt;&#13;
# &lt;p&gt;&lt;strong&gt;How to Clean&amp;nbsp;&lt;/strong&gt;&lt;/p&gt;&#13;
# &#13;
# &lt;ul style="margin-left: 40px;"&gt;&#13;
#     &lt;li&gt;Place eight (8) drops of water or Cleaning Solution into product well. The solution will loosen and dissolve left over makeup or skincare. If you don&amp;rsquo;t have Cleaning Solution run warm to hot water through your system stylus after each use.&lt;/li&gt;&#13;
#     &lt;li&gt;Activate clean mode* by pressing and holding power button until LED lights turn on for about 5 seconds.&amp;nbsp;Place index finger over airbrush nozzle to block airflow. Gently pull back on airbrush trigger up to the heavy setting so small bubbles appear in product well. Back bubble for 8-15 seconds depending on level of cleaning needed. Back bubbling aerates and clears airbrush makeup or skincare inside the stylus.&lt;/li&gt;&#13;
#     &lt;li&gt;Pull back trigger to heavy setting to flush out product onto a tissue or into a bathroom sink.&lt;/li&gt;&#13;
#     &lt;li&gt;Remove any makeup or skincare from product well with a soft cotton swab. Do not apply excessive pressure to airbrush needle running through bottom of makeup well as this may damage your airbrush stylus.&lt;/li&gt;&#13;
# &lt;/ul&gt;&#13;
# &#13;
# &lt;p&gt;&lt;br /&gt;&#13;
# &lt;strong&gt;TIP: To Prevent Clogs &amp;amp; Splattering&lt;/strong&gt;&lt;/p&gt;&#13;
# &#13;
# &lt;ul style="margin-left: 40px;"&gt;&#13;
#     &lt;li&gt;Fill product well half way with Tip Top Cleaning Solution&lt;/li&gt;&#13;
#     &lt;li&gt;Let sit overnight&lt;/li&gt;&#13;
#     &lt;li&gt;Spray out completely before next use&lt;/li&gt;&#13;
# &lt;/ul&gt;&#13;
# &#13;
# &lt;hr /&gt;&#13;
# &lt;p&gt;&lt;strong&gt;Breeze Airbrush Care&lt;/strong&gt;&lt;/p&gt;&#13;
# &#13;
# &lt;p&gt;&amp;nbsp;&lt;/p&gt;&#13;
# &#13;
# &lt;p&gt;&#13;
# &lt;video controls="" height="343px" id="pdp-vid" poster="https://res.cloudinary.com/luminess/image/upload/q_auto/v1612286114/LuminessCosmetics/Video-Logo/350x350_logo-link.png" width="100\%"&gt;&lt;source src="https://res.cloudinary.com/luminess/video/upload/v1657570807/LuminessCosmetics/PDPVideo/breeze-cleaning-how-to-video-desktop_miw5jq.mp4" /&gt; Your browser does not support video.&lt;/video&gt;&#13;
# &lt;/p&gt;&#13;
# &#13;
# &lt;p&gt;*Available in select models&lt;/p&gt;&#13;
# &#13;
# &lt;p&gt;&amp;nbsp;&lt;/p&gt;&#13;
# &#13;
# &lt;p&gt;Explore more great tutorial videos by clicking &lt;a href="https://www.luminesscosmetics.com/on/demandware.store/Sites-Luminess_Beauty-Site/default/Tutorials-Show"&gt;HERE&lt;/a&gt;&amp;nbsp;&lt;/p&gt;&#13;
# &#13;
# &lt;p&gt;&amp;nbsp;&lt;/p&gt;</custom-attribute>
#             <custom-attribute attribute-id="tabDetails">&lt;p&gt;&lt;strong&gt;What it is:&lt;/strong&gt; The BREEZE applies haircare products&amp;nbsp;in an ultra-fine mist for flawless application and improved skin absorption. Featuring an exclusive No-Mess Tip, the BREEZE offers control and precision during application for the most natural results that blend seamlessly with your hair.&amp;nbsp;&lt;/p&gt;&#13;
# &#13;
# &lt;p&gt;&lt;strong&gt;What it included:&amp;nbsp;&lt;/strong&gt;&lt;/p&gt;&#13;
# &#13;
# &lt;ul style="margin-left: 40px;"&gt;&#13;
#     &lt;li&gt;Breeze Haircare&amp;nbsp;Airbrush Device&lt;/li&gt;&#13;
#     &lt;li&gt;2 bottles - 0.50 oz Root &amp;amp; Hair Cover-Up in 2 shades&#13;
#     &lt;ul style="margin-left: 40px;"&gt;&#13;
#         &lt;li&gt;Blonde | Dark Blonde, Light Blonde&lt;/li&gt;&#13;
#         &lt;li&gt;Auburn&amp;nbsp;| Dark Red, Light Red&lt;/li&gt;&#13;
#         &lt;li&gt;Brunette | Light Brown, Medium Brown&lt;/li&gt;&#13;
#         &lt;li&gt;Black | Jet Black, Charcoal&lt;/li&gt;&#13;
#     &lt;/ul&gt;&#13;
#     &lt;/li&gt;&#13;
#     &lt;li&gt;Charging Cable&lt;/li&gt;&#13;
#     &lt;li&gt;1-Year Warranty&lt;/li&gt;&#13;
#     &lt;li&gt;$90 of On-Line Training&lt;/li&gt;&#13;
#     &lt;li&gt;Live Product Support&lt;/li&gt;&#13;
#     &lt;li&gt;FREE GIFT: Breeze Airbrush Makeup Stylus Head&lt;/li&gt;&#13;
# &lt;/ul&gt;&#13;
# &#13;
# &lt;p&gt;&lt;br /&gt;&#13;
# &lt;strong&gt;What is does:&lt;/strong&gt;&amp;nbsp;Extend the time between color treatments by expertly covering&amp;nbsp;fast-growing gray roots while restoring beautiful,&amp;nbsp;natural-looking color at the roots.&amp;nbsp;&lt;/p&gt;&#13;
# &#13;
# &lt;p&gt;&lt;strong&gt;Why You'll love it:&lt;/strong&gt; This formula is great to touch up your roots in between color sessions and blends&amp;nbsp;in your color at the root for seamless transition from your natural hair to your colored hair and even blurs the thinning areas.&lt;/p&gt;&#13;
# &#13;
# &lt;p&gt;&amp;nbsp;&lt;/p&gt;&#13;
# &#13;
# &lt;hr /&gt;&#13;
# &lt;p dir="ltr"&gt;&amp;nbsp;&lt;/p&gt;&#13;
# &#13;
# &lt;p dir="ltr"&gt;&lt;strong&gt;WARNINGS: Use Only as Directed&lt;/strong&gt;&lt;/p&gt;&#13;
# &#13;
# &lt;p&gt;&lt;b&gt;IMPORTANT BATTERY WARNING&lt;/b&gt;&lt;/p&gt;&#13;
# &#13;
# &lt;ul style="margin-left: 40px;"&gt;&#13;
#     &lt;li&gt;ENSURE DEVICE IS FULLY CHARGED FOR 4 HOURS BEFORE USE FOR OPTIMAL PERFORMANCE.&lt;/li&gt;&#13;
#     &lt;li&gt;This product contains Li-Ion batteries and should be recycled or disposed of per local and state guidelines.&lt;/li&gt;&#13;
#     &lt;li&gt;Do not expose or dispose of this device in fire.&lt;/li&gt;&#13;
#     &lt;li&gt;Charging or storing at temperatures below 40&amp;ordm;F or higher than 95&amp;ordm;F adversely affects lifetime of battery.&lt;/li&gt;&#13;
# &lt;/ul&gt;&#13;
# &#13;
# &lt;p&gt;&lt;br /&gt;&#13;
# &lt;b&gt;WHEN NOT TO USE&lt;/b&gt;&lt;/p&gt;&#13;
# &#13;
# &lt;ul style="margin-left: 40px;"&gt;&#13;
#     &lt;li&gt;The LUMINESS BREEZE Airbrush System is designed for cosmetic use only.&lt;/li&gt;&#13;
#     &lt;li&gt;Do not use the LUMINESS BREEZE Airbrush System on skin that is infected, irritated, burned, cut, or otherwise compromised.&lt;/li&gt;&#13;
#     &lt;li&gt;Wait until the skin area has healed before beginning or continuing use.&lt;/li&gt;&#13;
#     &lt;li&gt;The LUMINESS BREEZE Airbrush System should be kept out of the reach of children.&lt;/li&gt;&#13;
#     &lt;li&gt;The LUMINESS BREEZE Airbrush System should not be used while driving, operating machinery, or during any activity where use may put the user at undue risk of injury.&lt;/li&gt;&#13;
# &lt;/ul&gt;&#13;
# &#13;
# &lt;p&gt;&lt;br /&gt;&#13;
# &lt;b&gt;DANGER&lt;/b&gt;&lt;/p&gt;&#13;
# &#13;
# &lt;p&gt;To reduce the risk of electric shock:&lt;/p&gt;&#13;
# &#13;
# &lt;ul style="margin-left: 40px;"&gt;&#13;
#     &lt;li&gt;Do not reach for a LUMINESS System that is charging and has fallen into water.&lt;/li&gt;&#13;
#     &lt;li&gt;Do not immerse LUMINESS System in water or use in shower.&lt;/li&gt;&#13;
#     &lt;li&gt;Do not place or store the LUMINESS System where it can fall or be pulled into a tub or sink.&lt;/li&gt;&#13;
#     &lt;li&gt;Do not use an extension cord with LUMINESS System&lt;/li&gt;&#13;
#     &lt;li&gt;Unplug and remove power supply cord from LUMINESS System before cleaning.&lt;/li&gt;&#13;
# &lt;/ul&gt;&#13;
# &#13;
# &lt;p&gt;&lt;br /&gt;&#13;
# &lt;b&gt;IMPORTANT SAFETY CONCERNS&lt;/b&gt;&lt;/p&gt;&#13;
# &#13;
# &lt;p&gt;To reduce the risk of burns, fire, electric shock, or injury to persons:&lt;/p&gt;&#13;
# &#13;
# &lt;ul style="margin-left: 40px;"&gt;&#13;
#     &lt;li&gt;Never operate the LUMINESS System if it has a damaged cord, if it is not working properly, if it has been dropped or damaged, or dropped into water while plugged in.&lt;/li&gt;&#13;
#     &lt;li&gt;Keep LUMINESS System and charging cord away from heated surfaces.&lt;/li&gt;&#13;
#     &lt;li&gt;Never drop or insert any object into any opening.&lt;/li&gt;&#13;
#     &lt;li&gt;Never put the LUMINESS System in direct sunlight or store at a temperature above 140&amp;deg;F.&lt;/li&gt;&#13;
#     &lt;li&gt;Keep the LUMINESS System and cord dry at all times. Do not handle with wet hands. Do not store in a damp environment.&lt;/li&gt;&#13;
#     &lt;li&gt;Never attempt to open any part of the device.&lt;/li&gt;&#13;
#     &lt;li&gt;To prevent possible damage to the cord, do not wrap cord around the LUMINESS System.&lt;/li&gt;&#13;
# &lt;/ul&gt;&#13;
# &#13;
# &lt;p&gt;&amp;nbsp;&lt;/p&gt;&#13;
# &#13;
# &lt;p&gt;&lt;b&gt;Please read and fully understand user manual before operation.&lt;/b&gt;&lt;/p&gt;&#13;
# &#13;
# &lt;p&gt;This device is solely intended for use on face. Any harmful consequences resulting from misuse or application to other body areas, or any other improper applications is neither responsibility of LUMINESS Direct, LLC nor its affiliates.&lt;/p&gt;</custom-attribute>
#             <custom-attribute attribute-id="tabIngredients">Purified Water, Glycerin, PEG-8 / SMDI Copolymer, Stearic Acid, Phenoxyethanol, Triethanolamine, Glyceryl Stearate, PEG-100 Stearate, Tocopheryl Acetate, Butylene Glycol, Potassium Sorbate, Disodium EDTA, Lecithin, Kaolin Propylene Glycol, Iodopropynyl Butylcarbamate, Diazolidinyl Urea | May Contain (+/-): Mica (CI 77019), Titanium Dioxide (CI 77891), Iron Oxides (CI 77491, CI 77492, CI 77499), Yellow 5 Lake (CI 19140)</custom-attribute>
#             <custom-attribute attribute-id="usewith">
#                 <value>LMRHHL-GEN</value>
#                 <value>CLS01-GEN</value>
#             </custom-attribute>
#         </custom-attributes>
#         <variations>
#             <attributes>
#                 <variation-attribute attribute-id="color" variation-attribute-id="color">
#                     <display-name xml:lang="x-default">color</display-name>
#                     <variation-attribute-values>
#                         <variation-attribute-value value="Black">
#                             <display-value xml:lang="x-default">Black</display-value>
#                             <description xml:lang="x-default">Black</description>
#                         </variation-attribute-value>
#                         <variation-attribute-value value="Brunette">
#                             <display-value xml:lang="x-default">Brunette</display-value>
#                             <description xml:lang="x-default">Brunette</description>
#                         </variation-attribute-value>
#                         <variation-attribute-value value="Auburn">
#                             <display-value xml:lang="x-default">Auburn</display-value>
#                             <description xml:lang="x-default">Auburn</description>
#                         </variation-attribute-value>
#                         <variation-attribute-value value="Blonde">
#                             <display-value xml:lang="x-default">Blonde</display-value>
#                             <description xml:lang="x-default">Blonde</description>
#                         </variation-attribute-value>
#                     </variation-attribute-values>
#                 </variation-attribute>
#             </attributes>
#             <variants>
#                 <variant product-id="BRZRH-BND"/>
#                 <variant product-id="BRZRH-BRU"/>
#                 <variant product-id="BRZRH-AUB"/>
#                 <variant product-id="BRZRH-BLK"/>
#             </variants>
#         </variations>
#         <classification-category catalog-id="luminess-beauty-storefront">hidden</classification-category>
#         <pinterest-enabled-flag>false</pinterest-enabled-flag>
#         <facebook-enabled-flag>false</facebook-enabled-flag>
#         <store-attributes>
#             <force-price-flag>false</force-price-flag>
#             <non-inventory-flag>false</non-inventory-flag>
#             <non-revenue-flag>false</non-revenue-flag>
#             <non-discountable-flag>false</non-discountable-flag>
#         </store-attributes>
#     </product>




# '''    
# print(convert_xml_to_json(string))    
# string = '''
# Vendor Name in Shopify is,Vendor Name in RMS is
# Michael Aram,Aram
# Bao Bao,
# Branch,
# Cody Foster,Cody Foster & Co/Backporch
# Creative Candles,
# Dezso,
# Dinosaur Designs,
# Edward Wohl,
# Gigi Clozeau,
# Hibi,
# Hirotaka,
# Jamie Joseph,
# Jane Diaz,
# Jennie Kwon Designs,
# Joe Cariati,
# John Iversen,
# Joseph Brooks,
# Klein Reid,KleinReid
# Laura Zindel,
# Lena Skadegard,
# Leo Sewell,
# Lobmeyr,
# Luis Morais,
# Maria Tash,
# Mateo,
# MQuan,
# Nightingale Design,
# Nymphenburg,
# Pascale Monvoisin,
# Pean Doubulyu Glass,
# Romulus Craft,
# Sarah McGuire,Sarah Mcguire
# Shihara,
# Silvia Furmanovich,
# Simon Pearce,
# Sola Cube,
# Spencer Peterman,
# Stephanie Windsor Vintage,Stephanie Windsor
# Tai,Tai Rittichai
# Ted Muehling,
# Terrafirma Ceramics,
# Thomas Glenn Holidays,
# Valerie Casado,
# Variance Objects,Variance
# Welded,
# Yuta Segawa,
# Zoë Chicco,Zoe Chicco
# Alex Sepkus,
# Alice Cicolini,
# Almasika,
# Amali,
# Anaconda,
# Anita Ko,
# Anna Maccieri Rossi,
# Annette Ferdinandsen,
# Annie Fensterstock,
# Ark,Ark and Arrows
# Artëmer,Artemer
# Bea Bongiasca,
# Bea Bongiasca X Wolf,
# Brent Neale,
# Brooke Gregson,
# Castro Smith,
# Cathy Waterman,
# Celine Daoust,
# Danielle Welmond,
# Digby & Iona,
# Disa Allsopp,
# Dorette,
# Elizabeth Street,
# Emanuela Duca,Emanuela Duca Inc
# Erika Winters,
# Eva Fehren,
# Fernando Jorge,
# Fiat Lux,
# Foundrae,
# Francesca Villa,Francisca Villa
# Fraser Hamilton,
# Futura,
# Grace Lee,Grace Lee Designs
# Grainne Morton,
# Harwell Godfrey,
# Ila,ila&i
# Isabel Borland,
# Jill Platner,
# Johnny Ninos,
# Judy Geib,Judy Geib + Alpha
# Kathleen Whitaker,
# Kloto,
# Kothari Elements,
# Lunar Rain,
# Maiden Voyage,
# Mallary Marks,
# Mandrel Studio,mandrel studio
# Marian Maurer,
# Marie Lichtenberg,
# Marie-Hélène de Taillac,
# Melissa Kaye,
# Milamore,
# Moritz Glik,
# Morphe Jewelry,
# Have A Heart x Muse,Muse- Have A Heart
# Nak Armstrong,
# Nicole Landaw,
# Nikolle Radi,
# Noor Fares,
# Pat Flynn,Pat Flynn Inc
# Persée,Persee
# Pippa Small,
# Polly Wales,
# Prounis,
# Rebecca Overman,
# Retrouvai,
# Rosa Maria,
# Rosanne Pugliese,
# Rusty Thought,
# Sauer,
# Sevan,
# Shamballa Jewels,Shamballa
# Sia Taylor,
# Sophie Billie Brahe,Sophie Brahe
# Sorellina,
# Spinelli Kilcollin,
# Storrow,
# TenThousandThings,Ten Thousand Things
# The Moonstoned,
# Todd Pownell,
# Trove,
# Tura Sugden,
# Venyx,
# White/Space,
# '''

# # print(string.split('\n'))
# rsl ={}
# for row in string.split('\n'):
#     if row:
#         rsl[row.split(',')[0]] = row.split(',')[1] 
# # print(rsl)
# print(rsl.get('Bao Bao'))        

# print(32%26)
# def shift_letters(letters, parar_shift):
#     shift = parar_shift
#     if shift >= len(letters):
#         shift =  shift%len(letters)
#         print(shift)
#     rsl = []
#     for index in range(len(letters)):

#         if index + shift < len(letters):
#              rsl.append(letters[index + shift])
#         else:
#             i = index + shift - len(letters) 
#             rsl.append(letters[i])
#     return rsl
# letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# print(len(letters))
# print(shift_letters(letters,32))    






# def encrypt_simple(word, shift):
#     letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     if shift >= len(letters):
#         shift =  shift%len(letters)
#     rsl = []
#     for index in range(len(word)):
#         if word[index].upper() not in letters:
#             rsl.append(letters[i])


#         if letters.index(word[index]) + shift < len(letters):
#              rsl.append(letters[letters.index(word[index]) + shift])
#         else:
#             i = letters.index(word[index]) + shift - len(letters) 
#             rsl.append(letters[i])
#     return ''.join(rsl)

# print(encrypt_simple("DATAWARS", 5))

# # IFYFBFWX    
# # IFYFJFWX


# def decrypt_simple(word, shift):
#     letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     if shift >= len(letters):
#         shift =  shift%len(letters)
#     rsl = []
#     for index in range(len(word)):
#         if abs(letters.index(word[index]) - shift)  < len(letters):
#              rsl.append(letters[letters.index(word[index]) - shift])
#         else:
#             i = letters.index(word[index]) - shift - len(letters) 
#             rsl.append(letters[i])
#     return ''.join(rsl)

# print(decrypt_simple("PMFMIMDE", -14))    

# def encrypt_full(word, shift):
#     letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     if shift >= len(letters):
#         shift =  shift%len(letters)
#     rsl = []
#     for index in range(len(word)):
#         if word[index].upper() not in letters:
#             rsl.append(word[index])
#             continue

#         if letters.index(word[index].upper()) + shift < len(letters):
#              rsl.append(letters[letters.index(word[index].upper()) + shift]  if  word[index].isupper() else  letters[letters.index(word[index].upper()) + shift].lower() )
#         else:
#             i = letters.index(word[index].upper()) + shift - len(letters) 
#             rsl.append(letters[i]  if  word[index].isupper() else  letters[i].lower()  )
#     return ''.join(rsl)

# print(encrypt_full("MY FAVORITE WEBSITE IS DATAWARS SO MANY GREAT PROJECTS", 9))


# def decrypt_full(word, shift):
#     letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     if shift >= len(letters):
#         shift =  shift%len(letters)
#     rsl = []
#     for index in range(len(word)):
#         if word[index].upper() not in letters:
#             rsl.append(word[index])
#             continue

#         if abs(letters.index(word[index].upper()) - shift)  < len(letters):
#              rsl.append(letters[letters.index(word[index].upper()) - shift] if word[index].isupper() else  letters[letters.index(word[index].upper()) - shift].lower()  )
#         else:
#             i = letters.index(word[index].upper()) - shift - len(letters) 
#             rsl.append(letters[i] if word[index].isupper() else letters[i].lower() )
#     return ''.join(rsl)

# print(decrypt_full('VH OJEXARCN FNKBRCN RB MJCJFJAB BX VJWH PANJC YAXSNLCB', 9))    

# def break_cipher(encrypted_message, known_word):
#     letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     lst = list( letters.index(known_word[i].upper()) for i  in range(len(known_word)))
#     shift = 0
#     for text in encrypted_message.split(' '):
#         if len(text) == len(lst):
#             correct = True
#             previos = 0
#             for i  in range(len(text)):
#                 num = letters.index(text[i].upper()) if letters.index(text[i].upper()) >  lst[i]  else len(letters) + letters.index(text[i].upper())
#                 if previos and num - lst[i] != previos:
#                     correct = False
#                     break
#                 previos = num - lst[i]

#             if     correct:
#                 shift =previos

#     if shift >= len(letters):
#         shift =  shift%len(letters)
#     rsl = []
#     word = encrypted_message
#     for index in range(len(word)):
#         if word[index].upper() not in letters:
#             rsl.append(word[index])
#             continue

#         if abs(letters.index(word[index].upper()) - shift)  < len(letters):
#              rsl.append(letters[letters.index(word[index].upper()) - shift] if word[index].isupper() else  letters[letters.index(word[index].upper()) - shift].lower()  )
#         else:
#             i = letters.index(word[index].upper()) - shift - len(letters) 
#             rsl.append(letters[i] if word[index].isupper() else letters[i].lower() )
#     return ''.join(rsl)
# print(break_cipher('VH OJEXARCN FNKBRCN RB MJCJFJAB BX VJWH PANJC YAXSNLCB', "DATAWARS"))
# 'MY FAVORITE WEBSITE IS DATAWARS SO MANY GREAT PROJECTS'
# def my_decorator(func):
#     def double_up(a,b):
#          a = func(a,b)
#          return a* 2

#     return double_up 

# @my_decorator
# def sum(a,b):
#     return a+b

# print(sum(2,3))
# import re

# regex = r"\"content\"(.*?>)\",\""

# test_str = "[mgz_pagebuilder]{\"elements\":[{\"row_type\":\"full_width_row\",\"content_position\":\"top\",\"gap_type\":\"padding\",\"content_align\":\"center\",\"device_type\":\"all\",\"background_type\":\"image\",\"background_style\":\"auto\",\"background_position\":\"center-top\",\"parallax_speed\":0.5,\"mouse_parallax_size\":30,\"mouse_parallax_speed\":10000,\"lg_background_type\":\"image\",\"lg_background_style\":\"auto\",\"lg_background_position\":\"center-top\",\"md_background_type\":\"image\",\"md_background_style\":\"auto\",\"md_background_position\":\"center-top\",\"sm_background_type\":\"image\",\"sm_background_style\":\"auto\",\"sm_background_position\":\"center-top\",\"xs_background_type\":\"image\",\"xs_background_style\":\"auto\",\"xs_background_position\":\"center-top\",\"type\":\"row\",\"id\":\"olcp5sw\",\"elements\":[{\"device_type\":\"all\",\"background_type\":\"image\",\"background_style\":\"auto\",\"background_position\":\"center-top\",\"parallax_speed\":0.5,\"mouse_parallax_size\":30,\"mouse_parallax_speed\":10000,\"lg_background_type\":\"image\",\"lg_background_style\":\"auto\",\"lg_background_position\":\"center-top\",\"md_background_type\":\"image\",\"md_background_style\":\"auto\",\"md_background_position\":\"center-top\",\"sm_background_type\":\"image\",\"sm_background_style\":\"auto\",\"sm_background_position\":\"center-top\",\"xs_background_type\":\"image\",\"xs_background_style\":\"auto\",\"xs_background_position\":\"center-top\",\"md_size\":\"\",\"xl_offset_size\":\"\",\"xl_size\":\"\",\"lg_offset_size\":\"\",\"lg_size\":\"\",\"md_offset_size\":\"\",\"sm_offset_size\":\"\",\"sm_size\":\"\",\"xs_size\":\"\",\"type\":\"column\",\"id\":\"cvviha4\",\"elements\":[{\"content\":\"<p>The <a href=\\\"https://www.discstore.com/discgolf?manufacturer=246\\\" target=\\\"_blank\\\" rel=\\\"noopener\\\">Innova</a> XCaliber is extremely fast with glide and stability. The XCaliber achieves <a href=\\\"https://www.discstore.com/discgolf/discs-discgolf?disc_type=342\\\" target=\\\"_blank\\\" rel=\\\"noopener\\\">maximum distance</a> when thrown low, flat, and hard. This is the one for confident throws in windy conditions. The XCaliber has the stability to let the biggest arms throw with full power. Great disc for sidearm throwers and those with lots of power. Can handle headwinds and throws with off axis torque. Definitely not designed for beginning players.</p>\\n<p></p>\\n<p>Plastics Available: Champion, Star</p>\",\"device_type\":\"all\",\"background_type\":\"image\",\"background_style\":\"auto\",\"background_position\":\"center-top\",\"parallax_speed\":0.5,\"mouse_parallax_size\":30,\"mouse_parallax_speed\":10000,\"lg_background_type\":\"image\",\"lg_background_style\":\"auto\",\"lg_background_position\":\"center-top\",\"md_background_type\":\"image\",\"md_background_style\":\"auto\",\"md_background_position\":\"center-top\",\"sm_background_type\":\"image\",\"sm_background_style\":\"auto\",\"sm_background_position\":\"center-top\",\"xs_background_type\":\"image\",\"xs_background_style\":\"auto\",\"xs_background_position\":\"center-top\",\"type\":\"text\",\"id\":\"b05co2r\",\"history\":false}]}]}],\"pid\":\"y0rodxksfjp6\"}[/mgz_pagebuilder]"

# matches = re.finditer(regex, test_str, re.MULTILINE)

# for matchNum, match in enumerate(matches, start=1):
	
#     print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
	
#     for groupNum in range(0, len(match.groups())):
#         groupNum = groupNum + 1
		
#         print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Parse the JSON content
# try:
#     data = json.loads(json_string)
#     # Extract the HTML content from the first text element
#     html_content = data['elements'][0]['elements'][0]['content']
#     print(html_content)
# except json.JSONDecodeError as e:
#     print("JSON decoding error:", e)


# import requests
# import hashlib
# def compare_images(url1, url2):
#     response1 = requests.get(url1)
#     response2 = requests.get(url2)

#     content1 = response1.content
#     content2 = response2.content

#     md5_1 = hashlib.md5(content1).hexdigest()
#     md5_2 = hashlib.md5(content2).hexdigest()

#     return md5_1 == md5_2

# # Example usage
# url1 = "http://45.33.0.186/customers/jay_187617/product//0/5/055241-fyiparrowheadssts_2.jpg"
# url2 = "http://45.33.0.186/customers/jay_187617/product//0/5/055241-fyiparrowheadssts_3.jpg"

# if compare_images(url1, url2):
#     print("The images are the same.")
# else:
#     print("The images are different.")

# print(sum([1,2,3,4]))


# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

# import re

# regex = r"<ul>.*?<\/h5>"

# test_str = "<div class=\\\"product-description rte\\\"><ul> <li>Round neckline</li> <li>Back button closure</li> <li>Longer back</li> <li>Back pleats</li></ul><h5>PRODUCT CODE: BBB0005345A</h5><br>Model wears: M, UK 10, EUR 38<br>Model's height: 174 cm/5'9”<br><table><br><tbody><br><tr><br><td><strong>PTP(Inches) </strong></td><br><td><strong>S</strong></td><br><td><strong>M</strong></td><br><td><strong>L</strong></td><br><td><strong>XL</strong></td><br></tr><br><tr><br><td class=\\\"caption\\\">Shoulder</td><br><td>17.5</td><br><td>18</td><br><td>18.5</td><br><td>19</td><br></tr><br><tr><br><td class=\\\"caption\\\">Bust</td><br><td>41</td><br><td>43</td><br><td>45</td><br><td>47</td><br></tr><br><tr><br><td class=\\\"caption\\\">Length</td><br><td>23</td><br><td>23.5</td><br><td>24</td><br><td>24.5</td><br></tr><br></tbody><br></table><br><strong>LOOK AFTER ME</strong><br>Machine Wash According To Instructions On Care Label.<br>Hand wash preferred.<br></div>"

# matches = re.finditer(regex, test_str, re.MULTILINE)

# for matchNum, match in enumerate(matches, start=1):
#     print(match.group()) 
	# print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = ))
	
	# for groupNum in range(0, len(match.groups())):
	#     groupNum = groupNum + 1
		
	#     print(match.group(groupNum))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.

# from bs4 import BeautifulSoup

# # Sample HTML code
# html = '''
# <ul> <li>Round neckline</li> <li>Front patch pocket</li> <li>Drop Shoulder</li> <li>U-shape hemline with side slit</li> <li>Asymmetrical hemline</li> <li>Material: Jersey</li></ul><h5>PRODUCT CODE: BTD0011704Z （ 11704 ）</h5><br><div id=\"description-1\" class=\"accordion__body no-js-accordion\" data-accordion-body=\"\"><br><div class=\"rte__table-wrapper\"><br><table class=\"single-size-guide\"><br><tbody><br><tr><br><td class=\"caption\"></td><br><td>S</td><br><td>M</td><br><td>L</td><br><td>XL</td><br></tr><br><tr><br><td class=\"caption\">Shoulder</td><br><td>20</td><br><td>21</td><br><td>21.5</td><br><td>22.5</td><br></tr><br><tr><br><td class=\"caption\">Bust</td><br><td>44</td><br><td>46</td><br><td>48</td><br><td>50</td><br></tr><br><tr><br><td class=\"caption\">Hem</td><br><td>44.5</td><br><td>46.5</td><br><td>48.5</td><br><td>50.5</td><br></tr><br><tr><br><td class=\"caption\">Length</td><br><td>43.5</td><br><td>44</td><br><td>44.5</td><br><td>45</td><br></tr><br></tbody><br></table><br> <br></div><br>Model wears: M, UK 10, EUR 38<br></div><br><div class=\"accordion__body no-js-accordion\" data-accordion-body=\"\">Model's height: 174 cm/5'9”</div><br><div data-accordion-body=\"\"></div><br><div class=\"accordion__body no-js-accordion\" data-accordion-body=\"\"><strong>LOOK AFTER ME</strong></div><br><div class=\"accordion__body no-js-accordion\" data-accordion-body=\"\">Machine Wash According To Instructions On Care Label.</div><br><div class=\"accordion__body no-js-accordion\" data-accordion-body=\"\">Hand wash preferred.</div>
# '''

# # Parse the HTML using BeautifulSoup
# soup = BeautifulSoup(html, 'html.parser')

# # Find all <div> tags and replace them with their contents
# div_tags = soup.find_all('div')
# for tag in div_tags:
#     tag.unwrap()

# # Get the modified HTML code
# modified_html = str(soup)

# print(modified_html)


# import requests as r
# res= r.get('https://store.wnpa.org/media/catalog/product/cache/f6333e4346dc23b38f5e82f23e54b03f/0/0/000051-anza-dvd-1.jpg',headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36' , 'Range': 'bytes'})
# print(res)

# def burger(name):
#     def ingredients():
#         if name == "deli":
#             return ("steak", "pastrami", "emmental")
#         elif name == "smashed":
#             return ("chicken", "nacho cheese", "jalapeno")
#         else:
#             return None

#     return ingredients

# ingr = burger("deli")


# print(ingr())


# def double(func):
#     def modify(a,b):
#         return (a+b)*2
#     return modify



# def check_value_decor(func):
#     def check_value(a,b):
#         try:
#             rsl = a + b
#             return rsl        
#         except Exception as e:
#             return 'invalid type'
#             raise e


#     return check_value
# @check_value_decor
# @double
# def add(x,y):
#     return x+y
	#return None



# def sum_of_lst(*parm):
#     return sum(parm)

# print(sum_of_lst(1,2,3,45))


# def sum_of_lst(a,b,c,d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
# sum_of_lst(*[1,2,3,4])



# a = add(2,"o")
# print(a)
# @cal_decor
# def multi(a,b):
#     return a,b

# print(multi(4,2))   







# import requests
# import base64
# import mimetypes

# def url_to_base64(image_url):
#     # Fetch the image from the URL
#     response = requests.get(image_url)
	
#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         # Get the content type from the response headers
#         content_type = response.headers.get('content-type')
		
#         # Use the content type to determine the file extension
#         file_extension = mimetypes.guess_extension(content_type) if content_type else '.png'
		
#         # Encode the image content to base64
#         base64_image = base64.b64encode(response.content)
		
#         # Convert bytes to string (if needed)
#         base64_image_str = base64_image.decode('utf-8')
		
#         # Add the file extension to the base64 string
#         base64_image_with_extension = f"data:image/{file_extension[1:]};base64,{base64_image_str}"
		
#         return base64_image_with_extension
#     else:
#         print(f"Failed to fetch the image. Status code: {response.status_code}")
#         return None

# # Example usage:
# image_url = "https://www.kah-online.com/wp-content/uploads/2023/11/uT4JddlupVdXN_9dXsG4cvgYnrsXjakMEvWM0-qj1XQ"
# base64_data = url_to_base64(image_url)

# if base64_data:
#     print(base64_data)

# lst={
#     'Michael Aram': 'Aram',
#     'Bao Bao': '',
#     'Branch': '',
#     'Cody Foster': 'Cody Foster & Co/Backporch',
#     'Darius': 'Darius Jewels',
#     'Cece Jewelry': 'Cece',
#     'Creative Candles': '',
#     'Dezso': '',
#     'Dinosaur Designs': '',
#     'Edward Wohl': '',
#     'Gigi Clozeau': '',
#     'Hibi': '',
#     'Hirotaka': '',
#     'Jamie Joseph': '',
#     'Jane Diaz': '',
#     'Jennie Kwon': 'Jennie Kwon Designs',
#     'Joe Cariati': '',
#     'John Iversen': '',
#     'Joseph Brooks': '',
#     'Klein Reid': 'KleinReid',
#     'LFrank': 'L Frank',
#     'Laura Zindel': '',
#     'Lena Skadegard': '',
#     'Leo Sewell': '',
#     'Lobmeyr': '',
#     'Luis Morais': '',
#     'Maria Tash': '',
#     'Mateo': '',
#     'MQuan': '',
#     'Nightingale Design': '',
#     'Nymphenburg': '',
#     'Pascale Monvoisin': '',
#     'Pean Doubulyu Glass': '',
#     'Romulus Craft': '',
#     'Sarah McGuire': 'Sarah Mcguire',
#     'Shihara': '',
#     'Silvia Furmanovich': '',
#     'Simon Pearce': '',
#     'Sola Cube': '',
#     'Spencer Peterman': '',
#     'Stephanie Windsor Vintage': 'Stephanie Windsor',
#     'Tai': 'Tai Rittichai',
#     'Ted Muehling': '',
#     'Terrafirma Ceramics': '',
#     'Thomas Glenn Holidays': '',
#     'Valerie Casado': '',
#     'Variance Objects': 'Variance',
#     'Welded': '',
#     'Yuta Segawa': '',
#     'Zoë Chicco': 'Zoe Chicco',
#     'Alex Sepkus': '',
#     'Alice Cicolini': '',
#     'Almasika': '',
#     'Amali': '',
#     'Anaconda': '',
#     'Anita Ko': '',
#     'Anna Maccieri Rossi': '',
#     'Annette Ferdinandsen': '',
#     'Annie Fensterstock': '',
#     'Ark': 'Ark and Arrows',
#     'Artëmer': 'Artemer',
#     'Bea Bongiasca': '',
#     'Bea Bongiasca X Wolf': '',
#     'Brent Neale': '',
#     'Brooke Gregson': '',
#     'Castro Smith': '',
#     'Cathy Waterman': '',
#     'Celine Daoust': '',
#     'Danielle Welmond': '',
#     'Digby & Iona': '',
#     'Disa Allsopp': '',
#     'Dorette': '',
#     'Elizabeth Street': '',
#     'Emanuela Duca': 'Emanuela Duca Inc',
#     'Erika Winters': '',
#     'Eva Fehren': '',
#     'Fernando Jorge': '',
#     'Fiat Lux': '',
#     'Foundrae': '',
#     'Francesca Villa': 'Francisca Villa',
#     'Fraser Hamilton': '',
#     'Futura': '',
#     'Grace Lee': 'Grace Lee Designs',
#     'Grainne Morton': '',
#     'Harwell Godfrey': '',
#     'Ila': 'ila&i',
#     'Isabel Borland': '',
#     'Jill Platner': '',
#     'Johnny Ninos': '',
#     'Judy Geib': 'Judy Geib + Alpha',
#     'Kathleen Whitaker': '',
#     'Kloto': '',
#     'Kothari Elements': '',
#     'Lunar Rain': '',
#     'Maiden Voyage': '',
#     'Mallary Marks': '',
#     'Mandrel Studio': 'mandrel studio',
#     'Marian Maurer': '',
#     'Marie Lichtenberg': '',
#     'Marie-Hélène de Taillac': '',
#     'Melissa Kaye': '',
#     'Milamore': '',
#     'Moritz Glik': '',
#     'Morphe Jewelry': '',
#     'Have A Heart x Muse': 'Muse- Have A Heart',
#     'Nak Armstrong': '',
#     'Nicole Landaw': '',
#     'Nikolle Radi': '',
#     'Noor Fares': '',
#     'Pat Flynn': 'Pat Flynn Inc',
#     'Persée': 'Persee',
#     'Pippa Small': '',
#     'Polly Wales': '',
#     'Prounis': '',
#     'Rebecca Overmann': 'Rebecca Overman',
#     'Retrouvai': '',
#     'Rosa Maria': '',
#     'Rosanne Pugliese': '',
#     'Rusty Thought': '',
#     'Sauer': '',
#     'Sevan Bicakci': 'Sevan',
#     'Shamballa Jewels': 'Shamballa',
#     'Sia Taylor': '',
#     'Sophie Billie Brahe': 'Sophie Brahe',
#     'Sorellina': '',
#     'Spinelli Kilcollin': '',
#     'Storrow': '',
#     'TenThousandThings': 'Ten Thousand Things',
#     'The Moonstoned': '',
#     'Todd Pownell': '',
#     'Trove': '',
#     'Tura Sugden': '',
#     'Venyx': '',
#     'White/Space': '',
#     'Tó Garal': 'To Garal',
#     'Under Vendor Names in Shopify': '',
# }
# rsl = {}

# for row in lst:
#     if lst[row]:
#         rsl[lst[row]] = row
# print(rsl)

# encoded_string = "â€KAGO Seriesâ€"
# cleaned_string = encoded_string.replace("â€", "”").replace("â€", "“")
# decoded_string = cleaned_string.encode('utf-8').decode('utf-8')
# print(decoded_string)

# encoded_string = "ãƒ»"
# decoded_string = encoded_string.encode('utf-16', 'replace').decode('utf-16')
# print(decoded_string)

# def repeatedString(s, n):
#     compare_string = ''
#     if n > len(s):
#         remain =   n %len(s)
#         result = [] 
#         for i in range(int(n/len(s))):
#             result.append(s) 
#         # compare_string = int(n/len(s))*s
#         compare_string = ''.join(result)
#         compare_string = compare_string + s[:remain]
#     else:
#         compare_string = s[:n] 
#     return compare_string.count('a')


# print(repeatedString('a',1000000000000))
# def minion_game(string):
#     vowels = ['A', 'E', 'I', 'O', 'U']
#     p_s  = 0
#     s = []
#     p_k = 0
#     k =  []
#     for i in range(len(string)):
#         listed = []
#         word = ''
#         for j in range(i, len(string)):
#             word = word + string[j]
#             listed.append(word)
#         if string[i] in vowels:
#             k = k + listed
#         else:
#             s = s + listed
#     p_s = count_point(s,string)
#     p_k = count_point(k,string)
#     if p_s > p_k:
#         return f"Stuart {p_s}"
#     elif p_s < p_k:
#         return f"Kevin {p_k}"
#     else:
#         return "Draw"
	
#     # your code goes here
# def count_point(lst, string):
#     point = 0
#     print(lst)    
	
#     lst = list(set(lst))
#     for row in lst:
#         # print(row)
#         point = point + string.count(row)
#         # print(string.count(row))

#     return point

# print(minion_game('123456789'))


# import re

# html_string = '''<strong>[Ingredientes Claves]</strong>
# Zinc Oxide : Protector Solar(UV), Calmante, Hidratacion
# Titanium Dioxide : Proteccion UV forma fisicamente
# Centella Asiatica Extract : Antibacteriano y Calmante, Mejorar Mancha, Elasticidad, Reducir Sebo

# <strong>[ Ingredientes ]</strong>
# Water, Cyclomethicone, Zinc Oxide, Titanium Dioxide, Propanediol, Polyglyceryl-3 Polydimethylsiloxyethyl Dimethicone, Dibutyl Adipate, Caprylyl Methicone, 1,2-Hexanediol, Disteardimonium Hectorite, Magnesium Sulfate, Hydrogen Dimethicone, Aluminum Hydroxide, Salvia Hispanica Seed Extract, C30-45 Alkyl Cetearyl Dimethicone Crosspolymer, Centella Asiatica Extract, Houttuynia Cordata Extract, Polyglyceryl-2 Dipolyhydroxystearate, Stearic Acid, Fructooligosacharides, Saccharide Hydrolysate, Citrus Aurantium Bergamia(Bergamot) Fruit Oil, Helianthus Annuus(Sunflower) Seed Oil, Ethylhexylglycerin, Pullulan, Octyldodecanol, Pelargonium Graveolens Flower Oil, Panthenol, Rosa Damascena Flower Oil, Echium Plantagineum Seed Oil, Cardiospermum Halicacabum Flower/Leaf/Vine Extract, Helianthus Annuus(Sunflower) Seed Oil, Butylene Glycol(Hidratacion Fuerte), Caprylic/Capric Triglyceride, Tocopherol, Phosphatidylcholine, Ceramide NP, Glycine, Glutamic Acid, Serine, Lysine, Alanine, Arginine, Threonine, Proline'''

# # Use regex to extract content between [Ingredientes Claves] and [ Ingredientes ]
# ingredientes_claves_match = re.search(r'<strong>\[Ingredientes Claves\](.*?)<strong>', html_string, re.DOTALL)
# ingredientes_match = re.search(r'<strong>\[ Ingredientes \](.*?)$', html_string, re.DOTALL)

# # Check if matches are found
# if ingredientes_claves_match and ingredientes_match:
#     ingredientes_claves_content = ingredientes_claves_match.group(1).strip()
#     ingredientes_content = ingredientes_match.group(1).strip()

#     print("Ingredientes Claves:")
#     print(ingredientes_claves_content)

#     print("\nIngredientes:")
#     print(ingredientes_content)
# else:
#     print("No matches found.")
# from difflib import SequenceMatcher

# string_list = [
#     "Traumfänger Dreamcatcher indianisch Deko gehäckelt blau",
#     "Traumfänger Dreamcatcher Herz indianische Deko schwarz",
#     "Traumfänger Dreamcatcher Deko Perlen pink",
#     "Traumfänger Dreamcatcher indianische Deko braun",
#     "Traumfänger Dreamcatcher indianische Deko pink",
#     "Traumfänger Dreamcatcher indianische Deko weiss",
#     "XXL Traumfänger Dreamcatcher indianisch Deko bunt",
#     "Traumfänger Dreamcatcher Deko Perlen blau"
# ]

# # Function to find the longest common word
# from difflib import SequenceMatcher

# string_list = [
#     "Traumfänger Dreamcatcher indianisch Deko gehäckelt blau",
#     "Traumfänger Dreamcatcher Herz indianische Deko schwarz",
#     "Traumfänger Dreamcatcher Deko Perlen pink",
#     "Traumfänger Dreamcatcher indianische Deko braun",
#     "Traumfänger Dreamcatcher indianische Deko pink",
#     "Traumfänger Dreamcatcher indianische Deko weiss",
#     "XXL Traumfänger Dreamcatcher indianisch Deko bunt",
#     "Traumfänger Dreamcatcher Deko Perlen blau"
# ]

# Function to find the longest common phrase
# def find_longest_common_phrase(string_list):
#     if not string_list:
#         return ""

#     # Split each string into phrases
#     phrase_lists = [s.split(" ") for s in string_list]

#     # Find the shortest phrase list
#     shortest_phrases = min(phrase_lists, key=len)
#     num_phrases = len(shortest_phrases)

#     # Compare each phrase with the shortest phrase list
#     for i in range(num_phrases):
#         for j in range(i + 1, num_phrases + 1):
#             phrase = " ".join(shortest_phrases[i:j])
#             if all(phrase in phrases for phrases in phrase_lists):
#                 return phrase

#     return ""


#     # Convert the dictionary to JSON
# string_list= ['Sony Xperia 10 - Silikon Gummi Case Metall Carbon Look rot', 'sony Xperia 10 - Silikon Gummi Case Metall Carbon Look grau', 'Sony Xperia 10 - Silikon Gummi Case Metall Carbon Look dunkelblau', 'Sony Xperia 10 - Silikon Gummi Case Metall Carbon Look schwarz']
# def find_longest_common_phrase(string_list):
#     name = string_list[0]
#     rsl = []
#     for char in name.split(' '):
#         count = 0
#         for row in string_list:
#             if char.lower() in row.lower():
#                 count = count + 1
#             else:
#                 return ' '.join(rsl)
#         if count == len(string_list):
#             rsl.append(char)
#     return ' '.join(rsl)

# longest_common_part = find_longest_common_phrase(string_list)
# print(longest_common_part)


# import requests

# url = "https://www.tijon.com/wp-json/wc/v3/products/327"

# payload = {}
# headers = {
#   'Authorization': 'Basic Y2tfYTE0ZGZhNjQzNjY5Y2Y1ZTBjYTdiZGE2ZTI2NWJmMTgxZWRlNmE5Mjpjc18xODczMWViNzczMzczMDdmM2MwYWU1ZWRmZjA5M2RhMGQzZGUzMzE2',
#   'Cookie': '__cf_bm=N93pdOiGuMMEGSawzQPX.d9esWW3qy32HuS4.QIfgD4-1705916190-1-AYi5+eryP/yuUK5T08WYYwwdE2EJm7Hvjexhs0MixS+Bv9mp7++zEQOHUkc4sk85gZ0Nh0CT2zKb6Ay6Y5xLzyY=; wpe-auth=0200c58cd254bf7e9de04afa99b0fbe04f837a35376477ff8d76eb99a5fd04da'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)



# def round_to_zero_or_five(number):
#     whole_number = int(number)  # Extract the whole number part
#     decimal_part = number - whole_number  # Extract the decimal part
#     if decimal_part:
#         final = '0'
#         if int(str(number)[-1]) >= 5:
#             final = '5'
#         return float(str(number)[:-1] + final   )

#     return number

# # Example usage
# decimal_number = 13.94
# rounded_number = round_to_zero_or_five(decimal_number)
# print(rounded_number)  # Output: 13.9


# from bs4 import BeautifulSoup
# import requests
# import json



# html_doc = requests.get('https://www.babyriddle.com/posh-peanut-boutique')
# html_doc = html_doc.text



# # Assuming you have an HTML document stored in a variable called 'html_doc'
# # and you want to filter div elements by class 'my-class'

# # Parse the HTML document using BeautifulSoup
# soup = BeautifulSoup(html_doc, 'html.parser')

# # Find all div elements with the specified class
# div_elements = soup.find_all('div', class_='banners')

# # Loop through the filtered div elements and print their contents
# for div in div_elements:
#     print(div)


# import requests

# url = "https://newsapi.org/v2/everything?q=tesla&from=2024-01-22&sortBy=publishedAt&apiKey=86dbccff88f54ab3a32a750c9c21d9da&limit=10"

# payload = {}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)



# def get_all(a,b,c):
#     print(a)


# lst = [1,2,3]
# get_all(*lst)    


# def get_min_price(phone,operators):
#     current_prefix = ''
#     min_price = 0
#     rsl = ''    
#     for row in operators:
#         for key in row:
#             if not current_prefix:
#                 current_prefix = str(key)
#             if  phone.startswith(str(key))  :
#                 if (len(str(key)) > len(current_prefix) and int(current_prefix) in row ) or ((len(str(key)) == len(current_prefix) or int(current_prefix) not in row)  and   row[key] < min_price):
#                     #change value if the element in the same dict and length > current length
#                     #or not same dict but lesser or same dict and same length and lesser 
#                     print(key)
#                     min_price = row[key]
#                     current_prefix = str(key)
#                     rsl = operators.index(row) 

#     print(min_price)
#     print(rsl)

# a  = {
#     1: 0.9,
#     268: 5.1,
#     46: 0.17,
#     4620: 0.0,
#     468: 0.15,
#     4631: 0.15,
#     4673: 0.9,
#     46732: 1.1
# }

# b = {
#     1: 0.92,
#     44: 0.5,
#     46: 0.2,
#     467: 1.0,
#     48: 1.2
# }
# operators = [a,b]
# get_min_price('123456789',operators)

#m = number of operators
#n = average of prefixes count if operators    
#o = length of phone number 
#complexcity o(o*m*n)
# test_simple_unittest.py
# import unittest

# class TestStringMethods(unittest.TestCase):

#     def test_upper(self):
#         self.assertEqual('python'.upper(), 'PYTHON')

#     def test_isupper(self):
#         self.assertTrue('PYTHON'.isupper())
#         self.assertFalse('Python'.isupper())

#     def test_islower(self):
#         self.assertTrue('PYTHON'.islower())
#         self.assertFalse('Python'.islower())

#     def test_split(self):
#         test_string = 'python is a best language'
#         self.assertEqual(test_string.split(),
#                         ['python', 'is', 'a', 'best', 'language'])
#         # check that test_string.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             test_string.split(2)

# if __name__ == '__main__':
#     unittest.main(verbosity=2)





# def find_cheapest_operator(number, price_lists):
#   """
#   This function finds the cheapest operator for a given phone number based on provided price lists.

#   Args:
#       number: The phone number to find the cheapest operator for (string).
#       price_lists: A dictionary where keys are operator names (strings) and values are dictionaries representing price lists. 
#                     Each price list dictionary maps phone number prefixes (strings) to their corresponding prices (floats).

#   Returns:
#       A tuple containing the name of the cheapest operator (string) and their price (float), 
#       or None if no operator can handle the number.
#   """
# class TrieNode:
#   def __init__(self):
#     self.children = {}  
#     self.is_word = False  
#     self.operator = None  
#     self.price = None  

# class Trie:
#   def __init__(self):
#     self.root = TrieNode()


#   def search(self, number):
#     """
#     Searches for the longest matching prefix with an associated operator and price.
#     """
#     current = self.root
#     longest_prefix = ""
#     cheapest_operator = None
#     cheapest_price = float('inf')
#     for i, char in enumerate(number):
#       if char not in current.children:
#         break
#       current = current.children[char]
#       if current.is_word:
#         longest_prefix = number[:i+1]  # Update longest prefix if a complete word is found
#         if current.price < cheapest_price:
#           cheapest_operator = current.operator
#           cheapest_price = current.price
#     return longest_prefix, cheapest_operator, cheapest_price


#   def insert(self, prefix, operator, price):
#     """
#     Inserts a prefix-operator-price combination into the trie.
#     """
#     current = self.root
#     for char in prefix:
#       if char not in current.children:
#         current.children[char] = TrieNode()
#       current = current.children[char]
#     current.is_word = True
#     current.operator = operator
#     current.price = price

# def find_cheapest_operator_trie(number, price_lists):
#   """
#   Finds the cheapest operator for a number using a trie data structure.
#   """
#   trie = Trie()
#   for operator, price_list in price_lists.items():
#     for prefix, price in price_list.items():
#       trie.insert(prefix, operator, price)

#   longest_prefix, cheapest_operator, cheapest_price = trie.search(number)

#   if cheapest_operator:
#     print(f"Cheapest operator for {number} is {cheapest_operator} with a price of ${cheapest_price:.2f} per minute.")
#   else:
#     print(f"No operator can handle phone number {number}.")

# # Example usage
# price_lists = {
#   "Operator A": {"1": 0.9, "268": 5.1, "46": 0.17, "4620": 0.0, "468": 0.15, "4631": 0.15, "4673": 0.9, "46732": 1.1},
#   "Operator B": {"1": 0.92, "44": 0.5, "46": 0.2, "467": 1.0, "48": 1.2}
# }

# number = "4673212345"

# find_cheapest_operator_trie(number, price_lists)




# def numCells(matrix):
#     count = 0
#     cols_length = len(matrix[0]) 
#     rows_length = len(matrix)
#     for i in range(rows_length):
#         for j in range(cols_length):
#             is_dominant = False
#             lst = []
#             print(matrix[i][j])
#             for x in [-1,0,1]:
#                 for y in  [-1,0,1]:
#                     new_x = i + x
#                     new_y = j + y
#                     # print("x:"+str(new_x))
#                     # print("y:"+str(new_y))
#                     if new_x < rows_length and new_x >=0 and new_y < cols_length and new_y >= 0  :
#                         # print("hrere")
#                         if matrix[i][j] > matrix[new_x][new_y]:
#                             # print(matrix[i][j])
#                             # print(matrix[new_x][new_y])
#                             is_dominant = True                   
#                         lst.append(matrix[new_x][new_y])
#             print(lst)
#             if is_dominant:
#                 count = count + 1
#     return count

# matrix = [
#     [1, 2, 7],
#     [4, 5, 6],
#     [8, 8, 9]
# ]
# print(numCells(matrix))

# def count_dominant_cells(matrix):
#     count = 0

#     # Iterate over each cell in the matrix
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             cell_value = matrix[i][j]
#             is_dominant = True

#             # Check if the current cell is smaller than any of its neighbors
#             for x in [-1, 0, 1]:
#                 for y in [-1, 0, 1]:
#                     if (
#                         i + x >= 0 and i + x < len(matrix) and
#                         j + y >= 0 and j + y < len(matrix[0]) and
#                         (x != 0 or y != 0) and  # Exclude the current cell itself
#                         matrix[i + x][j + y] >= cell_value  # Use >= to include equal values
#                     ):
#                         is_dominant = False
#                         break

#                 if not is_dominant:
#                     break

#             # Increment the count if the cell is dominant
#             if is_dominant:
#                 count += 1

#     return count

# matrix = [
#     [1, 2, 7],
#     [4, 5, 6],
#     [8, 8, 9]
# ]

# dominant_count = count_dominant_cells(matrix)
# print("Number of Dominant Cells:", dominant_count)


# import redis

# # Connect to the Redis server running in a Docker container
# r = redis.Redis(
#     host='172.17.0.2',
#     port=6379,	
#     db=0
# )

# # Ping the Redis server to test the connection
# try:
#     response = r.ping()
#     print(f"Connected to Redis server: {response}")
# except redis.exceptions.ConnectionError as e:
#     print(f"Failed to connect to Redis server: {e}")

# import pika

# # docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management

# def send_data(data):

# # RabbitMQ connection details (modify as needed)
# 	connection_parameters = pika.ConnectionParameters(host='localhost')

# 	# Connect to the RabbitMQ broker
# 	connection = pika.BlockingConnection(connection_parameters)

# 	# Create a channel
# 	channel = connection.channel()

# 	# Define the queue name
# 	queue_name = 'my_queue'
# 	# Message content
# 	message = data
# 	channel.queue_declare(queue=queue_name,durable=True ) #do this when init the queue

# 	message_properties = pika.BasicProperties(delivery_mode=1,expiration='10000')


# 	# Publish the message to the queue
# 	channel.basic_publish(exchange='', routing_key=queue_name, body=message, properties = message_properties  )

# 	print(f"Message sent: {message}")

# 	# Close the connection1
# 	connection.close()

# for i in range(100):
# 	send_data(str(i))

# send_data("Hello")

# Insertion sort in Python


# def insertionSort(array):

#     # for step in range(1, len(array)):
#     #     key = array[step]
#     #     j = step - 1
		
#     #     # Compare key with each element on the left of it until an element smaller than it is found
#     #     # For descending order, change key<array[j] to key>array[j].        
#     #     while j >= 0 and key < array[j]:
#     #         array[j + 1] = array[j]
#     #         j = j - 1
		
#     #     # Place key at after the element just smaller than it.
#     #     array[j + 1] = key
#     sorted_arr = [array[0]]
#     for i in range(1,len(array)):
#         for j in range(len(sorted_arr)):
#             if array[i] < sorted_arr[j]:
#                 sorted_arr.insert(j,array[i])
#                 break
#             if j == len(sorted_arr) -1 and array[i] >= sorted_arr[j]    :
#                 sorted_arr.append(array[i])

#         print(sorted_arr)
#     return sorted_arr

# data = [9, 5, 1, 4, 3]
# data = insertionSort(data)
# print('Sorted Array in Ascending Order:')
# print(data)




# def merge_sort(data):

#   if len(data) <= 1:
#     return data
  
#   # Divide the list into two halves
#   mid = len(data) // 2
#   left = data[:mid]
#   right = data[mid:]

#   # Recursively sort the left and right halves
#   left_sorted = merge_sort(left)
#   right_sorted = merge_sort(right)

#   # Merge the sorted halves back together
#   return merge(left_sorted, right_sorted)

# def merge(left, right):
#   merged = []
#   i = 0
#   j = 0

#   # Compare elements from both lists and insert the smaller element into the merged list
#   while i < len(left) and j < len(right):
#     if left[i] <= right[j]:
#       merged.append(left[i])
#       i += 1
#     else:
#       merged.append(right[j])
#       j += 1

#   # Add any remaining elements from either list
#   merged += left[i:]
#   merged += right[j:]

#   return merged

# # Example usage
# data = [8, 4, 2, 1, 5, 3, 6, 7]
# sorted_data = merge_sort(data)

# print("Original data:", data)
# print("Sorted data:", sorted_data)

# class test:
#     count = 0
#     def merge_sort(self,arr):
#         if self.count == 3:
#             return True
#         left = arr[:int(len(arr)/2)]
#         right = arr[int(len(arr)/2):]
#         print(left)
#         print(right)
#         self.count = self.count + 1
#         return self.merge_sort(left)  , self.merge_sort(right) #if len(right) > 1 and len(left) > 1 else ''  
	
#     # def compare(self, left, right):
#     #     rsl = []
#     #     for i in range(len(left)):
#     #         for j in range(len(right)):
#     #             if left[i] > right[j]:
#     #                 rsl

# t = test()
# lst = [8, 4, 2, 1, 5, 3, 6, 7]
# t.merge_sort(lst)


# import threading

# def count(n):
#     print(sum(list(i for i in range(n))))


# t1 = threading.Thread(target=count,args=(1000,), daemon=True)
# t2 = threading.Thread(target=count,args=(100,), daemon=True)
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# def tower_of_hanoi(n, source, destination, auxiliary):
#   if n == 1:
#     print(f"Move disk 1 from rod {source} to rod {destination}")
#     return
#   tower_of_hanoi(n-1, source, auxiliary, destination)
#   print(f"Move disk {n} from rod {source} to rod {destination}")
#   tower_of_hanoi(n-1, auxiliary, destination, source)

# # Example usage
# tower_of_hanoi(6, 1, 3, 2)

# import redis

# class users():
# 	"""docstring for ClassName"""
# 	def __init__(self, id):
# 		self.id = id
		

# # Connect to the Redis server running in a Docker container
# r = redis.Redis(
#   host='redis-12132.c1.asia-northeast1-1.gce.redns.redis-cloud.com',
#   port=12132,
#   password='gDkNtTTJyigVpg0lgF9NCY15I2tDUJTW')

# # Ping the Redis server to test the connection
# try:
#     response = r.ping()
#     print(f"Connected to Redis server: {response}")
#     # u = users(1)
#     # r.set("tested", str(u),ex=300)
#     print(eval(r.get('tested')))

# except redis.exceptions.ConnectionError as e:
#     print(f"Failed to connect to Redis server: {e}")



# def remove_dup(lst):
# 	rsl = []
# 	for i in lst:
# 		found = False
# 		for j in range(len(rsl)):
# 			if rsl[j] == i:
# 				found = True
# 				break
# 		if not found:
# 			rsl.append(i)
# 	return rsl

# print(remove_dup([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))

# import hashlib
# plaintext_password  = "1234567"

# obj = hashlib.sha256(plaintext_password.encode('utf-8'))

# hashed = obj.hexdigest()
# print(hashed)

#Use bubble sort althgorith
# def custom_sort(arr: []) -> []:
# 	for i in range(len(arr)-1):
# 		for j in range(i+1,len(arr)):
# 			if arr[i] > arr[j]:
# 				arr[i] , arr[j] = arr[j], arr[i]
# 	return arr
# # print(custom_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))

# import unittest

# class test(unittest.TestCase):
# 	def sample_test(self):
# 		samle_lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# 		is_correct = custom_sort(samle_lst) == sorted(samle_lst)
# 		self.assertTrue(is_correct)

# if __name__ == '__main__':
# 	unittest.main()


# from concurrent.futures import ThreadPoolExecutor
# import time
# import random
# from datetime import datetime , timedelta
# import threading

# thread_lock = threading.Lock()
# def log(i):
# 	exe_time = random.randint(1,5)
# 	now = datetime.now()
# 	complete_time= now + timedelta(seconds= exe_time)
# 	time.sleep(exe_time)
# 	with thread_lock:
# 		print(f"Robot {i} started at {now} and finished at {complete_time}, taking {exe_time} seconds.")


# with ThreadPoolExecutor(max_workers= 10) as exe :
# 	future = []
# 	for i in range(1,11):
# 		future_obj = exe.submit(log, i)
# 		future.append(future_obj) 
# 	for row in future:
# 		row.result()


# def fibonacii( lst: list() , i: int):
# 	# lst = [0,1]
# 	# previos = lst[-1]
# 	# ex_previous = lst[0]
# 	# while len(lst)<i:
# 	# 	current = ex_previous + previos
# 	# 	lst.append(current)
# 	# 	previos , ex_previous = current , previos
# 	# return lst[:i]
# 	if not lst:
# 		lst = [0,1]
# 	if  len(lst) < i  :
# 		lst.append(lst[-1] +lst[-2])
# 		return fibonacii(lst , i)

# 	return lst[:i]


# print(fibonacii([] ,i=10))

activity_dict = {
    'A': {'Start Time': 1, 'End Time': 2},
    'B': {'Start Time': 3, 'End Time': 5},
    'C': {'Start Time': 0, 'End Time': 6},
    'D': {'Start Time': 4, 'End Time': 7},
    'E': {'Start Time': 5, 'End Time': 9}
}

