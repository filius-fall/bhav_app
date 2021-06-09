from datetime import date
import os
import io,zipfile
from urllib.request import Request, urlopen
import csv
import redis,json,requests

r = redis.Redis()

today = date.today()
d1 = today.strftime("%d%m%y")
date = date(2021,6,3)
headers = {'User-Agent': 'Mozilla/5.0 (Linux Mint 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
# url = Request(url = 'http://www.bseindia.com/download/BhavCopy/Equity/EQ{:%d%m%y}_CSV.ZIP'.format(date),headers=headers)
# print(url)

url = requests.get(url = 'http://www.bseindia.com/download/BhavCopy/Equity/EQ{:%d%m%y}_CSV.ZIP'.format(date),headers=headers)


path = os.path.join(os.getcwd(),d1+'.csv')

FILE_NAME = f"{date.strftime('EQ%d%m%y_CSV')}"

FILE = FILE_NAME.replace('_','.')


def download_and_extract_csv():
    zip_file = zipfile.ZipFile(io.BytesIO(url.content))
    csv_file = zip_file.extract(FILE)
    
    print(FILE)
    return csv_file


download_and_extract_csv()

def return_only(csv_file):
    field = ['code', 'name', 'group','type','open', 'high', 'low', 'close']
    data_list = []
    with open(csv_file,'r') as r:

        data = csv.DictReader(r,fieldnames=field)

        for i in data:
            data_list.append(i)

        data_list.pop(0)
        for i in data_list:
            del i[None]
            i['name'] = i['name'].strip()

        # print(data_list[0])
        return data_list
# download_and_extract_csv()
# return_only(FILE)



# def copy_required_to_another():
    
#     with open(FILE,'r') as original:
#         with open(path,'w') as copy:
#             writer = csv.writer(copy)
#             data = csv.DictReader(original)

#             writer.writerow(('code', 'name', 'open', 'high', 'low', 'close'))
#             # writer.writerow(('SC_CODE', 'SC_NAME', 'OPEN', 'HIGH', 'LOW', 'CLOSE'))
#             for row in data:
#                 writer.writerow((row['SC_CODE'].strip(),row['SC_NAME'].strip(),row['OPEN'].strip(),row['HIGH'].strip(),row['LOW'].strip(),row['CLOSE'].strip()))
    
#     os.remove(FILE)
#     return None

# def returns_data_as_list():
#     data_list = []
#     data = return_only('EQ030621.CSV')
#     for line in data:
#         data_list.append(line)

#     print(data_list)
#     return data_list
# returns_data_as_list()

def return_required_data(n: int):
    k = []
    data_list = return_only(FILE)
    count = 0
    for i in data_list:
        if count < n:
            k.append(i)
            count = count + 1
        else:
            break

    print(k)
    return k

def push_values_to_redis():
    r.flushall()
    data = return_only(FILE)
    for i in data:
        key = f"BSE:{i.get('code')}:{i.get('name').strip()}"
        r.set(key,json.dumps(i))



if __name__ == "__main__":
    download_and_extract_csv()
    # copy_required_to_another()
    return_required_data(5)
