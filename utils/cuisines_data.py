# Description: This file contains the functions that are used to read the processed data, get the top 1 restaurant for each cuisine, write the metrics, get the top N restaurants by cuisine and country

# Importing the libraries
import  pandas as pd
import streamlit as st
import plotly.express as px

# Importing the data
def read_processed_data(file_path):
    """ Function that reads the processed data """
    
    return pd.read_csv("dataset/processed/data.csv")

# Functions to get the top 1 restaurant for each cuisine
def top_cuisines():

            """ Function that returns the top 1 restaurant for each cuisine """
            df = read_processed_data()

            cuisines = {
                "Italian": "",
                "American": "",
                "Arabian": "",
                "Japanese": "",
                "Brazilian": "",
            }

            cols = [
                "restaurant_id",
                "restaurant_name",
                "country",
                "city",
                "cuisines",
                "average_cost_for_two",
                "currency",
                "aggregate_rating",
                "votes",
            ]

            for key in cuisines.keys():

                lines = df["cuisines"] == key

                cuisines[key] = (
                    df.loc[lines, cols]
                    .sort_values(["aggregate_rating", "restaurant_id"], ascending=[False, True])
                    .iloc[0, :]
                    .to_dict()
                )

            return cuisines

# Function to write the metrics
def write_metrics():
       
            """ Function that writes the metrics """
            cuisines = top_cuisines()

            italian, american, arabian, japanese, brazilian = st.columns(len(cuisines))

            with italian:
                st.metric(
                    label=f'Italiana: {cuisines["Italian"]["restaurant_name"]}',
                    value=f'{cuisines["Italian"]["aggregate_rating"]}/5.0',
                    help=f"""
                    País: {cuisines["Italian"]['country']}\n
                    Cidade: {cuisines["Italian"]['city']}\n
                    Média Prato para dois: {cuisines["Italian"]['average_cost_for_two']} ({cuisines["Italian"]['currency']})
                    """,
                )

            with american:
                st.metric(
                    label=f'Americana: {cuisines["American"]["restaurant_name"]}',
                    value=f'{cuisines["American"]["aggregate_rating"]}/5.0',
                    help=f"""
                    País: {cuisines["American"]['country']}\n
                    Cidade: {cuisines["American"]['city']}\n
                    Média Prato para dois: {cuisines["American"]['average_cost_for_two']} ({cuisines["American"]['currency']})
                    """,
                )

            with arabian:
                st.metric(
                    label=f'Árabe: {cuisines["Arabian"]["restaurant_name"]}',
                    value=f'{cuisines["Arabian"]["aggregate_rating"]}/5.0',
                    help=f"""
                    País: {cuisines["Arabian"]['country']}\n
                    Cidade: {cuisines["Arabian"]['city']}\n
                    Média Prato para dois: {cuisines["Arabian"]['average_cost_for_two']} ({cuisines["Arabian"]['currency']})
                    """,
                )

            with japanese:
                st.metric(
                    label=f'Japonesa: {cuisines["Japanese"]["restaurant_name"]}',
                    value=f'{cuisines["Japanese"]["aggregate_rating"]}/5.0',
                    help=f"""
                    País: {cuisines["Japanese"]['country']}\n
                    Cidade: {cuisines["Japanese"]['city']}\n
                    Média Prato para dois: {cuisines["Japanese"]['average_cost_for_two']} ({cuisines["Japanese"]['currency']})
                    """,
                )

            with brazilian:
                st.metric(
                    label=f'Brasileira: {cuisines["Brazilian"]["restaurant_name"]}',
                    value=f'{cuisines["Brazilian"]["aggregate_rating"]}/5.0',
                    help=f"""
                    País: {cuisines["Brazilian"]['country']}\n
                    Cidade: {cuisines["Brazilian"]['city']}\n
                    Média Prato para dois: {cuisines["Brazilian"]['average_cost_for_two']} ({cuisines["Brazilian"]['currency']})
                    """,
                )

            return None

# Function to get the top N restaurants by cuisine and country
def top_restaurants(countries, cuisines, top_n):
      
            """ Function that returns the top N restaurants by cuisine and country """
            df = read_processed_data()

            cols = [
                "restaurant_id",
                "restaurant_name",
                "country",
                "city",
                "cuisines",
                "average_cost_for_two",
                "aggregate_rating",
                "votes",
            ]

            lines = (df["cuisines"].isin(cuisines)) & (df["country"].isin(countries))

            dataframe = df.loc[lines, cols].sort_values(
                ["aggregate_rating", "restaurant_id"], ascending=[False, True]
            )

            return dataframe.head(top_n)

# Function to get the top N best cuisines
def top_best_cuisines(countries, top_n, selected_palette):
      
            """ Function that creates a bar chart with the top N best cuisines """
            df = read_processed_data()

            lines = df["country"].isin(countries)

            grouped_df = (
                df.loc[lines, ["aggregate_rating", "cuisines"]]
                .groupby("cuisines")
                .mean()
                .sort_values("aggregate_rating", ascending=False)
                .reset_index()
                .head(top_n)
            )

            fig = px.bar(
                grouped_df.head(top_n),
                x="cuisines",
                y="aggregate_rating",
                text="aggregate_rating",
                text_auto=".2f",
                title=f"Top {top_n} Melhores Tipos de Culinárias",
                labels={
                    "cuisines": "Tipo de Culinária",
                    "aggregate_rating": "Média da Avaliação Média",
                },
                color="aggregate_rating",
                color_continuous_scale=selected_palette,
            )

            return fig

# Function to get the top N worst cuisines
def top_worst_cuisines(countries, top_n, selected_palette):
      
            """ Function that creates a bar chart with the top N worst cuisines """
            df = read_processed_data()

            lines = df["country"].isin(countries)

            grouped_df = (
                df.loc[lines, ["aggregate_rating", "cuisines"]]
                .groupby("cuisines")
                .mean()
                .sort_values("aggregate_rating")
                .reset_index()
                .head(top_n)
            )

            fig = px.bar(
                grouped_df.head(top_n),
                x="cuisines",
                y="aggregate_rating",
                text="aggregate_rating",
                text_auto=".2f",
                title=f"Top {top_n} Piores Tipos de Culinárias",
                labels={
                    "cuisines": "Tipo de Culinária",
                    "aggregate_rating": "Média da Avaliação Média",
                },
                color="aggregate_rating",
                color_continuous_scale=selected_palette,
            )

            return fig