import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load the processed dataset
df = pd.read_csv("data/data.csv")

# Selecting numerical features for clustering
features = ["valence", "danceability", "energy", "acousticness", 
            "instrumentalness", "liveness", "speechiness", "tempo"]

X = df[features]

# Standardizing features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)



kmeans = KMeans(n_clusters=25, random_state=42)
df["cluster_label"] = kmeans.fit_predict(X_scaled)

# Save the updated dataset
df.to_csv("data/advanced_spotify_data.csv", index=False)

# PCA for 2D visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)


def recommend_songs(song_name, df, n_recommendations=5):
    # Find song in dataset
    song = df[df["name"].str.lower() == song_name.lower()]
    if song.empty:
        return "Song not found!"
    
    # Compute similarity using Cosine Similarity
    song_index = song.index[0]
    similarity_scores = cosine_similarity([X_scaled[song_index]], X_scaled)
    
    # Get top N similar songs
    top_indices = np.argsort(similarity_scores[0])[::-1][1:n_recommendations+1]
    recommendations = df.iloc[top_indices][["name", "artists", "popularity"]]
    
    return recommendations