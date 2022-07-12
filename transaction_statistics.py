# Libraries
import pandas as pd
import os
import streamlit as st

# Selecting which execl to read.
path = "C:/Devish/transaction history"
files = os.listdir(path)

def select_file():
    for i, file in enumerate(files):
        print(i, file)
    return(int(input("Enter the file index to read xlsx: ")))


def reading_excel(file_index):
    # Reading the excel file besed on the file_index.
    dataframe = pd.read_excel(path + '/' + files[file_index], engine= "openpyxl")
    # print(dataframe)
    return(dataframe)
    

def transaction_mode(dataframe):
    # Displaying the amount spent in each Mode_of_transaction
    transaction_history = dataframe.iloc[:, [2, 5]].values
    mode_of_transaction = {}
    for cash, label in transaction_history:
        if(label in mode_of_transaction.keys()):
            mode_of_transaction[label] += cash
        else:
            mode_of_transaction.update({label : cash})
            # print(pd.DataFrame(mode_of_transaction.items()))
    return(mode_of_transaction)

i = select_file()
dataframe = reading_excel(i)
print(dataframe)