from .bhav import BhavFile


def date_refresh():
    # Left space for logging
    BhavFile().perform()
    # Left space for logging