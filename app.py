import streamlit as st
from src.data_preprocessing import load_and_clean_data
from src.model_training import create_similarity_matrix
from src.recommendation import recommend
import time

st.set_page_config(page_title=" Movie Recommendation System", page_icon="🎥", layout="centered")

st.markdown(
    """
    <style>
    .title {
        font-size:40px !important;
        color:#FF4B4B;
        text-align:center;
        font-weight:700;
        animation: fadeIn 2s ease-in-out;
    }
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='title'>🎬 Movie Recommendation System</div>", unsafe_allow_html=True)
st.markdown("### Welcome! Discover movies similar to your favorites with just one click.")

with st.spinner("Loading movie data... "):
    time.sleep(1.5)
    df = load_and_clean_data("data/movies.csv")
st.success(" Data Loaded Successfully!")

with st.spinner("Analyzing movie similarities... "):
    time.sleep(1)
    similarity_matrix = create_similarity_matrix(df)
st.success("✅ Model Ready!")

st.markdown("---")
st.header(" Get Your Movie Recommendations")

movie_list = df['title'].values
selected_movie = st.selectbox("Select a movie you like:", movie_list)

if st.button("🎞️ Recommend"):
    with st.spinner("Finding similar movies..."):
        time.sleep(1)
        recommendations = recommend(selected_movie, df, similarity_matrix)
    if recommendations:
        st.success(f"🍿 Because you liked **{selected_movie}**, you might also enjoy:")
        for i, movie in enumerate(recommendations, 1):
            time.sleep(0.3)
            st.markdown(f"🎬 **{i}. {movie}**")
    else:
        st.warning(" No similar movies found! Try another title.")



