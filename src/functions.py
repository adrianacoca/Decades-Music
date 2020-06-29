# entity options: area, artist, event, instrument, label, place, recording, release, release-group, series, work, url
import requests
import os
import json

def artist_location(mbid):
    url = f"http://musicbrainz.org/ws/2/artist/{mbid}?inc=aliases&fmt=json"
    res = requests.get(url)
    data = res.json()
    return data["area"]["name"]


def results_by_year(df, column, year): 
    decade = df.loc[df['Year'] == year]
    return decade[f'{column}'].value_counts().head(10)

def atributes(df, atribute):
    return df.groupby("Year").agg({f"{atribute}":"mean"})

def check_year(year):
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    if year not in years: 
        raise ValueError("Invalid input. Please try one of the following decades" + str(years))

def check_column(column):
    columns = ["Artist", "Genre", "Country"]
    if column not in columns: 
        raise ValueError("Invalid input. Please try one of the following decades" + str(columns))

def check_atribute(atribute):
    atributes = ['Dance', 'Positiveness', 'Popularity']
    if atribute not in atributes: 
        raise ValueError("Invalid input. Please try one of the following atributes" + str(atributes))
