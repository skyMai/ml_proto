#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:53:09 2018

@author: mairong
"""

import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def main():
    main_file_path = '/Users/mairong/mr_py/kaggle_tutorial/dataset/train.csv'
    data = pd.read_csv(main_file_path)
    feature_col = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 
                        'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
    print(data.head())
    input_x = data[feature_col]
    input_y = data.SalePrice
    train_x, test_x, train_y, test_y = train_test_split(input_x, input_y, random_state=1)
    forest_model = RandomForestRegressor()
    forest_model.fit(train_x, train_y)
    cv_result = forest_model.predict(test_x)
    mae = mean_absolute_error(test_y, cv_result)
    print(mae)


if __name__ == "__main__":
    main()
