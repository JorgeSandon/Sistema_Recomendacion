import streamlit as st
import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD

# Cargar los datos
ratings = pd.read_csv("datos\ratings.csv") 
movies = pd.read_csv("datos\movies.csv")  

# Limpieza y preparación de datos
ratings = ratings.drop(columns=['timestamp'])
df = pd.merge(ratings, movies[['movieId', 'title']], on='movieId', how='left')
df['title'] = df['title'].str.replace(r'\(\d{4}\)', '').str.strip()
matriz = df.pivot_table(values='rating', index='userId', columns='title', fill_value=0)
X = matriz.T

# Aplicar SVD
num_sv = 7
SVD = TruncatedSVD(n_components=num_sv, random_state=42)
resultant_matrix = SVD.fit_transform(X)
corrMtx = np.corrcoef(resultant_matrix)

# Función de recomendación
def recommend_movies(movie_title, corr_matrix, movie_names):
    movie_idx = movie_names.index(movie_title)
    corr_recom = corr_matrix[movie_idx]
    recommended_movies = list(movie_names[(corr_recom > 0.98) & (corr_recom < 0.99)])
    return recommended_movies

# Streamlit App
st.title("Sistema de Recomendación de Películas")

# Selección de película
selected_movie = st.selectbox("Selecciona una película:", df['title'].unique())

# Obtener recomendaciones
recommended_movies = recommend_movies(selected_movie, corrMtx, list(matriz.columns))

# Mostrar las recomendaciones
st.header("Películas Recomendadas:")
for movie in recommended_movies:
    st.write(f"- {movie}")

