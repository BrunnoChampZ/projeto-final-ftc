import streamlit as st
import plotly.express as px
from utils import countries_data as cdt

def make_sidebar(df):
    """ Esta função cria a sidebar da página"""
    st.sidebar.markdown("## Filtros")

    countries = st.sidebar.multiselect(
        "Escolha os Paises que Deseja visualizar as Informações",
        df.loc[:, "country"].unique().tolist(),
        default=["Brazil", "United Kingdom", "India", "United States", "Turkey", "Australia"],
    )

    selected_palette = st.sidebar.selectbox(
        "Escolha a paleta de cores dos gráficos", px.colors.named_colorscales(), index = 4
    )

    return list(countries), selected_palette

def main():
    """ Função principal da página"""
    st.set_page_config(page_title="Countries", page_icon="🌍", layout="wide")

    df = cdt.read_processed_data()

    countries, selected_palette = make_sidebar(df)

    st.markdown("# :earth_americas: Visão Países")

    fig = cdt.restaurants_by_country(countries, selected_palette)

    st.plotly_chart(fig, use_container_width=True)

    fig = cdt.cities_by_country(countries, selected_palette)

    st.plotly_chart(fig, use_container_width=True)

    votes, plate_price = st.columns(2)

    with votes:
        fig = cdt.average_votes_per_country(countries, selected_palette)

        st.plotly_chart(fig, use_container_width=True)

    with plate_price:
        fig = cdt.average_cost_for_two_per_country(countries, selected_palette)

        st.plotly_chart(fig, use_container_width=True)

    return None

if __name__ == "__main__":
    main()