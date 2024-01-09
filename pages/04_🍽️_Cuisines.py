import streamlit as st
import plotly.express as px
from utils import cuisines_data as cdt


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

    top_n = st.sidebar.slider(
        "Selecione a quantidade de Restaurantes que deseja visualizar", 1, 20, 10
    )

    cuisines = st.sidebar.multiselect(
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

    return list(countries), top_n, list(cuisines), selected_palette


def main():
    st.set_page_config(page_title="Cuisines", page_icon="🍽️", layout="wide")

    df = cdt.read_processed_data()

    countries, top_n, cuisines, selected_pallete = make_sidebar(df)

    st.markdown("# :knife_fork_plate: Visão Tipos de Cusinhas")

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