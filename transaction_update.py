# Libraries
import pandas as pd
import os
import datetime

# Path where the excel sheets exist.
path = "C:/Devish/transaction history"
# Returns a list of excel sheets present in the path.
files = os.listdir(path)


def reading_excel(file_index):
    # Reading the excel file besed on the file_index.
    dataframe = pd.read_excel(path + '/' + files[file_index], engine= "openpyxl")
    # print(dataframe)
    return(dataframe)


def selecting_right_file():
    # Opens the file based on the current year, if the year does not exist it will come out of the loop.
    # year = str(datetime.datetime.now().year)
    year = "2023"
    for i, file in enumerate(files):
        if(year == file[20:24]):
            return(i)
    # If the excel sheet of the current year is not present it will create a new excel sheet.
    intial_dataframe = pd.DataFrame({"Date" : [], "Time" : [], "Amount of transaction" : [], "Initial amount" : [], "Final Amount" : [], "Mode of transaction" : [], "Tansaction id" : [],"Alert" : [], "Error: Reason" : []})
    new_excel = pd.ExcelWriter(path + "/" + f"transaction_history({year}).xlsx", engine = 'xlsxwriter')
    intial_dataframe.to_excel(new_excel, sheet_name = "Sheet1", index = False)
    new_excel.save()
    # new_excel.close()
    files.append(f"transaction_history({year}).xlsx")
    return(len(files) - 1)


def appending_excel(file_index, append_values):
    dataframe = pd.read_excel(path + '/' + files[file_index], engine= "openpyxl")
    input_dataframe = pd.DataFrame(append_values)
    dataframe = pd.concat([dataframe, input_dataframe], ignore_index = True)
    dataframe.to_excel(path + '/' + files[file_index], sheet_name='Sheet1', index = False)
