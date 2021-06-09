# from get_data import download_and_extract_csv, copy_required_to_another , returns_data_as_list,return_required_data
# import redis 
# import json

# r = redis.Redis()

# r.set('sree','hello')

# a = r.get('sree')
# r.flushall()
# # print(a)
# k = returns_data_as_list()
# for i in k:
#     key = f"BSE:{i.get('code')}:{i.get('name').strip()}"
#     print(key)
#     r.set(key,json.dumps(i))


from datetime import date
import os
import io,zipfile
from urllib.request import Request, urlopen
import csv
import redis,json,requests

r = redis.Redis()

# today = date.today()
# d1 = today.strftime("%d%m%y")
date = date(2021,6,3)
headers = {'User-Agent': 'Mozilla/5.0 (Linux Mint 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
# url = Request(url = 'http://www.bseindia.com/download/BhavCopy/Equity/EQ{:%d%m%y}_CSV.ZIP'.format(date),headers=headers)
# # print(url)

# path = os.path.join(os.getcwd(),d1+'.csv')



# def download_and_extract_csv():
#     file = urlopen(url)
    
#     # k = []
#     with zipfile.ZipFile(io.BytesIO(file.read())) as zip_file:
#             for i in zip_file.open(zip_file.namelist()[0]):
#                 print(i.decode('UTF-8'))

#     return None


# download_and_extract_csv()
BHAVCOPY_NAME = 'EQ%d%m%y_CSV'
bhavcopy_name = f'{date.strftime(BHAVCOPY_NAME)}'

url = requests.get(url = 'http://www.bseindia.com/download/BhavCopy/Equity/EQ{:%d%m%y}_CSV.ZIP'.format(date),headers=headers)
# print(url)
zip_file = zipfile.ZipFile(io.BytesIO(url.content))
csv_file = zip_file.extract('test.CSV')

# remeber to replace your code with above two lines creating a csv with this is easy

k = csv.reader(csv_file)
print(k)
