import pandas as pd
import requests
import dotenv
import os

dotenv.load_dotenv()
OMDB_API_KEY = os.getenv('OMDB_API_KEY')

def conv_numerico(df):
    df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
    df['Released_Year'] = df['Released_Year'].astype('Int64')
    df['Gross'] = df['Gross'].str.replace(',', '').astype(float)
    df['Runtime'] = df['Runtime'].str.replace(' min', '').astype('Int64')

    return df

def buscar_dados_omdb(titulo):
    url = "http://www.omdbapi.com/"
    params = {
        "apikey": OMDB_API_KEY,
        "t": titulo,
    }
    
    r = requests.get(url, params=params, timeout=5)
    data = r.json()
    if data.get("Response") == "True":
        return {
            "Series_Title": data.get("Title"),
            "Released_Year": data.get("Year"),
            "Certificate": data.get("Rated"),
            "Meta_score": data.get("Metascore"),
            "Gross": data.get("BoxOffice")
            }
    return None