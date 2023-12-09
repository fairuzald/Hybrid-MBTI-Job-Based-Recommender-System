from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import numpy as np
import skfuzzy as fuzz

# Membuat matriks fitur lagu
song_features = np.array([song['features'] for song in songs])

# Membuat matriks preferensi pengguna
user_preferences = np.array([user['preferences'] for user in users])

# Menghitung skor CBF dengan cosine similarity
cbf_scores = cosine_similarity(user_preferences, song_features)

# Menghitung skor CF dengan k-nearest neighbors
song_user_matrix = csr_matrix(user_song_data.values)
model_knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
model_knn.fit(song_user_matrix)
distances, indices = model_knn.kneighbors(user_preferences)
cf_scores = 1 - distances

# Menggabungkan skor CBF dan CF
hybrid_scores = (cbf_scores + cf_scores) / 2

# Menggunakan algoritma Fuzzy untuk menyesuaikan skor berdasarkan konteks pengguna
context = get_user_context(user)
fuzzy_scores = fuzz.interp_membership(np.arange(0, 1, 0.01), context, hybrid_scores)

# Mengembalikan lagu dengan skor tertinggi
recommended_song = songs[np.argmax(fuzzy_scores)]
