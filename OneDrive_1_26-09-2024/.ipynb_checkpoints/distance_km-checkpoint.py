import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import sqldf


def get_distance(df, lon1='LAST_DELIVERY_LONGITUDE', lat1='LAST_DELIVERY_LATITUDE', lon2='LON', lat2='LAT'):
    R = 6373.0


    rad_lon1 = 'Rad_' + lon1
    rad_lat1 = 'Rad_' + lat1
    rad_lon2 = 'Rad_' + lon2
    rad_lat2 = 'Rad_' + lat2

    new_data = {rad_lon1: np.radians(df[lon1]), rad_lat1: np.radians(df[lat1]), rad_lon2: np.radians(df[lon2]), rad_lat2: np.radians(df[lat2])}
    df = df.assign(**new_data)
    
    
    df['dlong'] = df[rad_lon1] - df[rad_lon2]
    df['dlat'] = df[rad_lat1] - df[rad_lat2]
    
    df['dummy_a'] = np.sin(df['dlat']/2)**2 + np.cos(df[rad_lat1])*np.cos(df[rad_lat2])*np.sin(df['dlong']/2)**2
    
    df['distance'] = R*2*np.arctan2(np.sqrt(df['dummy_a']), np.sqrt(1 - df['dummy_a']))
    
    df.drop(['dlong', 'dlat', 'dummy_a', rad_lat1, rad_lon1, rad_lat2, rad_lon2],axis=1,inplace=True)
    
    return df