import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("movie_data/movies.csv", encoding="latin-1", sep="\t", usecols=["title", "genres"])
data["genres"] = data["genres"].apply(lambda s: s.replace("|", " ").replace("-",""))
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data["genres"])
tfidf_matrix_dense = pd.DataFrame(tfidf_matrix.todense(), columns=vectorizer.get_feature_names_out(), index=data["title"])

cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim_df = pd.DataFrame(cosine_sim, index=data["title"], columns=data["title"])

seen_movie = "Heat (1995)"
top_k = 20

top_movies = cosine_sim_df[seen_movie].sort_values(ascending=False)[:top_k]

