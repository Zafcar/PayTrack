# Libraries
import pandas as pd
import os
import streamlit as st

# Selecting which execl to read.
path = "C:/Devish/transaction history"
files = os.listdir(path)
for i, file in enumerate(files):
    print(i, file)
file_index = int(input("Enter the file index to read xlsx: "))

# Reading the excel file besed on the file_index.
dataframe = pd.read_excel(path + '/' + files[file_index])
# print(dataframe)
transaction_history = dataframe.iloc[:, [2, 5]].values

# Displaying the amount spent in each Mode_of_transaction
mode_of_transaction = {}
for cash, label in transaction_history:
    if(label in mode_of_transaction.keys()):
        mode_of_transaction[label] += cash
    else:
        mode_of_transaction.update({label : cash})
# print(pd.DataFrame(mode_of_transaction.items()))
###
