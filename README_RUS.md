
# RecSys

## Цели
В этом проекте реализуется content- based рекомендательная система на основе фреймворка [Streamlit](https://streamlit.io/) c использованием API OMDB.

## Данные
В проекте использованные данные
* [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
* [OMDb API](https://www.omdbapi.com/)


## Для запуска:

* pip install -r requirements.txt
* в scr создать .env файл с содержимым 
    API_KEY= <ваш API ключ> https://www.omdbapi.com/
    MOVIES = 'assets/movies.csv'
    DISTANCE = 'assets/distance.csv'
* запустить обработку данных /src/notebooks/distances.ipynb
* streamlit run app.py

Проект выполнен в School21

 


