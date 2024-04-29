
# import pandas as pd
import numpy as np

data = np.genfromtxt('E:\Practice\Python\Hands-On-Data-Analysis-with-Pandas-2nd-edition\ch_02\data\example_data.csv',
                    delimiter=';', names=True, dtype=None, encoding = 'UTF-8')

print(data)
