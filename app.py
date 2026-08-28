import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Configurar el título principal de la aplicación web
st.header('Cuadro de Mando de Anuncios de Venta de Coches')

# --- CASILLAS DE VERIFICACIÓN (CHECKBOXES) ---
# Crear las casillas en la interfaz web
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

# --- LÓGICA PARA EL HISTOGRAMA ---
if build_histogram: # Si la casilla del histograma está seleccionada
    st.write('Construir un histograma para la columna odómetro')

    # Crear el histograma utilizando plotly.graph_objects
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(title_text='Distribución del Odómetro (Millas)')

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# --- LÓGICA PARA EL GRÁFICO DE DISPERSIÓN ---
if build_scatter: # Si la casilla del gráfico de dispersión está seleccionada
    st.write('Construir un gráfico de dispersión para la relación Odómetro vs Precio')

    # Crear el gráfico de dispersión utilizando plotly.graph_objects
    fig_scatter = go.Figure(data=[go.Scatter(
        x=car_data['odometer'], 
        y=car_data['price'], 
        mode='markers',
        marker=dict(opacity=0.5)
    )])
    
    # Personalizar los ejes del gráfico
    fig_scatter.update_layout(
        title_text='Relación entre Millas Recorridas (Odómetro) y Precio',
        xaxis_title='Millas Recorridas (Odómetro)',
        yaxis_title='Precio ($)'
    )

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)

