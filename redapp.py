import streamlit as st
import numpy as np
import pandas as pd
import time
st.title("This is Red's App")

#st.image(red.jpg, width=None)

st.write(':sunglasses:')

st.image("images/red.jpg", width=200)
st.write("""
        ### Redouane NOUAf
        """)
#st.markdown('<h1 style="color: Red;">Redouane NOUAF</h1>', unsafe_allow_html=True)

st.image("images/kube.jpg")
st.markdown('<h1 style="float: left;">Kubernetes</h1>', unsafe_allow_html=True)

st.write("Using data to create a table:")
st.write(pd.DataFrame({
    'Article id': [1, 2, 3, 4],
    'Article name': ['Herbsman', 'Zahia', 'Dreams', 'Wonderland']
}))

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
df
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])
    st.line_chart(chart_data)
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])
'You selected: ', option
left_column, right_column = st.columns(2)
pressed = left_column.button('3fett hna')
if pressed:
    right_column.write("Sriwriw!")
expander = st.expander("FAQ")
expander.write("explanations explanations explanations \n explanations explanations explanations explanations... \n explanations explanations explanations explanations....")
'Starting a long computation...'
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)
'...Saaaafi Saaaaliiina !'
