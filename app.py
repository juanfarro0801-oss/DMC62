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
    st.title("Proyecto Módulo 1– Python Fundamentals")
    
    st.write("Elaborado por: Juan Diego Farro Taza")
    st.write("Módulo: Home")
    st.write("Informacion general: Bachiller en Ingenieria en Gestion Empresarial de la Universidad Nacional Agraria la molina. Interesado en aprender todo lo relacionado al analisis de datos")
    st.write("Año: 2026")    
    
    st.image("Python.png", width=300)
    
    st.write("### Breve descripción del proyecto")
    st.write("Aplicación interactiva desarrollada en Streamlit para integrar los conceptos fundamentales de programación en Python del Módulo 1.")
    
    st.write("### Tecnologías utilizadas")
    st.write("- Python")
    st.write("- Streamlit")

elif seccion == "Ejercicio 1":
    st.title("Ejercicio 1: Flujo de caja con listas")
    st.write("Registra tus movimientos financieros (ingresos o gastos):")

    # Inicializar lista en la memoria de la sesión [cite: 1]
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # Widgets para ingresar datos [cite: 1]
    concepto = st.text_input("Ingresa el concepto del movimiento")
    tipo = st.selectbox("Selecciona el tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Ingresa el valor", min_value=0.0, step=10.0)

    # Botón para agregar a la lista [cite: 1]
    if st.button("Agregar movimiento"):
        if concepto.strip() != "":
            st.session_state.movimientos.append({
                "Concepto": concepto,
                "Tipo": tipo,
                "Valor": valor
            })
            st.success(f"Movimiento '{concepto}' agregado correctamente.")
        else:
            st.warning("Por favor, ingresa un concepto válido.")

    # Mostrar la lista de movimientos registrados [cite: 1]
    st.write("### Historial de movimientos")
    if len(st.session_state.movimientos) > 0:
        st.write(st.session_state.movimientos)

        # Calcular totales [cite: 1]
        total_ingresos = sum(item["Valor"] for item in st.session_state.movimientos if item["Tipo"] == "Ingreso")
        total_gastos = sum(item["Valor"] for item in st.session_state.movimientos if item["Tipo"] == "Gasto")
        saldo_final = total_ingresos - total_gastos

        st.write(f"**Total Ingresos:** S/. {total_ingresos}")
        st.write(f"**Total Gastos:** S/. {total_gastos}")
        st.write(f"**Saldo Final:** S/. {saldo_final}")

        # Indicar si está a favor o en contra [cite: 1]
        if saldo_final >= 0:
            st.success("El flujo de caja está: **A favor**")
        else:
            st.error("El flujo de caja está: **En contra**")

        # Botón opcional para limpiar la lista
        if st.button("Limpiar registros"):
            st.session_state.movimientos = []
            st.rerun()
    else:
        st.info("Aún no hay movimientos registrados.")

elif seccion == "Ejercicio 2":
    st.write("Estás en el Ejercicio 2")

elif seccion == "Ejercicio 3":
    st.write("Estás en el Ejercicio 3")

elif seccion == "Ejercicio 4":
    st.write("Estás en el Ejercicio 4")
