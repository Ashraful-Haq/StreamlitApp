import streamlit as st
import pandas as pd  
import numpy as np 

#Title
st.title("Simple Streamlit app")
#Header
st.header("Simple Header")
#Text
st.write("This is my first time using Streamlit")
#Button
if st.button("Click here"):
    st.write("Button clicked")
#Checkbox
option = st.checkbox("Tick")
if option:
    st.write("Checkbox ticked") 
# Creating empty series  
ser = pd.Series()  
st.write("Series: ", ser)  
# simple array  
data = np.array(['h', 'e', 'l', 'l', 'o'])  
ser = pd.Series(data)  
st.write("Series:\n", ser)

