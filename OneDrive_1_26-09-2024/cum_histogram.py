import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import sqldf

def get_cumulative_histogram(df, X='min_distance', HUE='is_delivered_2'):
    sns.ecdfplot(data=df, x=X, log_scale=True, hue = HUE)
    plt.pyplot.xlim([0.001,10000])
    plt.pyplot.xlabel('Min Distance between Delivery Point and GPS Tracking \n for each shipment (km)')
    plt.pyplot.ylabel('Proportion of Shipments')
    plt.pyplot.grid('show')
    plt.pyplot.title('Cumulative Distribution of Minimum Distance \n (between Delivery Long/Lat & GPS Long/Lat for each shipment)')
    plt.pyplot.show()