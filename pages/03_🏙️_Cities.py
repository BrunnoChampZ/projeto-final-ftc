#Description: This file contains the code for the Cities page of the Streamlit app.

# Importing the libraries
import streamlit as st
import pandas as pd
import plotly.express as px
from utils import cities_data as cdt

# Importing the data
df = cdt.read_processed_data()

# Function that creates the sidebar
def sidebar():

    """ Function that creates the sidebar """
    st.sidebar.markdown("## Filtros")

    all_countries = df.loc[:, "country"].unique().tolist()
    select_all_countries = st.sidebar.checkbox("Selecionar todos os países", True)

    if select_all_countries:
        selected_countries = all_countries
    else:
        selected_countries = st.sidebar.multiselect(
            "Escolha os Paises que Deseja visualizar as Informações:",
            all_countries[1:],  # Exclui "Todos" da lista
            default=["Brazil", "England", "India", "United States of America", "Turkey", "Australia"],
        )

    selected_palette = st.sidebar.selectbox(
        "Escolha a paleta de cores dos gráficos",
        px.colors.named_colorscales(), index=0
    )

    return selected_countries, selected_palette

# Main function
def main():

    """ Main function of the page """
    st.set_page_config(page_title="Cities", page_icon="🏙️", layout="wide")

    selected_countries, selected_palette = sidebar()

    st.markdown("# :cityscape: Visão Cidades")

    fig = cdt.top_cities_restaurants(selected_countries, selected_palette)

    st.plotly_chart(fig, use_container_width=True)

    best, worst = st.columns(2)

    with best:
        fig = cdt.top_best_restaurants(selected_countries, selected_palette)

        st.plotly_chart(fig, use_container_width=True)

    with worst:
        fig = cdt.top_worst_restaurants(selected_countries, selected_palette)

        st.plotly_chart(fig, use_container_width=True)

    fig = cdt.most_cuisines(selected_countries, selected_palette)

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()