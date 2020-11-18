# -*- coding: utf-8 -*-

#streamlit run C:\Users\fredr\Python_koding\Gjensidig_intervju\Gjensidige_intervju\streamlit_interface.py


import streamlit as st
import Lorenz_system as lz
import altair as alt
import pandas as pd
import numpy as np


#LAYOUT
st.sidebar.image("https://www.gjensidige.no/konsern/presse/bildearkiv/_attachment/129733?_download=true&_ts=151631b91d0", width = 200)
st.title("Modelling chaos with the Lorenz system")
st.write("This is an example code of how you can use streamlit to help analyze your results.\n \nThe Lorenz system is given by")
st.latex(r"\dot{x} = \sigma \cdot (y - x)")
st.latex(r"\dot{y} = x \cdot (\rho - z) - y")
st.latex(r"\dot{z} = xy - \beta z")
"test"
#SYSTEM PARAMETERS (FIXED)
x_0, y_0, z_0 = [0.001]*3 #Set Initial values
delta, TOL = 1e-3, 1e-4  #Set partition delta and quadrature error tolerance TOL
#t_limit = 50 #Will evaluate this intervall

#SIDEBAR
st.sidebar.write("## Parameters of the system")
sigma = st.sidebar.slider("Sigma (std 10)", 1, 100, 10)
rho = st.sidebar.slider("Rho (std 28)", 1, 100, 28)
beta = st.sidebar.slider("3 * Beta (std 8)", 1, 100, 8) / 3
t_limit = st.sidebar.number_input("Simulation time", 1, 100, 40)

#OTHER PARAMETERS
t_final_shown = st.slider("Show time intervall: ", 1, t_limit, t_limit)
horizontal_axis = st.selectbox("Select horizontal axis", ["x","y", "z", "T"])
vertical_axis = st.selectbox("Select vertical axis", ["z","x", "y", "T"])

#CALCULATE AND FORMATE DATA
@st.cache
def calculate():
    x,y,z,T = lz.run_lorenz(x_0, y_0, z_0, t_limit, delta, sigma, rho, beta, TOL)
    data = np.transpose(np.array([x,y,z,T]))
    return pd.DataFrame(data, columns = ["x","y","z","T"])
results = calculate()



#GENERATE AND UPLOAD CHARTS 
chart = alt.Chart(results.head(t_final_shown*int(1/delta))).mark_line().encode(
    x = horizontal_axis,
    y = vertical_axis,
    order = "T"        
).configure_line(size = 0.5)

st.altair_chart(chart)



st.write("Ran as: ", __name__)


