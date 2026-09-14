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
    st.title("Ejercicio 1 – Flujo de caja con listas")
    
    # Breve descripción del ejercicio con st.markdown() [cite: 1]
    st.markdown("Este módulo permite registrar movimientos financieros (ingresos y gastos) en una lista vacía para calcular el flujo de caja [cite: 1].")

    # Inicializar la lista en session_state [cite: 1]
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # Widgets para ingresar los datos [cite: 1]
    concepto = st.text_input("Concepto del movimiento")
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor", min_value=0.0, step=10.0)

    # Botón para agregar movimientos [cite: 1]
    if st.button("Agregar movimiento"):
        if concepto.strip():
            st.session_state.movimientos.append({
                "Concepto": concepto,
                "Tipo": tipo,
                "Valor": valor
            })

    # Mostrar la tabla de movimientos [cite: 1]
    if len(st.session_state.movimientos) > 0:
        st.markdown("### Tabla de movimientos registrados [cite: 1]")
        st.dataframe(st.session_state.movimientos)

        # Cálculos de totales y saldo final [cite: 1]
        total_ingresos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
        total_gastos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
        saldo_final = total_ingresos - total_gastos

        # Resultado final del flujo de caja con st.metric [cite: 1]
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Ingresos", f"S/. {total_ingresos:,.2f}")
        col2.metric("Total Gastos", f"S/. {total_gastos:,.2f}")
        col3.metric("Saldo Final", f"S/. {saldo_final:,.2f}")

        # Indicador de estado del flujo de caja [cite: 1]
        if saldo_final >= 0:
            st.success("El flujo de caja está: **a favor** [cite: 1]")
        else:
            st.error("El flujo de caja está: **en contra** [cite: 1]")
            
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
