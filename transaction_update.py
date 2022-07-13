# Libraries
import pandas as pd
import os
import datetime

# Selecting which execl to read.
path = "C:/Devish/transaction history"
files = os.listdir(path)

def selecting_right_file():
    year = str(datetime.datetime.now().year)
    for i, file in enumerate(files):
        if(year == file[20:24]):
            return(i)
    intial_dataframe = pd.DataFrame({"Date" : [], "Time" : [], "Amount of transaction" : [], "Initial amount" : [], "Final Amount" : [], "Mode of transaction" : [], "Tansaction id" : [],"Alert" : [], "Error: Reason" : []})
    new_excel = pd.ExcelWriter(path + "/" + f"transaction_history({year}).xlsx", engine = 'xlsxwriter')
    intial_dataframe.to_excel(new_excel, sheet_name = "Sheet1", index = False)
    new_excel.save()
    # new_excel.close()
    files.append(f"transaction_history({year}).xlsx")
    return(len(files) - 1)


def appending_excel(file_index):
    dataframe = pd.read_excel(path + '/' + files[file_index], engine= "openpyxl")
    input_dataframe = pd.DataFrame({"Date" : ["assa"], "Time" : ["1231"], "Amount of transaction" : [1235],	"Initial amount" : [45645], "Final Amount" : [65465], "Mode of transaction" : ["adad"], "Tansaction id" : ["sdads"], "Alert" : ["asdas"],	"Error: Reason" : ["adsda"]})
    dataframe = pd.concat([dataframe, input_dataframe], ignore_index = True)
    dataframe.to_excel(path + '/' + files[file_index], sheet_name='Sheet1', index = False)
