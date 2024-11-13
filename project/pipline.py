import kagglehub
import os
import shutil
from pirateweather import forecast

# Download latest version
path = kagglehub.dataset_download("zernach/2018-airplane-flights")
for file in os.listdir(path):
    filename=os.path.basename(file)
    shutil.copy(os.path.join(path,file),f"data/{filename}")
path = kagglehub.dataset_download("behroozbc/average-day-weather-for-2018")
for file in os.listdir(path):
    filename=os.path.basename(file)
    shutil.copy(os.path.join(path,file),f"data/{filename}")
