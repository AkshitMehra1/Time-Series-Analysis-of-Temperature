import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
def avg_season_temp(global_temp):
    global_temp['dt']=pd.to_datetime(global_temp['dt'])
    global_temp['month']=global_temp['dt'].dt.month
    def get_season(month):
        if month>=3 and month<=5:
            return 'spring'
        elif month>=6 and month<=8:
            return 'summer'
        elif month>=9 and month<=11:
            return 'autumn'
        else:
            return 'winter'
    global_temp['season']=global_temp['month'].apply(get_season)
    years=global_temp['years'].unique()
    spring_temps=[]
    summer_temps=[]
    autumn_temps=[]
    winter_temps=[]
    for year in years:
        current_df=global_temp[global_temp['years']==year]
        spring_temps.append(current_df[current_df['season']=='spring']['LandAverageTemperature'].mean())
        summer_temps.append(current_df[current_df['season']=='summer']['LandAverageTemperature'].mean())
        autumn_temps.append(current_df[current_df['season']=='autumn']['LandAverageTemperature'].mean())
        winter_temps.append(current_df[current_df['season']=='winter']['LandAverageTemperature'].mean())
    season=pd.DataFrame()
    season['year']=years
    season['spring_temps']=spring_temps
    season['summer_temps']=summer_temps
    season['autumn_temps']=autumn_temps
    season['winter_temps']=winter_temps
    fig=px.line(season,x='year', y='spring_temps', title='Avg Temp in Each Season')
    fig.add_scatter(x=season['year'], y=season['summer_temps'], name='summer_temps')
    fig.add_scatter(x=season['year'], y=season['autumn_temps'], name='autumn_temps')
    fig.add_scatter(x=season['year'], y=season['winter_temps'], name='winter_temps')
    fig.show()