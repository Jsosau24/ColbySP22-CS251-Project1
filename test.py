from data import Data
import numpy as np
from analysis import Analysis

iris_filename = 'data/iris.csv'
iris_data = Data(iris_filename)
an = Analysis(iris_data)

print(iris_data.get_all_data())
