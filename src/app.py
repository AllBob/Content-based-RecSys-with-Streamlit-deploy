import os

import streamlit as st
from dotenv import load_dotenv
import base64

from api.omdb import OMDBApi
from recsys import ContentBaseRecSys

TOP_K = 5
load_dotenv()

API_KEY = os.getenv("API_KEY")
MOVIES = os.getenv("MOVIES")
DISTANCE = os.getenv("DISTANCE")

omdbapi = OMDBApi(API_KEY)


recsys = ContentBaseRecSys(
    movies_dataset_filepath=MOVIES,
    distance_filepath=DISTANCE,
)



main_bg = "assets/popcorn.jpg"
main_bg_ext = "jpg"

st.markdown(
    f"""
     <style>
     .main {{
         background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
         background-repeat: no-repeat;
         background-position: right 50% bottom 100%;
         background-size: contain;
         background-attachment: scroll;
     }}
     </style>
     """,
    unsafe_allow_html=True,
)




st.markdown(
    "<h3 style='text-align: center; color: red;'>Что бы посмотреть?</h3>",
    unsafe_allow_html=True
)
st.write(
    "Сервис анализирует описания и ключевые слова фильмов нашей базы данных и подбирает максимально похожие на фильм-образец. А для более точной подстройки реaлизовано два фильтра :women-with-bunny-ears-partying: ")
selected_movie = st.selectbox(
    "Выбери или введи название фильма, который тебе понравился:",
    recsys.get_title()
)

selected_genre= st.selectbox(
    "Выбери или введи интересующий жанр:",
    recsys.get_genres(), index=None,
   placeholder="не выбрано",
)

selected_year= st.selectbox(
    "Выбери или введи год выпуска фильма. Порекомендуем фильмы этого года и новее:",
    recsys.get_year(), index=None,
   placeholder="не выбрано",
)


if st.button('Подобрать фильм :popcorn:'):
    st.write("Выбранный фильм:", selected_movie)
    poster=omdbapi.get_posters([selected_movie])
    st.image(poster[0], width=150)
    sorted_idx=recsys.filter(selected_genre, selected_year)
    recommended_movie_names = recsys.recommendation(sorted_idx, selected_movie, top_k=TOP_K)
    if len(recommended_movie_names)>=5:
        st.write("Рекомендованные фильмы:")
        recommended_movie_posters = omdbapi.get_posters(recommended_movie_names)
        imdb_id_linker=omdbapi.get_id_for_links(recommended_movie_names)
        movies_col = st.columns(TOP_K)

        for index, col in enumerate(movies_col):
            with col:
                st.image(recommended_movie_posters[index])
                st.write(recommended_movie_names[index])
                st.link_button("Подробнее...", "https://www.imdb.com/title/" + imdb_id_linker[index])
    else:
        st.write("Упс, по таким данным не смогли рассчитать 5 рекомендаций, маловато данных... \nПопробуй изменить фильтры!")