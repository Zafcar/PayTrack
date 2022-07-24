import streamlit as st
from transaction_update import *
import datetime

current_time = datetime.datetime.now()
current_date = datetime.date.today()


# Input widgets.
col_date, col_time, col_amount_transaction = st.columns(3)
col_date.date_input("Date of transaction", datetime.date(int(current_date.strftime("%Y")), int(current_date.strftime("%m")), int(current_date.strftime("%d"))))
col_time.text_input('Time of transaction', current_time.strftime("%H")+":"+ current_time.strftime("%M"))
col_amount_transaction.text_input('Transaction Amount')

col_mode_transaction, col_transaction_id = st.columns(2)