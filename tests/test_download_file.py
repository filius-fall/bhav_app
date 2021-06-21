import os
import requests
from app.bhav import download_extract_url,get_date,HEADERS

def test_download_extract_url():
    date = get_date()
    url = requests.get(url = 'http://www.bseindia.com/download/BhavCopy/Equity/EQ{:%d%m%y}_CSV.ZIP'.format(date),headers=HEADERS)
    
    assert os.path.exists(download_extract_url(url)) == True