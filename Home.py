#libraries
import streamlit as st
from PIL import Image
import pandas as pd
import inflection
import folium
from streamlit_folium import folium_static

st.set_page_config(page_title="Home", layout="wide")

image = Image.open("logo.jpg")
st.sidebar.image(image, width=25)

st.sidebar.markdown("# Fome Zero!")
st.sidebar.markdown("## Filtros")
st.sidebar.caption("Escolha os Paises que Deseja visualizar os Restaurantes")

# =======================================
# Funções
# =======================================
def create_map(df):
    m = folium.Map(location=[df["latitude"].mean(), df["longitude"].mean()], zoom_start=3, layout="wide")

    for index, row in df.iterrows():
        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=f"{row['restaurant_name']} ({row['country']})",
            icon=folium.Icon(color=row["color_name"])
        ).add_to(m)

    return m

def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new

    return df

def clean_code (df):
    """ Esta função limpa os dados do dataset
    """

    # Removendo espaços dos nomes das colunas
    df.columns = df.columns.str.replace(' ', '_')

    # Removendo colunas que não serão utilizadas
    df.drop(["switch_to_order_menu"], axis=1, inplace=True)

    # Removendo linhas duplicadas de Restaurant_ID
    df.drop_duplicates(subset="restaurant_id", keep="first", inplace=True)

    #Removendo valores "NaN" de todas as colunas
    df.dropna(inplace=True)

    #Categorizando todos os restaurantes somente por um topo de culinária
    df["cuisines"] = df["cuisines"].apply(lambda x: str(x).split(",")[0] if pd.notnull(x) else x)

    #Remover valores "NaN" da coluna "Cuisines"
    df = df[df["cuisines"].notnull()]

    #Inserindo a coluna "price_type" no dataset
    df.insert(loc=10, column="price_type", value=df["price_range"].apply(create_price_type))

    #Inserindo a coluna "color_name" no dataset
    df.insert(loc=19, column="color_name", value=df["rating_color"].apply(color_name))

    return df

COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zealand",
    162: "Phillipines",
    166: "Qatar",
    184: "Singapore",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "United Kingdom",
    216: "United States"
}

def country_name(country_id):
    return COUNTRIES[country_id]

def create_price_type(price_range):

    if price_range == "1":
        return "cheap"
    elif price_range == "2":
        return "normal"
    elif price_range == "3":
        return "expensive"
    else:
        return "gourmet"
    
COLORS = {
    "3F7E00": "dark_green",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "lightred",
}

def color_name(color_code):
    return COLORS[color_code]

def country_name(df):
    df.insert(loc=2, column="country", value=df["country_code"].apply(lambda x: COUNTRIES.get(x, "")))
    df.drop(["country_code"], axis=1, inplace=True)
    return df

# --------------------------------------- Inicio da Estrutura lógica do código --------------------------------------- #

# ---------------------------------------
# Import dataset
# ---------------------------------------
df = pd.read_csv("dataset/zomato.csv")

# Renomeando as colunas
df = rename_columns(df)
df = country_name(df)

df1 = df.copy()

# Limpando os dados
df1 = clean_code(df)

st.write("# Fome Zero!")
st.write("## O Melhor lugar para encontrar seu mais novo restaurante favorito!")
st.write("### Temos as seguintes marcas dentro da nossa plataforma:")


# =======================================
# Layout no streamlit
# =======================================

countries_options = st.sidebar.multiselect(
    "Escolha os Paises que Deseja visualizar os Restaurantes",
    options=list(COUNTRIES.values()),
    default=["Brazil", "United States", "India", "United Kingdom", "Turkey", "Australia"]
)

tab1 = st.container()

with tab1:
    with st.container():

        col1, col2, col3, col4, col5 = st.columns(5, gap = "large")
        with col1:
            #restaurantes cadastrados
            restaurantes = df1["restaurant_id"].nunique()
            col1.metric("Restaurantes cadastrados", restaurantes)
        
        with col2:
            #países cadastrados
            paises = df1["country"].nunique()
            col2.metric("Países Cadastrados", paises)
            
        with col3:
            #cidades cadastradas
            cidades = df1["city"].nunique()
            col3.metric("Cidades cadastradas", cidades)

        with col4:
            #avaliações cadastradas
            avaliacoes = df1["votes"].sum()
            col4.metric("Avaliações cadastradas", avaliacoes)
        
        with col5:
            #tipos de culinárias oferecidas
            culinarias = df1["cuisines"].nunique()
            col5.metric("Tipos de culinárias", culinarias)

# Filtrar os dados com base nos países selecionados
filtered_df = df1[df1["country"].isin(countries_options)]

# Criar o mapa
folium_static(create_map(filtered_df))