#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:53:09 2018

@author: mairong
"""

import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


#
def get_mae(max_leaf_nodes, predictors_train, predictors_val, targ_train, targ_val):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(predictors_train,targ_train)
    predict_y = model.predict(predictors_val)
    mae = mean_absolute_error(predict_y,targ_val)
    return mae

# work dir:
# main_file_path = '/Users/mairong/mr_py/kaggle_tutorial/dataset/train.csv'
# home dir:
main_file_path = '/Users/MaiRong/study/learning/python/ml_proto/kaggle_tutorial/dataset/train.csv'
data = pd.read_csv(main_file_path)
# print('hello world')
# print(data.describe())
# print(data.columns)
# id_col = data.Id
# # print(id_col.head())
# # print(data.Street)
# columns_of_interest = ['Id','MSSubClass','Street','SalePrice']
# two_columns = data[columns_of_interest]
# print(two_columns.describe())

##########test
# print(data.columns)
# melbourne_price_data = data.SalePrice
# print(melbourne_price_data.head())
# two_col= ['SalePrice','MoSold']
# two_col_data = data[two_col]
# print(two_col_data.head())

#############stage 2

y = data.SalePrice
data.dropna(axis = 0)

features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 
                        'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = data[features]
model = DecisionTreeRegressor()
model.fit(X,y)
print(model.predict(X.head()))
print(y.head())

predict_result =model.predict(X)
mae = mean_absolute_error(y, predict_result)
print("the final mean absolute error for X:", mae)

train_x, test_x, train_y, test_y = train_test_split(X, y, random_state=1)
tree_model = DecisionTreeRegressor()

tree_model.fit(train_x, train_y)
test_predict = tree_model.predict(test_x)
cross_err = mean_absolute_error(test_predict, test_y)
#print("cross error is :", cross_err)

#stage3:Underfitting, Overfitting and Model Optimization
for max_leaf_nodes in [5,10,20,50,500,5000]:
    my_mae = get_mae(max_leaf_nodes, train_x, test_x, train_y, test_y )
    print("Max leaf nodes: %d, \t\t  mean absolute error: %d "%(max_leaf_nodes, my_mae))