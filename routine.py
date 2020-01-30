"""
AVHRR data reading for the netcdf data type
"""

from mpop.satellites import PolarFactory
import numpy as np
import datetime
import glob
import os
data_location = r"d:\Data\SampleData"


for row in glob.glob1(data_location, "*.nc"):
    print(os.path.join(data_location, row))

start = datetime.datetime.now()

end = datetime.datetime.now()

print(start - end)
