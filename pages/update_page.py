from warnings import catch_warnings
import streamlit as st
from transaction_update import *
import datetime

current_time = datetime.datetime.now()
current_date = datetime.date.today()
index = selecting_right_file()
dataframe = reading_excel(index)

# Input widgets.
def input_widgets():
    
    # Includes input widgets for date, time and amount of transaction. 
    col_date, col_time, col_amount_transaction = st.columns(3)
    date = col_date.date_input("Date of transaction", datetime.date(int(current_date.strftime("%Y")), int(current_date.strftime("%m")), int(current_date.strftime("%d"))))
    time = col_time.text_input('Time of transaction', current_time.strftime("%H")+":"+ current_time.strftime("%M"))
    # This done to prevent user from typing characters apart from numbers.
    transaction_value = 0
    try:
        transaction_value = int(col_amount_transaction.text_input('Transaction Amount'))
    except:
        st.error('Enter proper Transaction Amount')

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
        icici_mode_transaction = st.selectbox('Select the mode if transaction for ICICI', ("Interest at the end of the month", "NEFT", "INFT", "SMS Charge", "ATM CARD"))
        if(icici_mode_transaction == "NEFT"):
            transaction_id = "NEFT: " + st.text_input("Enter NEFT number")
        elif(icici_mode_transaction == "INFT"):
            transaction_id = "INFT: " + st.text_input("Enter INFT number")
        elif(icici_mode_transaction == "SMS Charge"):
            transaction_id = "Tansaction id: " + st.text_input("Tansaction id")
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
    return({"Date" : [date], "Time" : [time], "Amount of transaction" : [transaction_value],	"Initial amount" : [dataframe.iloc[-1, 4]], "Final Amount" : [dataframe.iloc[-1, 4] - transaction_value], "Mode of transaction" : [mode_transaction], "Tansaction id" : [transaction_id], "Alert" : [alert],	"Error: Reason" : [reason]})

append_values = input_widgets()

button = st.button('Confirm')

if(button):
    appending_excel(index, append_values)

if(button or True):
    display_dataframe = dataframe.astype(str)
    st.dataframe(display_dataframe)