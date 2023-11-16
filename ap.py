import pandas as pd
import streamlit as st
from sklearn.decomposition import TruncatedSVD
import numpy as np

# Cargar datos
movies = pd.read_csv("datos/movies.csv")
ratings = pd.read_csv("datos/ratings.csv")
ratings = ratings.drop(columns=['timestamp'])

# Realizar un "join" entre los conjuntos de datos en la columna 'movieId'
df = pd.merge(ratings, movies[['movieId', 'title']], on='movieId', how='left')

# Eliminar los años de la columna 'title'
df['title'] = df['title'].str.replace(r'\(\d{4}\)', '').str.strip()

# Crear matriz
matriz = df.pivot_table(values='rating', index='userId', columns='title', fill_value=0)

# Transponer la matriz
X = matriz.T

# Aplicar SVD
num_sv = 7
SVD = TruncatedSVD(n_components=num_sv, random_state=42)
resultant_matrix = SVD.fit_transform(X)

# Calcular la matriz de correlación de Pearson
corrMtx = np.corrcoef(resultant_matrix)

# Crear la aplicación de Streamlit
st.title("Sistema de Recomendación de Películas")

# Selección de película
liked = st.selectbox("Selecciona una película que te guste:", matriz.columns)

# Obtener recomendaciones
id_liked = list(matriz.columns).index(liked)
corr_recom = corrMtx[id_liked]

# Filtrar recomendaciones basadas en correlación
recommended_movies = list(matriz.columns[(corr_recom > 0.98) & (corr_recom < 0.99)])

# Mostrar recomendaciones
st.subheader("Películas Recomendadas:")
if recommended_movies:
    st.write(recommended_movies)
else:
    st.write("Lo siento, no hay recomendaciones disponibles para esta película.")

# Puedes agregar más elementos de la interfaz de usuario según sea necesario

