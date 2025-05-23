import streamlit as st

st.set_page_config(layout="wide")
st.title("Visualizador Wayback - ArcGIS")

longitude = st.number_input("Longitude", value=-47.87859, format="%.6f")
latitude = st.number_input("Latitude", value=-15.76465, format="%.6f")

if st.button("Carregar Mapa"):
    url = f"https://livingatlas.arcgis.com/wayback/#active=27982&mapCenter={longitude}%2C{latitude}%2C19&animationSpeed=2000"

    html_code = f"""
    <div style="display: flex; justify-content: center; align-items: center; width: 100%;">
        <div style="position: relative; width: 90%; max-width: 1600px; height: 800px; border: 2px solid #ccc; border-radius: 8px; overflow: hidden;">
            <!-- X exatamente no centro -->
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 10; font-size: 68px; color: #ff4c4c;">
                ×
            </div>
            <iframe src="{url}" width="100%" height="100%" style="border: none;"></iframe>
        </div>
    </div>
    """

    st.components.v1.html(html_code, height=850)
