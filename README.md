# dashboard_cloud_deploy

##  Aplicación en Vivo

Puedes interactuar con el cuadro de mando completamente funcional y desplegado en la nube a través del siguiente enlace oficial:
**[Despliegue en Render](https://dashboard-cloud-deploy.onrender.com)**


# Cuadro de Mando - Anuncios de Venta de Coches

Este proyecto es una aplicación web interactiva desarrollada en Python orientada a la ingeniería de software y el despliegue en la nube. La aplicación funciona como un cuadro de mando (*dashboard*) que permite realizar un análisis exploratorio de datos de forma dinámica sobre un conjunto de datos de anuncios de venta de vehículos en los Estados Unidos.

---

## ️ Funcionalidades de la Aplicación

La aplicación proporciona una interfaz gráfica e interactiva en el navegador que le permite al usuario controlar qué componentes visuales desea renderizar bajo demanda mediante casillas de verificación (**Checkboxes**):

*   **Distribución del Odómetro (Histograma):** Analiza la frecuencia y concentración de las millas recorridas por los vehículos anunciados mediante un histograma generado con la librería de bajo nivel `plotly.graph_objects`.
*   **Relación de Precio vs. Millaje (Gráfico de Dispersión):** Permite evaluar visualmente cómo impacta el kilometraje acumulado (*odometer*) en el precio de venta final (*price*) de los coches a través de un diagrama de puntos dispersos interactivo con controles de zoom integrados.

---

##  Tecnologías Utilizadas

*   **Lenguaje de Programación:** Python (Entorno virtual aislado gestionado con Conda).
*   **Framework Web:** Streamlit (Desarrollo ágil de la interfaz de usuario).
*   **Gráficos Interactivos:** Plotly (`plotly.graph_objects` para la estructuración de figuras).
*   **Procesamiento de Datos:** Pandas (Carga y lectura eficiente del dataset estructurado en formato CSV).
*   **Control de Versiones:** Git & GitHub Desktop.

---

##  Instrucciones para Ejecución Local

Si deseas clonar este repositorio y ejecutar la aplicación web en tu entorno local, realiza los siguientes pasos en la terminal de tu computadora:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/AlfredoEnrique7/dashboard_cloud_deploy.git
   cd dashboard_cloud_deploy
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   conda create --name mi_entorno python=3.13 -y
   conda activate mi_entorno
   ```

3. **Instalar dependencias requeridas:**
   ```bash
   pip install -r requirements.txt
   conda install nbformat -y
   ```

4. **Arrancar el servidor de Streamlit:**
   ```bash
   streamlit run app.py
   ```

