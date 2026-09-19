import streamlit as st
import numpy as np
import pandas as pd
import libreria_funciones_proyecto1 as lf
import librería_clases_proyecto1 as lc

st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.sidebar.image("DMC Logo.png")

# Menú lateral
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
    
    st.markdown("Este módulo permite registrar movimientos financieros (ingresos y gastos) en una lista vacía para calcular el flujo de caja")

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    concepto = st.text_input("Concepto del movimiento. Ejemplo: Pasajes, servicios, sueldo, etc.")
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor", min_value=0.0, step=10.0)

    # Botón para agregar movimientos
    if st.button("Agregar movimiento"):
        if concepto.strip():
            st.session_state.movimientos.append({
                "Concepto": concepto,
                "Tipo": tipo,
                "Valor": valor
            })

    # Mostrar la tabla de movimientos
    if len(st.session_state.movimientos) > 0:
        st.markdown("### Tabla de movimientos registrados")
        st.dataframe(st.session_state.movimientos)

        # Cálculos de totales y saldo final
        total_ingresos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
        total_gastos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
        saldo_final = total_ingresos - total_gastos

        # Resultado final del flujo de caja con st.metric
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Ingresos", f"S/. {total_ingresos:,.2f}")
        col2.metric("Total Gastos", f"S/. {total_gastos:,.2f}")
        col3.metric("Saldo Final", f"S/. {saldo_final:,.2f}")

        # Indicador de estado del flujo de caja
        if saldo_final >= 0:
            st.success("El flujo de caja está: **a favor**")
        else:
            st.error("El flujo de caja está: **en contra**")
            
        if st.button("Limpiar registros"):
            st.session_state.movimientos = []
            st.rerun()
    else:
        st.info("Aún no hay movimientos registrados.")

elif seccion == "Ejercicio 2":
    st.title("Ejercicio 2 – Registro con NumPy, arrays y DataFrame")
    
    st.markdown("Este módulo permite registrar productos y calcular el total de ventas utilizando arreglos de NumPy y convirtiéndolos a un DataFrame.")

    if "registros_productos" not in st.session_state:
        st.session_state.registros_productos = []

    prod_nombre = st.text_input("Nombre del producto")
    prod_categoria = st.selectbox("Categoría", ["Tecnología", "Oficina", "Hogar", "Otros"])
    prod_precio = st.number_input("Precio unitario", min_value=0.0, step=1.0)
    prod_cantidad = st.number_input("Cantidad", min_value=1, step=1)

    if st.button("Agregar registro"):
        if prod_nombre.strip():
            total_calculado = prod_precio * prod_cantidad
            st.session_state.registros_productos.append({
                "Producto": prod_nombre,
                "Categoría": prod_categoria,
                "Precio": prod_precio,
                "Cantidad": prod_cantidad,
                "Total": total_calculado
            })
            st.success(f"Producto '{prod_nombre}' registrado correctamente.")

    if len(st.session_state.registros_productos) > 0:
        # Uso de NumPy
        lista_precios = np.array([r["Precio"] for r in st.session_state.registros_productos])
        lista_cantidades = np.array([r["Cantidad"] for r in st.session_state.registros_productos])
        lista_totales = np.array([r["Total"] for r in st.session_state.registros_productos])

        st.markdown("### Tabla de registros actualizada")
        df_productos = pd.DataFrame(st.session_state.registros_productos)
        st.dataframe(df_productos)

        st.write(f"**Monto total general en inventario/ventas:** S/. {np.sum(lista_totales):,.2f}")

        if st.button("Limpiar registros de productos"):
            st.session_state.registros_productos = []
            st.rerun()
    else:
        st.info("Aún no hay productos registrados.")

elif seccion == "Ejercicio 3":
    st.title("Ejercicio 3 – Uso de funciones desde una librería externa")
    st.markdown("Este módulo permite calcular la cuota de un préstamo bajo el sistema francés utilizando la librería externa.")

    # Inicializar el histórico de resultados en la sesión
    if "historico_prestamo" not in st.session_state:
        st.session_state.historico_prestamo = []

    # Widgets para ingresar los parámetros de tu función
    monto = st.number_input("Ingrese el monto del préstamo", min_value=0.0, value=10000.0, step=500.0)
    tasa_anual_pct = st.number_input("Ingrese la tasa de interés anual (%)", min_value=0.0, value=12.0, step=0.5)
    plazo_meses = st.number_input("Ingrese el plazo en meses", min_value=1, value=12, step=1)

    # Botón para ejecutar la función de la librería
    if st.button("Calcular Préstamo"):
        # Ejecución 
        resultado = lf.calcular_cuota_prestamo_frances(monto, tasa_anual_pct, int(plazo_meses))
        
        # Mostrar resultado en pantalla
        st.write("El resultado de tu cálculo es:", resultado)
        
        # Guardar en el histórico de resultados (DataFrame)
        st.session_state.historico_prestamo.append({
            "Monto": monto,
            "Tasa Anual (%)": tasa_anual_pct,
            "Plazo (meses)": plazo_meses,
            "Cuota Mensual": resultado["cuota_mensual"],
            "Total Pagado": resultado["total_pagado"],
            "Interés Total": resultado["interes_total"]
        })

    # Mostrar la tabla histórica de resultados obtenidos
    if len(st.session_state.historico_prestamo) > 0:
        st.markdown("### Tabla histórica de resultados obtenidos")
        df_historico = pd.DataFrame(st.session_state.historico_prestamo)
        st.dataframe(df_historico)

