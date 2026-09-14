import streamlit as st
import numpy as np
import pandas as pd

st.title("Especialización Python for Analytics")

# Menú lateral
seccion = st.sidebar.selectbox(
    "Seleccione el módulo",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# ==========================================
# 1. HOME (PRESENTACIÓN)
# ==========================================
if seccion == "Home":
    st.title("Especialización Python for Analytics")
    st.subheader("Módulo 1 – Python Fundamentals")
    
    # Información general del estudiante (Modifica con tus datos)
    st.write("**Elaborado por:** Juan Diego [Escribe aquí tu nombre completo]")
    st.write("**Año:** 2026")
    
    # Logos o imágenes representativas [cite: 1]
    col_img1, col_img2 = st.columns(2)
    with col_img1:
        try:
            st.image("Python.png", width=250)
        except Exception:
            st.info("Imagen Python.png no encontrada en el directorio.")
    with col_img2:
        try:
            st.image("DMC Logo.png", width=250)
        except Exception:
            st.info("Imagen DMC Logo.png no encontrada en el directorio.")
            
    st.markdown("---")
    st.markdown("""
    ### 📌 Breve descripción del proyecto
    Esta aplicación interactiva integra los conceptos fundamentales de programación en Python desarrollados en el **Módulo 1**:
    * **Ejercicio 1:** Flujo de caja utilizando estructuras de listas [cite: 1].
    * **Ejercicio 2:** Registro de datos con arreglos de NumPy y conversión a Pandas DataFrame [cite: 1].
    * **Ejercicio 3:** Invocación de funciones desde una librería externa [cite: 1].
    * **Ejercicio 4:** Implementación de clases y operaciones CRUD [cite: 1].
    """)
    st.markdown("**Tecnologías utilizadas:** Python, Streamlit, NumPy, Pandas")

# ==========================================
# 2. EJERCICIO 1: FLUJO DE CAJA CON LISTAS
# ==========================================
elif seccion == "Ejercicio 1":
    st.title("Ejercicio 1: Flujo de caja con listas")
    st.markdown("""
    Este módulo permite registrar movimientos financieros (ingresos o gastos) en una lista, 
    calculando automáticamente el total de ingresos, total de gastos y el saldo final [cite: 1].
    """)

    # Inicializar el estado de sesión para guardar los movimientos [cite: 1]
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # Formulario para registrar movimientos
    with st.form("form_flujo", clear_on_submit=True):
        concepto = st.text_input("Concepto del movimiento (ej. Sueldo, Luz, Venta)")
        tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
        valor = st.number_input("Valor en S/.", min_value=0.0, step=10.0, format="%.2f")
        btn_agregar = st.form_submit_button("Agregar movimiento")

        if btn_agregar:
            if not concepto.strip():
                st.warning("Por favor ingresa un concepto válido.")
            else:
                st.session_state.movimientos.append({
                    "Concepto": concepto,
                    "Tipo": tipo,
                    "Valor": valor
                })
                st.success(f"Movimiento '{concepto}' registrado con éxito.")

    # Mostrar la tabla y métricas si hay datos
    if len(st.session_state.movimientos) > 0:
        df_movimientos = pd.DataFrame(st.session_state.movimientos)
        st.subheader("Historial de Movimientos")
        st.dataframe(df_movimientos, use_container_width=True)

        # Cálculos de ingresos, gastos y saldo final
        total_ingresos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
        total_gastos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
        saldo_final = total_ingresos - total_gastos

        # Mostrar métricas en columnas [cite: 1]
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Ingresos", f"S/. {total_ingresos:,.2f}")
        col2.metric("Total Gastos", f"S/. {total_gastos:,.2f}")
        col3.metric("Saldo Final", f"S/. {saldo_final:,.2f}")

        # Indicador de estado del flujo de caja [cite: 1]
        if saldo_final >= 0:
            st.success("Estado del flujo de caja: **A favor**")
        else:
            st.error("Estado del flujo de caja: **En contra**")
            
        # Botón para limpiar registros (útil para pruebas)
        if st.button("Limpiar movimientos"):
            st.session_state.movimientos = []
            st.rerun()
    else:
        st.info("Aún no has registrado ningún movimiento. Utiliza el formulario superior para comenzar.")

# ==========================================
# 3. EJERCICIO 2 (Estructura base)
# ==========================================
elif seccion == "Ejercicio 2":
    st.title("Ejercicio 2: Registro con NumPy, arrays y DataFrame")
    st.write("Próximamente: Aquí implementaremos el registro usando arreglos de NumPy [cite: 1].")

# ==========================================
# 4. EJERCICIO 3 (Estructura base)
# ==========================================
elif seccion == "Ejercicio 3":
    st.title("Ejercicio 3: Uso de funciones desde una librería externa")
    st.write("Próximamente: Aquí conectaremos `libreria_funciones_proyecto1.py` [cite: 1].")

# ==========================================
# 5. EJERCICIO 4 (Estructura base)
# ==========================================
elif seccion == "Ejercicio 4":
    st.title("Ejercicio 4: Uso de clases desde una librería externa con CRUD")
    st.write("Próximamente: Aquí implementaremos la clase y operaciones CRUD con `libreria_clases_proyecto1.py` [cite: 1].")
