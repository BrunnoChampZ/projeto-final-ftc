import streamlit as st
import plotly.express as px
from utils import cities_data as cdt

def make_sidebar(df):
    st.sidebar.markdown("## Filtros")

    countries = st.sidebar.multiselect(
        "Escolha os Paises que Deseja visualizar as Informações",
        df.loc[:, "country"].unique().tolist(),
        default=["Brazil", "United Kingdom", "India", "United States", "Turkey", "Australia"],
    )

    selected_palette = st.sidebar.selectbox(
        "Escolha a paleta de cores dos gráficos",
        px.colors.named_colorscales(), index=4
    )

    return list(countries), selected_palette


def main():
    st.set_page_config(page_title="Cities", page_icon="🏙️", layout="wide")

    df = cdt.read_processed_data()

    countries,selected_palette = make_sidebar(df)

    st.markdown("# :cityscape: Visão Cidades")

    fig = cdt.top_cities_restaurants(countries, selected_palette)

    st.plotly_chart(fig, use_container_width=True)

    best, worst = st.columns(2)

    with best:
        fig = cdt.top_best_restaurants(countries, selected_palette)

        st.plotly_chart(fig, use_container_width=True)

    with worst:
        fig = cdt.top_worst_restaurants(countries, selected_palette)

        st.plotly_chart(fig, use_container_width=True)

    fig = cdt.most_cuisines(countries, selected_palette)

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()