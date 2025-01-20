import streamlit as st
import pickle
import pandas as pd
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])


    recommended_movies = []
    for i in movies_list [1:6]:
        recommended_movies.append(movies.iloc[i[0]]['title'])
    return recommended_movies


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox('Select a movie:', movies['title'].values)
recommended_movies = recommend(selected_movie_name)
if st.button('Recommend'):
    st.write(recommended_movies)

