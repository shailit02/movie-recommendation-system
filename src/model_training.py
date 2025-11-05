from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def create_similarity_matrix(df):
    cv = CountVectorizer(stop_words='english')
    count_matrix = cv.fit_transform(df['combined'])
    similarity = cosine_similarity(count_matrix)
    return similarity
