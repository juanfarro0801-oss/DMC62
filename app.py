import streamlit as st
import numpy as np

st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.sidebar.image("DMC Logo.png")

# Menú lateral obligatorio según la guía [cite: 1]
seccion = st.sidebar.selectbox(
    "Seleccione el módulo",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

if seccion == "Home":
    st.title("Proyecto Módulo 1 – Python Fundamentals")
    
    st.write("Elaborado por: Juan Diego Farro Taza")
    st.write("Módulo: Home")
    st.write("Módulo: Bachiller en Ingenieria en Gestion Empresarial")
    st.write("Año: 2026")    
    
    st.image("Python.png", width=300)
    
    st.write("### Breve descripción del proyecto")
    st.write("Aplicación interactiva desarrollada en Streamlit para integrar los conceptos fundamentales de programación en Python del Módulo 1.")
    
    st.write("### Tecnologías utilizadas")
    st.write("- Python")
    st.write("- Streamlit")

elif seccion == "Ejercicio 1":
    st.write("Estás en el Ejercicio 1")

elif seccion == "Ejercicio 2":
    st.write("Estás en el Ejercicio 2")

elif seccion == "Ejercicio 3":
    st.write("Estás en el Ejercicio 3")

elif seccion == "Ejercicio 4":
    st.write("Estás en el Ejercicio 4")
