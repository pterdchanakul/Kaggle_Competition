# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 17:29:45 2017

@author: JusOroku
"""

# Predict survival on the Titanic 
# More detail of the competition at https://www.kaggle.com/c/titanic

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



# Importing the dataset
train_dataset = pd.read_csv('train.csv')
test_dataset = pd.read_csv('test.csv')
testset_passenger_id = test_dataset.iloc[:,0].values