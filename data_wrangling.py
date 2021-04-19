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

def process_data(r1):
    r1_json = json.loads(r1.text)
    r1_df = pd.json_normalize(r1_json, record_path=['items'])
    r2_df = r1_df[['name','language']]
    language_list_df = r2_df.groupby('language').count()
    return language_list_df, r2_df
