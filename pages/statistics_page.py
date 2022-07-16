import pandas as pd
import streamlit as st
import altair as alt
import numpy as np
from transaction_statistics import *

excel_files, excel_index = select_file()
option = st.selectbox('Select an Excel file', excel_files)
dataframe = reading_excel(excel_index[option])

# Converting all the cloumns in the excel to string for displaying it.
display_dataframe = dataframe.astype(str)

# Displaying the dataset of slected excel sheet.
st.dataframe(display_dataframe)

# Displaying the amount spends.
in_flow, out_flow = cashflow(dataframe)
total_amount_spend, amount_added, amount_spend = st.columns(3)
if(in_flow + out_flow > 0):
     st.markdown(f'<p style="color:#33ff33;">↑ {str(round(in_flow + out_flow, 2))}</p>', unsafe_allow_html=True)
else:
     st.markdown(f'<p style="color:#FF5733;">↓ {str(round(in_flow + out_flow, 2))}</p>', unsafe_allow_html=True)
st.markdown(f'<p style="color:#33ff33;">↑ {str(round(in_flow, 2))}</p>', unsafe_allow_html=True)
st.markdown(f'<p style="color:#FF5733;">↓ {str(round(out_flow, 2))}</p>', unsafe_allow_html=True)
