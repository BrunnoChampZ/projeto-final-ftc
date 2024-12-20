# Description: This file contains the functions that process the data from the dataset.

# Importing the libraries
import inflection
import pandas as pd

# Function that lists all countries
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
    215: "England",
    216: "United States of America"
}

# Function that lists the colors of the flags
COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "lightred",
}

def rename_columns(dataframe):
    """" Function that renames the columns of a dataframe """
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

def country_name(country_id):
    """ Function that returns the name of a country """
    return COUNTRIES[country_id]

def color_name(color_code):
    """ Function that returns the name of a color """
    return COLORS[color_code]

def create_price_type(price_range):
    """ Function that returns the type of price range """
    if price_range == "1":
        return "cheap"
    elif price_range == "2":
        return "normal"
    elif price_range == "3":
        return "expensive"
    else:
        return "gourmet"

def columns_order(dataframe):
    """ Function that changes the order of the columns """	
    df = dataframe.copy()

    new_cols_order = [
        "restaurant_id",
        "restaurant_name",
        "country",
        "city",
        "address",
        "locality",
        "locality_verbose",
        "longitude",
        "latitude",
        "cuisines",
        "price_type",
        "average_cost_for_two",
        "currency",
        "has_table_booking",
        "has_online_delivery",
        "is_delivering_now",
        "aggregate_rating",
        "rating_color",
        "color_name",
        "rating_text",
        "votes",
    ]

    return df.loc[:, new_cols_order]

def process_data(file_path):
    """ Function that processes the data """

    df = pd.read_csv(file_path)

    df = rename_columns(df)

    df = df.dropna()

    df["price_type"] = df.loc[:, "price_range"].apply(lambda x: create_price_type(x))

    df["country"] = df.loc[:, "country_code"].apply(lambda x: country_name(x))

    df["color_name"] = df.loc[:, "rating_color"].apply(lambda x: color_name(x))

    df["cuisines"] = df.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])

    df = df.drop(df[(df["cuisines"] == "Drinks Only")].index)

    df = df.drop(df[(df["cuisines"] == "Mineira")].index)

    df = df.drop_duplicates()

    df = columns_order(df)

    df.to_csv("./dataset/processed/data.csv", index=False)

    return df