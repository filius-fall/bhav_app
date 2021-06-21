from app.bhav import get_scan_values

def test_get_scan_values():

    try:
        assert (len(get_scan_values(1)) > 1) and (isinstance(get_scan_values(1)[1],(dict)) )
    except AssertionError:

        assert False