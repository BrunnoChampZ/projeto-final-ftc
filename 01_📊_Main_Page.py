# Description: Main page of the project

# Importing the libraries
import pandas as pd
import streamlit as st
import folium
from PIL import Image
from streamlit_folium import folium_static

from utils.process_data import process_data

# Importing the data
RAW_DATA_PATH = f"./dataset/raw/data.csv"

# =======================================
# Functions
# =======================================

# Function that creates the sidebar
def sidebar(df):

    """ Function that creates the sidebar """
    image = Image.open("./img/logo.jpg")
    st.sidebar.image(image, width=25)

    st.sidebar.markdown("# Fome Zero!")
    st.sidebar.markdown("## Filtros")

    countries_options = st.sidebar.multiselect(
        "Escolha os Paises que Deseja visualizar os Restaurantes",
        df.loc[:, "country"].unique().tolist(),
        default=["Brazil", "England", "India", "United States", "Turkey", "Australia"],
    )

    st.sidebar.markdown("## Dados Tratados")

    processed_data = pd.read_csv("./dataset/processed/data.csv")

    st.sidebar.download_button(
        label="Download",
        data=processed_data.to_csv(index=False),
        file_name="data.csv",
        mime="text/csv",
    )

    return list(countries_options)

# Function that creates the leaflet map
def create_leaflet_map(df):

    """ Function that creates the leaflet map """
    map = folium.Map(location=[df["latitude"].mean(), df["longitude"].mean()], zoom_start=1)
    marker_cluster = folium.plugins.MarkerCluster().add_to(map)

    for index, row in df.iterrows():

        popup_content = f"""
        <b>{row["restaurant_name"]}</b><br>
        <p>Preço: {row["average_cost_for_two"]} {row["currency"]} para dois<br>
        Tipo: {row["cuisines"]}<br>
        Avaliação: {row["aggregate_rating"]}/5.0</p>
        Comentário: {row["rating_text"]}</p>
        """

        folium.Marker([row["latitude"], row["longitude"]], popup=folium.Popup(popup_content, max_width=300), icon=folium.Icon(icon="home", color=row["color_name"])).add_to(marker_cluster)

    folium_static(map, width=1000, height=700)

# Main function
def main():

    df = process_data(RAW_DATA_PATH)

    st.set_page_config(page_title="Home", layout="wide")

    selected_countries = sidebar(df)

    st.write("# Fome Zero!")
    st.write("## O Melhor lugar para encontrar seu mais novo restaurante favorito!")
    st.write("### Temos as seguintes marcas dentro da nossa plataforma:")

    tab1 = st.container()

    with tab1:
        with st.container():

            col1, col2, col3, col4, col5 = st.columns(5, gap = "large")
            with col1:
                #restaurantes cadastrados
                restaurantes = df["restaurant_id"].nunique()
                col1.metric("Restaurantes cadastrados", restaurantes)
            
            with col2:
                #países cadastrados
                paises = df["country"].nunique()
                col2.metric("Países Cadastrados", paises)
                
            with col3:
                #cidades cadastradas
                cidades = df["city"].nunique()
                col3.metric("Cidades cadastradas", cidades)

            with col4:
                #Total de avaliações cadastradas divididas por 3 casas decimais
                avaliacoes = df["votes"].sum()
                col4.metric("Avaliações feitas na plataforma", avaliacoes)
            
            with col5:
                #tipos de culinárias oferecidas
                culinarias = df["cuisines"].nunique()
                col5.metric("Tipos de culinárias", culinarias)
    
        map_df = df.loc[df["country"].isin(selected_countries), :]
        create_leaflet_map(map_df)

        return None

    if __name__ == "__main__":
        main()