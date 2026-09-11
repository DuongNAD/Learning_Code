"""
03_Unsupervised_Learning: Content-Based Recommender System
==========================================================
Demonstrates content-based filtering on MovieLens dataset:
- Text feature processing on movie genres
- TF-IDF Vectorization
- Pairwise Cosine Similarity computation
- Top-K recommendation generation with similarity ranking
"""

import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(CURRENT_DIR, "movie_data/movies.csv")
if not os.path.exists(DATA_PATH):
    DATA_PATH = os.path.join(CURRENT_DIR, "../../06_Datasets_Kaggle/movie_lens/movies.csv")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"MovieLens dataset not found at {DATA_PATH}")


class ContentBasedRecommender:
    """Hệ thống gợi ý phim dựa trên độ tương đồng nội dung (thể loại phim)."""

    def __init__(self, data_path: str = DATA_PATH):
        self.data_path = data_path
        self.movies_df = None
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = None
        self.cosine_sim_df = None
        self._fit()

    def _fit(self):
        self.movies_df = pd.read_csv(
            self.data_path,
            encoding="latin-1",
            sep="\t",
            usecols=["title", "genres"]
        )
        # Chuẩn hoá thể loại: thay thế dấu '|' và '-' bằng khoảng trắng
        cleaned_genres = self.movies_df["genres"].apply(
            lambda s: str(s).replace("|", " ").replace("-", "")
        )
        self.tfidf_matrix = self.vectorizer.fit_transform(cleaned_genres)
        cosine_sim = cosine_similarity(self.tfidf_matrix)
        self.cosine_sim_df = pd.DataFrame(
            cosine_sim,
            index=self.movies_df["title"],
            columns=self.movies_df["title"]
        )

    def recommend(self, movie_title: str, top_k: int = 10) -> pd.DataFrame:
        """
        Trả về danh sách top_k bộ phim có độ tương đồng cao nhất với movie_title.
        """
        if movie_title not in self.cosine_sim_df:
            # Thử tìm kiếm gần đúng (fuzzy match theo tên)
            matches = [t for t in self.cosine_sim_df.columns if movie_title.lower() in t.lower()]
            if not matches:
                raise ValueError(f"Không tìm thấy phim '{movie_title}' trong cơ sở dữ liệu.")
            movie_title = matches[0]

        sim_scores = self.cosine_sim_df[movie_title].drop(movie_title).sort_values(ascending=False)[:top_k]
        
        # Ghép thể loại vào kết quả
        genre_map = self.movies_df.set_index("title")["genres"].to_dict()
        results = []
        for title, score in sim_scores.items():
            results.append({
                "Tên phim gợi ý": title,
                "Thể loại": genre_map.get(title, "N/A"),
                "Độ tương đồng Cosine": round(float(score), 4)
            })
        return pd.DataFrame(results)


def main():
    print(f"Khởi tạo Hệ thống Gợi ý Phim từ: {DATA_PATH}...")
    recommender = ContentBasedRecommender(DATA_PATH)
    
    seen_movie = "Heat (1995)"
    print(f"\n=== GỢI Ý PHIM CHO KHÁN GIẢ ĐÃ XEM: '{seen_movie}' ===")
    recommendations = recommender.recommend(seen_movie, top_k=10)
    print(recommendations.to_string(index=False))


if __name__ == "__main__":
    main()
