import kagglehub
import os
import shutil

# Download latest version
path = kagglehub.dataset_download("zernach/2018-airplane-flights",)
for file in os.listdir(path):
    filename=os.path.basename(file)
    shutil.copy(os.path.join(path,file),f"data/{filename}")
print("Path to dataset files:", path)