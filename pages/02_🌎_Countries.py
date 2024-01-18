import streamlit as st
import plotly.express as px
from utils import countries_data as cdt

def sidebar(df):
    """ Esta função cria a sidebar da página"""
    st.sidebar.markdown("## Filtros")

    all_countries = ["Todos"] + df.loc[:, "country"].unique().tolist()

    container = st.sidebar.container()
    select_all = container.checkbox("Selecionar todos os países")

    if select_all:
        selected_countries = container.multiselect(
            "Escolha os Paises que Deseja visualizar as Informações:",
            all_countries,
            default=all_countries,
        )
    else:
        selected_countries = container.multiselect(
            "Escolha os Paises que Deseja visualizar as Informações:",
            all_countries[1:],  # Exclui "Todos" da lista
            default=["Brazil", "United Kingdom", "India", "United States", "Turkey", "Australia"],
        )

    selected_palette = st.sidebar.selectbox(
        "Escolha a paleta de cores dos gráficos", px.colors.named_colorscales(), index=4
    )

    return selected_countries, selected_palette

def main():
    """ Função principal da página"""
    st.set_page_config(page_title="Countries", page_icon="🌍", layout="wide")

    df = cdt.read_processed_data()

    selected_countries, selected_palette = sidebar(df)

    st.markdown("# :earth_americas: Visão Países")

    fig = cdt.restaurants_by_country(selected_countries, selected_palette)

    st.plotly_chart(fig, use_container_width=True)

    fig = cdt.cities_by_country(selected_countries, selected_palette)

    st.plotly_chart(fig, use_container_width=True)

    votes, plate_price = st.columns(2)

    with votes:
        fig = cdt.average_votes_per_country(selected_countries, selected_palette)

        st.plotly_chart(fig, use_container_width=True)

    with plate_price:
        fig = cdt.average_cost_for_two_per_country(selected_countries, selected_palette)

        st.plotly_chart(fig, use_container_width=True)

    return None

if __name__ == "__main__":
    main()