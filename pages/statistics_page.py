import streamlit as st
from transaction_statistics import *

excel_files, excel_index = select_file()
option = st.selectbox('Select an Excel file', excel_files)
dataframe = reading_excel(excel_index[option])

# Converting all the cloumns in the excel to string for displaying it.
display_dataframe = dataframe.astype(str)

# Displaying the dataset of slected excel sheet.
st.dataframe(display_dataframe)

# Displaying the amount spends.
col1, col2, col3 = st.columns(3)
in_flow, out_flow = cashflow(dataframe)
total_amount_spend, amount_added, amount_spend = st.columns(3)
if(in_flow + out_flow >= 0):
     col1.markdown(f'<h2 style="color:#33cc33;"><span style = "font-size: 20px;">Total cash flow</span><br>↑ ₹{str(round(in_flow + out_flow, 2))}</h1>', unsafe_allow_html=True)
else:
     col1.markdown(f'<h2 style="color:#ff0000;"><span style = "font-size: 20px;">Total cash flow</span><br>↓ ₹{str(round(in_flow + out_flow, 2))}</h1>', unsafe_allow_html=True)
col2.markdown(f'<h2 style="color:#33cc33;"><span style = "font-size: 20px;">Cash inflow</span><br>↑ ₹{str(round(in_flow, 2))}</h1>', unsafe_allow_html=True)
col3.markdown(f'<h2 style="color:#ff0000;"><span style = "font-size: 20px;">Cash spent</span><br>↓ ₹{str(round(out_flow, 2))}</h1>', unsafe_allow_html=True)


# Displaying graph based on date.
# date_cash = data_base_transaction(dataframe)
# transaction_chart = figure(
#      title='simple line example',
#      x_axis_label='Date',
#      y_axis_label='Cash')

# transaction_chart.line(date_cash["Date"], date_cash["Cash outflow"], legend_label='Trend', line_width=2)

# st.bokeh_chart(transaction_chart, use_container_width=True)

# st.area_chart(pd.DataFrame(data_base_transaction(dataframe)))