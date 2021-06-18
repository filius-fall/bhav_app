import os
from datetime import date

from app.bhav import file_name

def test_file_name():

    assert file_name(date.today()) == os.path.join(os.path.abspath('./media'),'EQ180621.CSV')