elif seccion == "Ejercicio 4":
    st.title("Ejercicio 4 – Uso de clases con CRUD")
    st.markdown("Este módulo gestiona el inventario de productos utilizando la clase `InventarioProducto` con operaciones CRUD completas.")

    # Inicializar la lista en session_state para guardar los objetos o diccionarios
    if "inventario_crud" not in st.session_state:
        st.session_state.inventario_crud = []

    # Pestañas opcionales para organizar el CRUD de manera limpia
    tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs(["Crear", "Leer", "Actualizar", "Eliminar"])

    # --- 1. CREAR ---
    with tab_crear:
        st.subheader("Registrar nuevo producto en inventario")
        nombre_prod = st.text_input("Nombre del producto", key="crear_nombre")
        costo_prod = st.number_input("Costo unitario", min_value=0.0, value=10.0, step=1.0, key="crear_costo")
        precio_prod = st.number_input("Precio unitario", min_value=0.0, value=15.0, step=1.0, key="crear_precio")
        stock_act = st.number_input("Stock actual", min_value=0, value=50, step=1, key="crear_stock")
        stock_min = st.number_input("Stock mínimo", min_value=0, value=10, step=1, key="crear_min")

        if st.button("Guardar Producto"):
            if nombre_prod.strip():
                try:
                    # Instanciar la clase de la librería externa
                    producto_obj = lc.InventarioProducto(nombre_prod, costo_prod, precio_prod, stock_act, stock_min)
                    
                    # Guardar el objeto y su resumen en el session_state
                    st.session_state.inventario_crud.append({
                        "objeto": producto_obj,
                        **producto_obj.resumen()
                    })
                    st.success(f"Producto '{nombre_prod}' creado correctamente.")
                    
                    # Limpia los inputs recargando la aplicación de forma inmediata
                    st.rerun()
                except Exception as e:
                    st.error(f"Error al validar los datos: {e}")
            else:
                st.warning("El nombre del producto no puede estar vacío.")

    # --- 2. LEER ---
    with tab_leer:
        st.subheader("Visualización del Inventario")
        if len(st.session_state.inventario_crud) > 0:
            # Extraer solo los resúmenes para mostrar en el DataFrame
            datos_tabla = [
                {
                    "Producto": item["producto"],
                    "Stock Actual": item["stock_actual"],
                    "Valor Inventario": item["valor_inventario"],
                    "Margen Unitario": item["margen_unitario"],
                    "Margen (%)": item["margen_pct"],
                    "Necesita Reposición": item["necesita_reposicion"]
                }
                for item in st.session_state.inventario_crud
            ]
            st.dataframe(datos_tabla)
        else:
            st.info("Aún no hay productos registrados en el inventario.")

# --- 3. ACTUALIZAR ---
    with tab_actualizar:
        st.subheader("Actualizar datos de un producto")
        if len(st.session_state.inventario_crud) > 0:
            nombres_productos = [item["producto"] for item in st.session_state.inventario_crud]
            prod_seleccionado = st.selectbox("Seleccione el producto a actualizar", nombres_productos, key="select_act")

            # Buscar el índice y el objeto del producto seleccionado
            idx = nombres_productos.index(prod_seleccionado)
            prod_actual = st.session_state.inventario_crud[idx]["objeto"]

            # Usamos los atributos actuales del objeto como valor por defecto en los inputs
            nuevo_costo = st.number_input("Nuevo costo unitario", min_value=0.0, value=float(prod_actual.costo_unitario), step=1.0, key=f"act_costo_{prod_seleccionado}")
            nuevo_precio = st.number_input("Nuevo precio unitario", min_value=0.0, value=float(prod_actual.precio_unitario), step=1.0, key=f"act_precio_{prod_seleccionado}")
            nuevo_stock = st.number_input("Nuevo stock actual", min_value=0, value=int(prod_actual.stock_actual), step=1, key=f"act_stock_{prod_seleccionado}")
            nuevo_min = st.number_input("Nuevo stock mínimo", min_value=0, value=int(prod_actual.stock_minimo), step=1, key=f"act_min_{prod_seleccionado}")

            if st.button("Actualizar Producto"):
                try:
                    # Reinstanciar la clase con los nuevos valores
                    producto_actualizado = lc.InventarioProducto(prod_seleccionado, nuevo_costo, nuevo_precio, nuevo_stock, nuevo_min)
                    st.session_state.inventario_crud[idx] = {
                        "objeto": producto_actualizado,
                        **producto_actualizado.resumen()
                    }
                    st.success(f"Producto '{prod_seleccionado}' actualizado con éxito.")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error al actualizar: {e}")
        else:
            st.info("No hay productos disponibles para actualizar.")

    # --- 4. ELIMINAR ---
    with tab_eliminar:
        st.subheader("Eliminar un producto")
        if len(st.session_state.inventario_crud) > 0:
            nombres_productos_del = [item["producto"] for item in st.session_state.inventario_crud]
            prod_a_eliminar = st.selectbox("Seleccione el producto a eliminar", nombres_productos_del, key="select_del")

            if st.button("Eliminar Producto"):
                idx_del = nombres_productos_del.index(prod_a_eliminar)
                st.session_state.inventario_crud.pop(idx_del)
                st.success(f"Producto '{prod_a_eliminar}' eliminado correctamente.")
                st.rerun()
        else:
            st.info("No hay productos para eliminar.")
