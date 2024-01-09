import pandas as pd
import streamlit as st
import plotly.express as px

def read_processed_data():
    return pd.read_csv("dataset/processed/data.csv")

def restaurants_by_country(countries, selected_palette):
                """ Esta função cria um gráfico de barras com a quantidade de restaurantes por país"""
                df = read_processed_data()

                grouped_df = (
                    df.loc[df["country"].isin(countries), ["restaurant_id", "country"]]
                    .groupby("country")
                    .count()
                    .sort_values("restaurant_id", ascending=False)
                    .reset_index()
                )

                fig = px.bar(
                    grouped_df,
                    x="country",
                    y="restaurant_id",
                    text="restaurant_id",
                    title="Quantidade de Restaurantes Registrados por País",
                    labels={
                        "country": "Paises",
                        "restaurant_id": "Quantidade de Restaurantes",
                    },
                    color = "restaurant_id",
                    color_continuous_scale=selected_palette,
                )

                return fig

def cities_by_country(countries, selected_palette):
                """ Esta função cria um gráfico de barras com a quantidade de cidades por país"""

                df = read_processed_data()

                grouped_df = (
                    df.loc[df["country"].isin(countries), ["city", "country"]]
                    .groupby("country")
                    .nunique()
                    .sort_values("city", ascending=False)
                    .reset_index()
                )

                fig = px.bar(
                    grouped_df,
                    x="country",
                    y="city",
                    text="city",
                    title="Quantidade de Cidades Registrados por País",
                    labels={
                        "country": "Paises",
                        "city": "Quantidade de Cidades",
                    },
                    color = "city",
                    color_continuous_scale=selected_palette,
                )

                return fig

def average_votes_per_country(countries, selected_palette):
                """ Esta função cria um gráfico de barras com a média de avaliações por país"""
                
                df = read_processed_data()

                grouped_df = (
                    df.loc[df["country"].isin(countries), ["votes", "country"]]
                    .groupby("country")
                    .mean()
                    .sort_values("votes", ascending=False)
                    .reset_index()
                )

                fig = px.bar(
                    grouped_df,
                    x="country",
                    y="votes",
                    text="votes",
                    text_auto=".2f",
                    title="Média de Avaliações feitas por País",
                    labels={
                        "country": "Paises",
                        "votes": "Quantidade de Avaliações",
                    },
                    color = "votes",
                    color_continuous_scale=selected_palette,
                )

                return fig

def average_cost_for_two_per_country(countries, selected_palette):
                """ Esta função cria um gráfico de barras com a média de custo por dois por país"""
                
                df = read_processed_data()

                grouped_df = (
                    df.loc[df["country"].isin(countries), ["average_cost_for_two", "country"]]
                    .groupby("country")
                    .mean()
                    .sort_values("average_cost_for_two", ascending=False)
                    .reset_index()
                )

                fig = px.bar(
                    grouped_df,
                    x="country",
                    y="average_cost_for_two",
                    text="average_cost_for_two",
                    text_auto=".2f",
                    title="Média de Preço de um prato para duas pessoas por País",
                    labels={
                        "country": "Paises",
                        "average_cost_for_two": "Preço de prato para duas Pessoas",
                    },
                    color = "average_cost_for_two",
                    color_continuous_scale=selected_palette,
                )

                return fig