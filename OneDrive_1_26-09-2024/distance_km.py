import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import sqldf


def get_distance(df):
    R = 6373.0
    
    df['Rad_LAST_DELIVERY_LATITUDE'] = np.radians(df['LAST_DELIVERY_LATITUDE'])
    df['Rad_LAST_DELIVERY_LONGITUDE'] = np.radians(df['LAST_DELIVERY_LONGITUDE'])
    df['Rad_LAT'] = np.radians(df['LAT'])
    df['Rad_LON'] = np.radians(df['LON'])
    
    df['dlong'] = df['Rad_LAST_DELIVERY_LONGITUDE'] - df['Rad_LON']
    df['dlat'] = df['Rad_LAST_DELIVERY_LATITUDE'] - df['Rad_LAT']
    
    df['dummy_a'] = np.sin(df['dlat']/2)**2 + np.cos(df['Rad_LAST_DELIVERY_LATITUDE'])*np.cos(df['Rad_LAT'])*np.sin(df['dlong']/2)**2
    
    df['distance'] = R*2*np.arctan2(np.sqrt(df['dummy_a']), np.sqrt(1 - df['dummy_a']))
    
    df.drop(['index', 'dlong', 'dlat', 'dummy_a', 'Rad_LAST_DELIVERY_LATITUDE', 'Rad_LAST_DELIVERY_LONGITUDE', 'Rad_LAT', 'Rad_LON'],axis=1,inplace=True)
    
    return df