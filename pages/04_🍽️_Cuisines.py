# Description: This file contains the code for the Cuisines page of the Streamlit web app.

# Importing the libraries
import streamlit as st
import plotly.express as px
from utils import cuisines_data as cdt

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
            "Escolha os Paises que Deseja visualizar as Informações",
            all_countries[1:],  # Exclui "Todos" da lista
            default=["Brazil", "England", "India", "United States of America", "Turkey", "Australia"],
        )

    selected_palette = st.sidebar.selectbox(
        "Escolha a paleta de cores dos gráficos",
        px.colors.named_colorscales(), index=0
    )

    top_n = st.sidebar.slider(
        "Selecione a quantidade de Restaurantes que deseja visualizar", 1,10,20
    )

    select_all_cuisines = st.sidebar.checkbox("Selecionar todas as cozinhas", True)
    
    if select_all_cuisines:
        selected_cuisines = df.loc[:, "cuisines"].unique().tolist()
    else:
        selected_cuisines = st.sidebar.multiselect(
            "Escolha os Tipos de Culinária ",
            df.loc[:, "cuisines"].unique().tolist(),
            default=[
                "Home-made",
                "BBQ",
                "Japanese",
                "Brazilian",
                "Arabian",
                "American",
                "Italian",
            ],
        )

    return selected_countries, top_n, selected_cuisines, selected_palette

# Main function
def main():

    """ Main function of the page """
    st.set_page_config(page_title="Cuisines", page_icon="🍽️", layout="wide")

    df = cdt.read_processed_data()

    countries, top_n, cuisines, selected_pallete = sidebar()

    st.markdown("# :knife_fork_plate: Visão Tipos de Culinárias")

    df_restaurants = cdt.top_restaurants(countries, cuisines, top_n)

    st.markdown(f"## Melhores Restaurantes dos Principais tipos Culinários")

    cdt.write_metrics()

    st.markdown(f"## Top {top_n} Restaurantes")

    st.dataframe(df_restaurants)

    best, worst = st.columns(2)

    with best:
        fig = cdt.top_best_cuisines(countries, top_n, selected_pallete)

        st.plotly_chart(fig, use_container_width=True)

    with worst:
        fig = cdt.top_worst_cuisines(countries, top_n, selected_pallete)

        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()