import kagglehub
import os
import shutil
from pirateweather import forecast
import pandas as pd
QuarterRange=[{'start':'2018-01-01','end':'2018-03-31','index':1},{'start':'2018-04-01','end':'2018-06-31','index':2},{'start':'2018-07-01','end':'2018-09-31','index':3},{'start':'2018-10-01','end':'2018-12-31','index':4}]
# Download latest version
path = kagglehub.dataset_download("zernach/2018-airplane-flights")
for file in os.listdir(path):
    filename=os.path.basename(file)
    shutil.copy(os.path.join(path,file),f"data/{filename}")
path = kagglehub.dataset_download("behroozbc/average-day-weather-for-2018")
for file in os.listdir(path):
    filename=os.path.basename(file)
    shutil.copy(os.path.join(path,file),f"data/{filename}")
weatherdf= pd.read_csv('data\Avg-day-2018.csv')[['DATE','DailyAverageDewPointTemperature']]
flightsdf=pd.read_csv('data\Cleaned_2018_Flights.csv')
resultdf=[]
for quarter in QuarterRange:
    quraterRange=weatherdf[(weatherdf['DATE'] > quarter['start']) & (weatherdf['DATE'] < quarter['end'])]
    flights_quarter_range=flightsdf[flightsdf['Quarter']==quarter['index']]
    resultdf.append({'AvgTemperature':quraterRange['DailyAverageDewPointTemperature'].astype(float).mean(),'PricePerMiles':((flights_quarter_range['PricePerTicket'].astype(float))/flights_quarter_range['Miles'].astype(float)).mean(),'quarter':quarter['index']})

pd.DataFrame(resultdf).to_csv('data\\final.csv')
