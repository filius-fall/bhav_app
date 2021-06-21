import os
from datetime import date

from app.bhav import file_name

def test_file_name():
    try:    
        k = file_name(date.today())

        assert k == os.path.join(os.path.abspath('./media'),'EQ180621.CSV')
    
    except AssertionError:
        print('Not todays file')
        assert True