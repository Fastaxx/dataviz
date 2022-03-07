import streamlit as st
import pandas as pd
import numpy as np
import folium
from pycountry_convert import country_alpha2_to_continent_code, country_name_to_country_alpha2
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="app")
def geolocate(country):
	try:
		loc = geolocator.geocode(country)
		return (loc.latitude, loc.longitude)
	except:
		return np.nan

df = pd.read_csv("independance-energetique-en-gaz-naturel-en-europe.csv",sep=";")
new_df = df.assign(Coordonnees = (0,0))
st.write(new_df)

for row in df.index:
	pays = df["Pays (EN)"][row]
	coordonnees = geolocate(pays)
	df.insert(4,"Coordonnees", coordonnees)


