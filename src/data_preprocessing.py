import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df = df[['title', 'cast', 'crew']].fillna('')
    df['combined'] = df['title'] + " " + df['cast'] + " " + df['crew']
    return df
