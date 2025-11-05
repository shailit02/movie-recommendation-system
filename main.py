from src.data_preprocessing import load_and_clean_data
from src.model_training import create_similarity_matrix

def run_pipeline():
    df = load_and_clean_data("data/movies.csv")
    similarity_matrix = create_similarity_matrix(df)
    return df, similarity_matrix

if __name__ == "__main__":
    df, sim = run_pipeline()
    print("✅ Data and similarity matrix ready!")
