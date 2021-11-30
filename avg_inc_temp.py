import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
from avg_season_increase import *

def fetch_year(date):
    return date.split('-')[0]

def plotfig():
    fig=px.line(data,x='years',y='LandAverageTemperature',title='Avg Land Temp in World')
    fig.add_scatter(x=data['years'],y=data['Uncertainity_top'], name='Uncertainity_top')
    fig.add_scatter(x=data['years'],y=data['Uncertainity_bottom'], name='Uncertainity_bottom')
    fig.show()
if __name__=="__main__":
    global_temp=pd.read_csv('GlobalTemperatures.csv')
    global_temp['years']=global_temp['dt'].apply(fetch_year)
    data=global_temp.groupby('years').agg({'LandAverageTemperature':'mean','LandAverageTemperatureUncertainty':'mean'}).reset_index()
    data['Uncertainity_top']=data['LandAverageTemperature'] + data['LandAverageTemperatureUncertainty']
    data['Uncertainity_bottom']=data['LandAverageTemperature'] - data['LandAverageTemperatureUncertainty']
    plotfig()
    avg_season_temp(global_temp)
    