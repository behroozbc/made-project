from pipline import download_dataset, copy_to_data, read_file,save_processed_data,transform
import unittest.mock as mock
import pandas as pd
import os
from pandas.testing import assert_frame_equal 
test_csv_path='/home/runner/work/made-project/made-project/main/project/test-files/test.csv'

def test_transform():
    weatherdf=pd.DataFrame([['2018/01/02',1],['2018/01/03',2],['2018/05/02',1],['2018/05/03',2],['2018/08/02',1],['2018/08/03',2],['2018/11/02',1],['2018/11/03',2]],columns=['DATE','DailyAverageDewPointTemperature'])
    flightsdf=pd.DataFrame([[500,1,1],[200,1,2],[500,1,3],[100,1,4]],columns=['PricePerTicket','Miles','Quarter'])
    result= transform(flightsdf,weatherdf)
    assert result.shape==(4,3)
def test_save_processed_data():
    data=pd.DataFrame(data=[])
    with mock.patch.object(data,'to_csv') as to_csv_mock:
        save_processed_data(data,'test.csv')
        to_csv_mock.assert_called_once()
def test_copy_to_data():
    path=copy_to_data(test_csv_path)
    assert os.path.exists(os.path.abspath(path))
def test_read_file():
    testfile= read_file(test_csv_path)
    actualFile=pd.read_csv(test_csv_path)
    assert_frame_equal(testfile,actualFile)
test_transform()
test_save_processed_data()
test_copy_to_data()
test_read_file()