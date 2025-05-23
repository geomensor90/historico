import streamlit as st

# Força o layout para ocupar toda a largura da tela
st.set_page_config(layout="wide")

st.title("Visualizador de imagens históricas")

# Entradas para as coordenadas
longitude = st.number_input("Longitude", value=-47.87859, format="%.6f")
latitude = st.number_input("Latitude", value=-15.76465, format="%.6f")

# Botão para carregar o mapa
if st.button("Carregar Mapa"):
    url = f"https://livingatlas.arcgis.com/wayback/#active=27982&mapCenter={longitude}%2C{latitude}%2C19&animationSpeed=2000"
    st.components.v1.iframe(url, width=1800, height=800, scrolling=True)
