# RecSys

## Objectives
This project implements a content-based recommendation system based on the [Streamlit](https://streamlit.io/) framework, using the OMDB API.

## Data
The following data was used in the project:
* [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* [OMDb API](https://www.omdbapi.com/)

## To run:

* pip install -r requirements.txt
* create a .env file in the scr directory with the following contents:
    API_KEY= <your API key> https://www.omdbapi.com/
    MOVIES = 'assets/movies.csv'
    DISTANCE = 'assets/distance.csv'
* run data processing /src/notebooks/distances.ipynb
* streamlit run app.py



The project was completed at School21.