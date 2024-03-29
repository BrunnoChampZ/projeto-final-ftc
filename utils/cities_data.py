import pandas as pd
import streamlit as st
import plotly.express as px

def read_processed_data():
    """ Esta função lê o dataset processado"""
    return pd.read_csv("dataset/processed/data.csv")

def top_cities_restaurants(countries, selected_palette):
            """ Esta função cria um gráfico interativo de barras do top 10 cidades com mais restaurantes,
            de acordo com os países selecionados e com a paleta de cores escolhida"""
            df = read_processed_data()

            grouped_df = (
                df.loc[df["country"].isin(countries), ["restaurant_id", "country", "city"]]
                .groupby(["country", "city"])
                .count()
                .sort_values(["restaurant_id", "city"], ascending=[False, True])
                .reset_index()
            )

            fig = px.bar(
                grouped_df.head(10),
                x="city",
                y="restaurant_id",
                text="restaurant_id",
                text_auto=".2f",
                title="Top 10 Cidades com mais Restaurantes na Base de Dados",
                labels={
                    "city": "Cidade",
                    "restaurant_id": "Quantidade de Restaurantes",
                    "country": "País",
                },
                color="country",
                color_continuous_scale=selected_palette,
            )

            return fig

def top_best_restaurants(countries, selected_palette):
            """ Esta função cria um gráfico interativo de barras do top 7 cidades com restaurantes com média de avaliação acima de 4,
            de acordo com os países selecionados e com a paleta de cores escolhida"""
            df = read_processed_data()

            grouped_df = (
                df.loc[
                    (df["aggregate_rating"] >= 4) & (df["country"].isin(countries)),
                    ["restaurant_id", "country", "city"],
                ]
                .groupby(["country", "city"])
                .count()
                .sort_values(["restaurant_id", "city"], ascending=[False, True])
                .reset_index()
            )

            fig = px.bar(
                grouped_df.head(7),
                x="city",
                y="restaurant_id",
                text="restaurant_id",
                text_auto=".2f",
                title="Top 7 Cidades com Restaurantes com média de avaliação acima de 4",
                labels={
                    "city": "Cidade",
                    "restaurant_id": "Quantidade de Restaurantes",
                    "country": "País",
                },
                color="restaurant_id",
                color_continuous_scale=selected_palette,
            )

            return fig

def top_worst_restaurants(countries, selected_palette):
            """ Esta função cria um gráfico interativo de barras do top 7 cidades com restaurantes com média de avaliação abaixo de 2.5,
            de acordo com os países selecionados e com a paleta de cores escolhida"""
            df = read_processed_data()

            grouped_df = (
                df.loc[
                    (df["aggregate_rating"] <= 2.5) & (df["country"].isin(countries)),
                    ["restaurant_id", "country", "city"],
                ]
                .groupby(["country", "city"])
                .count()
                .sort_values(["restaurant_id", "city"], ascending=[False, True])
                .reset_index()
            )

            fig = px.bar(
                grouped_df.head(7),
                x="city",
                y="restaurant_id",
                text="restaurant_id",
                text_auto=".2f",
                title="Top 7 Cidades com Restaurantes com média de avaliação abaixo de 2.5",
                labels={
                    "city": "Cidade",
                    "restaurant_id": "Quantidade de Restaurantes",
                    "country": "País",
                },
                color="restaurant_id",
                color_continuous_scale=selected_palette,
            )

            return fig

def most_cuisines(countries, selected_palette):
            """ Esta função cria um gráfico interativo de barras do top 10 cidades com restaurantes com tipos culinários distintos,
            de acordo com os países selecionados e com a paleta de cores escolhida"""
            df = read_processed_data()

            grouped_df = (
                df.loc[df["country"].isin(countries), ["cuisines", "country", "city"]]
                .groupby(["country", "city"])
                .nunique()
                .sort_values(["cuisines", "city"], ascending=[False, True])
                .reset_index()
            )

            fig = px.bar(
                grouped_df.head(10),
                x="city",
                y="cuisines",
                text="cuisines",
                title="Top 10 Cidades mais restaurantes com tipos culinários distintos",
                labels={
                    "city": "Cidades",
                    "cuisines": "Quantidade de Tipos Culinários Únicos",
                    "country": "País",
                },
                color="cuisines",
                color_continuous_scale=selected_palette,
            )

            return fig