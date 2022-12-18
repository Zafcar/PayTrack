import streamlit as st
from transaction_update import *
import datetime

# Gets current time and date.
current_time = datetime.datetime.now()
current_date = datetime.date.today()

# Global variables.
index = selecting_right_file(current_date.strftime("%Y"))
dataframe = reading_excel(index)
df_is_empty = dataframe.empty

# Input widgets.
def input_widgets():

    button = False

    # Includes input widgets for date, time and amount of transaction. 
    col_date, col_time, col_amount_transaction = st.columns(3)
    date = col_date.date_input("Date of transaction", datetime.date(current_date.year, current_date.month, current_date.day))
    time = col_time.text_input('Time of transaction', current_time.strftime("%H")+":"+ current_time.strftime("%M"))
    # This done to prevent user from typing characters apart from numbers.
    transaction_value = col_amount_transaction.number_input('Transaction Amount', step = 1.00)    
    
    # Includes input widgets for mode of transaction.
    # Based on input given in mode mode_transaction other widgets get displayed and necessary inputs are taken in. 
    mode_transaction = st.selectbox('Select the mode if transaction', ("GPAY", "Paytm", "ICICI"))
    transaction_id = ""

    if(mode_transaction == "GPAY"):
        col_gpay_id, col_upi_id = st.columns(2)
        transaction_id = "GPAY id: " + col_gpay_id.text_input("Enter GPAY id")
        transaction_id += " UPI id: " + col_upi_id.text_input("Enter UPI id")
        # st.write(transaction_id)

    elif(mode_transaction == "Paytm"):
        transaction_id = "UPI id: " + st.text_input("Enter UPI id")
        # st.write(transaction_id)
        
    elif(mode_transaction == "ICICI"):
        icici_mode_transaction = st.selectbox('Select the mode if transaction for ICICI', ("Interest at the end of the month", "NEFT", "INFT", "IMPS", "SMS Charge", "ATM CARD"))
        if(icici_mode_transaction == "NEFT"):
            transaction_id = "NEFT: " + st.text_input("Enter NEFT number")
        elif(icici_mode_transaction == "INFT"):
            transaction_id = "INFT: " + st.text_input("Enter INFT number")
        elif(icici_mode_transaction == "SMS Charge"):
            transaction_id = "Tansaction id: " + st.text_input("Tansaction id")
        
        elif(icici_mode_transaction == "IMPS"):
            transaction_id = "Transaction id: " + st.text_input("Transaction id")
        
        else:
            transaction_id = icici_mode_transaction
        # st.write(transaction_id)

    col_alert, col_reason = st.columns(2)
    alert = col_alert.radio("Any problems detected in the transaction", ('Yes', 'No'))
    reason = "NONE"
    if(alert == "Yes"):
        reason = col_reason.text_input("Type the reason of the problem")
    # st.write(date)
    # return({"Date" : [datetime.datetime.strptime(date, '%y/%m/%d')], "Time" : [datetime.datetime.strptime(time, '%H:%M:%S')], "Amount of transaction" : [transaction_value ],	"Initial amount" : [dataframe.iloc[-1, 4]], "Final Amount" : [dataframe.iloc[-1, 4] - transaction_value], "Mode of transaction" : [mode_transaction], "Tansaction id" : [transaction_id], "Alert" : [alert],	"Error: Reason" : [reason]})
    if(df_is_empty):
        intial_amount = input_intial_amount
    else:
        intial_amount = dataframe.iloc[-1, 4]

    # This button appends all the values.
    if(transaction_value != 0 and transaction_id != "" and reason != ""):
        button = st.button('Confirm')

    return({"Date" : [date], "Time" : [time], "Amount of transaction" : [transaction_value],	"Initial amount" : [intial_amount], "Final Amount" : [intial_amount + transaction_value], "Mode of transaction" : [mode_transaction], "Tansaction id" : [transaction_id], "Alert" : [""],	"Error: Reason" : [reason]}, button)


# This checks if the dataframe is empty or not and checks whether to add initial values.
if(df_is_empty):
    if(pervious_year(current_date.year - 1)):
        temp_dataframe = reading_excel(index - 1)
        input_intial_amount  = temp_dataframe.iloc[-1, 4]
    else:
        input_intial_amount = st.number_input('Enter initial amount', step = 1)
        if(input_intial_amount < 0):
            st.error("Please enter proper amount")


append_values, button = input_widgets()

if(button):
    appending_excel(index, append_values)
    alert_color_fix(reading_excel(index), index)

if(button or True):
    display_dataframe = reading_excel(index).astype(str)
    st.dataframe(display_dataframe)
