from datetime import date

from app.bhav import formatted_date

def test_formatted_date():
    assert formatted_date(date.today()) == date.today().strftime('%d-%m-%y') 