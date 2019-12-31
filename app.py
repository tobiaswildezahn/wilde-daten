import streamlit as st
import numpy as np 

st.title("Wilde-Daten.de")
st.text(" Hier entsteht die Homepage von Wilde-Daten")
st.title("Ein Zufallsdiagramm")

chart = st.bar_chart(np.random.rand(10,5))
btn = st.button("Zufallsgenerator!")

if btn:
	chart.bar_chart(np.random.rand(10,5))

