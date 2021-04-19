import numpy as np
import pandas as pd
import requests
import datetime
import json

def get_data():
    start_date = datetime.datetime.now() - datetime.timedelta(days=30)
    start_date = start_date.strftime('%Y-%m-%d')
    r1 = requests.get('https://api.github.com/search/repositories?q=created:>{}&sort=stars&order=desc'.format(start_date))
    return r1