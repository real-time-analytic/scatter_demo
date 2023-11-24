import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# import the WHO dataset

who_data = pd.read_csv('WHO_data_new.csv')

st.write(who_data)

st.sidebar.header('Pick two variables for your scatterplot')
x_val = st.sidebar.selectbox('Pick your x-axis',who_data.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox('Pick your y-axis',who_data.select_dtypes(include=np.number).columns.tolist())

# create altair chart
scatter = alt.Chart(who_data,title=f'Correlation between {x_val} and {y_val}').mark_point().encode(
    alt.X(x_val,title=f'{x_val}'),
    alt.Y(y_val,title=f'{y_val}'))
st.altair_chart(scatter, use_container_width=True)

# calculate the correlation
corr = round(who_data[x_val].corr(who_data[y_val]),2)

st.write(f'The correlation between {x_val} and {y_val} is {corr}')