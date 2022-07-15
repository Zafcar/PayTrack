import pandas as pd
import streamlit as st
import altair as alt
import numpy as np
from transaction_statistics import *

excel_files, excel_index = select_file()
option = st.selectbox('Select an Excel file', excel_files)
dataframe = reading_excel(excel_index[option])
dataframe = dataframe.astype(str)
st.dataframe(dataframe)

# st.bar_chart(dataframe[:, [0, 2]])

chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["a", "b", "c"])

st.bar_chart(chart_data)