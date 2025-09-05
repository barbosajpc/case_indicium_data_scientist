import pandas as pd

def conv_numerico(df):
    df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
    df['Released_Year'] = df['Released_Year'].astype('Int64')
    df['Gross'] = df['Gross'].str.replace(',', '').astype(float)
    df['Runtime'] = df['Runtime'].str.replace(' min', '').astype('Int64')

    return df