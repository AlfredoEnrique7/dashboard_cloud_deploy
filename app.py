import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Encabezado con texto (Criterio obligatorio)
st.set_page_config(page_title="Dashboard de Anuncios de Vehículos", layout="wide")
st.title("🚗 Cuadro de Mando: Mercado de Vehículos Usados (EE. UU.)")
st.markdown("Analiza de forma interactiva la distribución de precios, condiciones y kilometraje del dataset oficial.")

# 2. Carga segura de datos
@st.cache_data
def cargar_datos():
    return pd.read_csv("vehicles_us.csv")

try:
    df = cargar_datos()
except FileNotFoundError:
    st.error("❌ Archivo 'vehicles_us.csv' no encontrado en el directorio raíz.")
    st.stop()

# 3. Componentes Interactivos (Botón / Casilla de verificación - Criterio obligatorio)
st.sidebar.header("Filtros y Controles")
filtrar_buena_condicion = st.sidebar.checkbox("Mostrar solo vehículos en excelente/buena condición")

# Filtrar dinámicamente si la casilla está marcada
if filtrar_buena_condicion:
    df_visualizacion = df[df['condition'].isin(['excellent', 'good', 'like new', 'new'])]
else:
    df_visualizacion = df

# 4. Construcción de Visualizaciones Requeridas
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Histograma de Precios")
    fig_histograma = px.histogram(
        df_visualizacion, x='price',
        title="Frecuencia de Precios en el Mercado",
        labels={'price': 'Precio (USD)'}, template='plotly_dark'
    )
    st.plotly_chart(fig_histograma, use_container_width=True)

with col2:
    st.markdown("### 📉 Gráfico de Dispersión (Scatterplot)")
    fig_dispersion = px.scatter(
        df_visualizacion, x='odometer', y='price', 
        color='type', title="Relación: Kilometraje (Odometer) vs Precio",
        labels={'odometer': 'Kilometraje', 'price': 'Precio (USD)', 'type': 'Tipo de Auto'},
        template='plotly_dark'
    )
    st.plotly_chart(fig_dispersion, use_container_width=True)
