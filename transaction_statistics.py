# Libraries
from csv import excel_tab
import pandas as pd
import os

# Selecting which execl to read.
path = "C:/Devish/transaction history"
files = os.listdir(path)

def select_file():
    excel_index = {}
    for i, file in enumerate(files):
        excel_index[file] = i
    return(files, excel_index)


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


def cashflow(dataframe):
    in_flow = 0
    out_flow = 0
    payment_history = dataframe.iloc[:, [2]].values
    for i in payment_history:
        if(i > 0):
            in_flow += i
        else:
            out_flow += i
    # print(in_flow + out_flow)
    return(float(in_flow), float(out_flow))

    

    


# dataframe = reading_excel(1)
# cashflow(dataframe)