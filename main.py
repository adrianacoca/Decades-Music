import argparse
import requests
import os
import json
import pandas as pd
import numpy as np
import src.functions as func

top_artists = pd.read_csv('src/top_artist_id.csv')
top_artists = top_artists.to_dict()

top_artists = {"Elton John":"b83bc61f-8451-4a5d-8b8e-7e9ed295e822",
"Queen":"0383dadf-2a4e-4d10-a46a-e9e041da8eb3",
"ABBA":"d87e52c5-bb8d-4da8-b941-9f4928627dc8",
"The Beatles":"b10bbbfc-cf9e-42e0-be17-e2c3e1d2600d",
"Barbra Streisand":"56cd15a1-0d74-438b-8244-c96ffe1cae03", 
"Rihanna":"73e5e69d-3554-40d8-8516-00cb38737a1c",
"Whitney Houston":"0307edfc-437c-4b48-8700-80680e66a228",
"Mariah Carey":"494e8d09-f85b-4543-892f-a5096aed1cd4",
"Post Malone":"b1e26560-60e5-4236-bbdb-9aa5a8d5ee19",
"Taylor Swift":"20244d07-534f-4eff-b4d4-930878889970"}

# API Music Brainz
for key, value in top_artists.items():
    top_artists[key] = func.artist_location(value)
alldecades = pd.read_csv('output/music_decades.csv')
alldecades['Country'] = alldecades['Artist'].map(top_artists)


parser = argparse.ArgumentParser(description="Introduce the decade from 1950 - 2010 you would want to analyse, and either the top Artists or Genres of that decade")
parser.add_argument("-y", "--year", type=int, help="Introduce a decade from 1950-2010. Eg: 1970")
parser.add_argument("-c", "--column", type=str, help="Introduce 'Artist', 'Genre' or 'Country'")
parser.add_argument("-a", "--atribute", type=str, help="Introduce song atribute within 'Dance', 'Positiveness', 'Popularity'")
args = parser.parse_args()

def main():
    func.check_year(args.year)
    func.check_column(args.column)
    print (func.atributes(alldecades, args.atribute))
    print (func.results_by_year(alldecades, args.column, args.year))

if __name__ == '__main__':
    main()