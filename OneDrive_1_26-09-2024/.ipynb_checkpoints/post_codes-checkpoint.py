import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import urllib.request
import json
import sqldf

def get_data_from_post_codes(post_code):
    
    url = "https://api.postcodes.io/postcodes/" + post_code

    url = url.replace(" ", "%20")

    try:
        contents = urllib.request.urlopen(url).read()
        data = json.loads(contents)
        df = pd.json_normalize(data['result'])
        return df
    except:
        pass