import streamlit as st
import pandas as pd
import pickle
import requests


with open('movie_data.pkl','rb') as file:
    movies,cosine_sim = pickle.load(file)



def get_recommendations(title,cosine_sim=cosine_sim):
    idx = movies[movies['title']==title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores,key=lambda x:x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return movies [['title','movie_id']].iloc[movie_indices]
    


def fetch_poster(movie_id):
    import requests

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US"
    response = requests.get(url)
    data = response.json()

    # Check if poster_path exists
    if 'poster_path' in data and data['poster_path'] is not None:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        # Provide a default image if not found
        return "https://via.placeholder.com/500x750?text=No+Image+Available"




st.title('Movie Recommender System')

selected_movie = st.selectbox('Select a movie:',movies['title'].values)


if st.button('Show Recommendations'):
    recommendations = get_recommendations(selected_movie)
    st.write('Top 10 movie recommendations:')


    #Create a 2 row by 5 grid layout

    for i in range(0,10,5):
        cols = st.columns(5)
        for cols, j in zip(cols, range(i,i+5)):
            movie_title = recommendations.iloc[j]['title']
            movie_id = recommendations.iloc[j]['movie_id']
            poster_url = fetch_poster(movie_id)
            with cols:
                st.image(poster_url,width=150)
                st.write(movie_title)