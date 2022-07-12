# Libraries
import pandas as pd
import os
import streamlit as st
import datetime

# Selecting which execl to read.
path = "C:/Devish/transaction history"
files = os.listdir(path)

def selecting_right_file():
    year = "2023"
    # year = str(datetime.datetime.now().year)
    for i, file in enumerate(files):
        if(year == file[20:24]):
            return(i)
    intial_dataframe = pd.DataFrame({"Date" : [], "Time" : [], "Amount of transaction" : [], "Initial amount" : [], "Final Amount" : [], "Mode of transaction" : [], "Tansaction id" : [],"Alert" : [], "Error: Reason" : []})
    new_excel = pd.ExcelWriter(path + "/" + f"transaction_history({year}).xlsx", engine = 'xlsxwriter')
    intial_dataframe.to_excel(new_excel, sheet_name = "Sheet1", index = False)
    new_excel.save()
    files.append(f"transaction_history({year}).xlsx")
    return(len(files) - 1, new_excel)


def reading_excel(file_index):
    # Reading the excel file besed on the file_index.
    dataframe = pd.read_excel(path + '/' + files[file_index], engine= "openpyxl")
    # print(dataframe)
    return(dataframe)


def appending_excel(dataframe, excel):
    dataframe.loc[len(dataframe.index)] = ["assa", "1231", 1235, 45645, 65465, "adad", "sdads","asdas", "adsda"] 
    dataframe.to_excel(excel, index=False, header=False)
    print(dataframe)


i, excel = selecting_right_file()
dataframe = reading_excel(i)
appending_excel(dataframe, excel)
excel.close()