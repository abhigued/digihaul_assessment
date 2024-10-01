import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import urllib.request
import json
import sqldf

def get_data_from_lon_lat(lon, lat):
    
    url = "https://api.postcodes.io/postcodes?lon=" + str(lon) + "&lat=" + str(lat)

    url = url.replace(" ", "%20")

    try:
        contents = urllib.request.urlopen(url).read()
        data = json.loads(contents)
        df = pd.json_normalize(data['result'])
        return df
    except:
        pass