import kagglehub
import os
import shutil
import pandas as pd

QuarterRange=[{'start':'2018-01-01','end':'2018-03-31','index':1},{'start':'2018-04-01','end':'2018-06-31','index':2},{'start':'2018-07-01','end':'2018-09-31','index':3},{'start':'2018-10-01','end':'2018-12-31','index':4}]
# Download latest version
def download_dataset(name:str):
    path=kagglehub.dataset_download(name)
    return os.path.join(path,os.listdir(path)[0])
def copy_to_data(fullPath2File:str):
    savePath=f"{os.getcwd()}/main/data/{os.path.basename(fullPath2File)}"
    shutil.copy(fullPath2File,savePath)
    return savePath
def read_file(path2localfile):
    return pd.read_csv(path2localfile)
def save_processed_data(arr:pd.DataFrame,location:str):
    arr.to_csv(location)
def transform(flightsdf:pd.DataFrame,weatherdf:pd.DataFrame):
    weatherdf= weatherdf[['DATE','DailyAverageDewPointTemperature']]
    resultdf=[]
    for quarter in QuarterRange:
        quraterRange=weatherdf[(weatherdf['DATE'] > quarter['start']) & (weatherdf['DATE'] < quarter['end'])]
        flights_quarter_range=flightsdf[flightsdf['Quarter']==quarter['index']]
        resultdf.append({'AvgTemperature':quraterRange['DailyAverageDewPointTemperature'].astype(float).mean(),'PricePerMiles':((flights_quarter_range['PricePerTicket'].astype(float))/flights_quarter_range['Miles'].astype(float)).mean(),'quarter':quarter['index']})        
    return pd.DataFrame(resultdf)

if __name__=='__main__':
    resultdf=transform(read_file(copy_to_data(download_dataset('zernach/2018-airplane-flights'))),read_file(copy_to_data(download_dataset('behroozbc/average-day-weather-for-2018'))))
    save_processed_data(resultdf,'data\\final.csv')

