import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv(r"C:\Users\samue\OneDrive\Escritorio\Data Analyst Bootcamp (TripleTen)\Sprint 7 (2)\final-project-sprint7\vehicles_us.csv")

st.header('Análisis de datos de vehículos')

build_histogram = st.checkbox('Construir histograma')
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Construir un gráfico de dispersión para las columnas odómetro y precio')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)