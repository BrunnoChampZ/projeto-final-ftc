# Description: This file contains the functions that are used to create the charts that are displayed in the cities page.

# Importing the libraries
import pandas as pd
import streamlit as st
import plotly.express as px

# Importing the data
def read_processed_data():
    """ Function that reads the processed data """
    
    return pd.read_csv("dataset/processed/data.csv")

# Functions to create the charts
def top_cities_restaurants(countries, selected_palette):

            """ Function that creates a bar chart with the top 10 cities with the most restaurants """
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
        
            """ Function that creates a bar chart with the top 7 cities with the best restaurants """
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
        
            """ Function that creates a bar chart with the top 7 cities with the worst restaurants """
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
        
            """ Function that creates a bar chart with the top 10 cities with the most distinct cuisines """
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