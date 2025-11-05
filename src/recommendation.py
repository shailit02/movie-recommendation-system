import streamlit as st

def recommend(movie_name, df, similarity_matrix, top_n=5):
    if movie_name not in df['title'].values:
        st.warning(f"⚠️ '{movie_name}' not found in the dataset!")
        return []
    idx = df[df['title'] == movie_name].index[0]
    distances = list(enumerate(similarity_matrix[idx]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)[1:top_n+1]
    recommendations = [df.iloc[i[0]].title for i in distances]
    return recommendations
