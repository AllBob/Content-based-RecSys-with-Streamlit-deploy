from typing import List, Set, Optional

import pandas as pd
from .utils import parse


class ContentBaseRecSys:

    def __init__(self, movies_dataset_filepath: str, distance_filepath: str):
        self.distance = pd.read_csv(distance_filepath, index_col='movie_id')
        self.distance.index = self.distance.index.astype(int)
        self.distance.columns = self.distance.columns.astype(int)
        self._init_movies(movies_dataset_filepath)

    def _init_movies(self, movies_dataset_filepath) -> None:
        self.movies = pd.read_csv(movies_dataset_filepath, index_col='id')
        self.movies.index = self.movies.index.astype(int)
        self.movies['genres'] = self.movies['genres'].apply(parse)

    def get_title(self) -> List[str]:
        return self.movies['title'].values

    
    def get_genres(self) -> Set[str]:
        genres = [item for sublist in self.movies['genres'].values.tolist() for item in sublist]
        return set(genres)

    
    def get_year(self) -> List[str]:
        return sorted(self.movies['year'].drop(self.movies[self.movies['year']=='нет данных о годе'].index).unique(), reverse=True)
    
    def filter(self, genres: Optional[str] = None, year: Optional[str] = None) -> List[int]:
        moviesfiltred=self.movies.copy()
        if year is not None:
            moviesfiltred.drop(moviesfiltred[moviesfiltred['year'] == 'нет данных о годе'].index, inplace=True)
            moviesfiltred=moviesfiltred[moviesfiltred['year'].astype(int)>=int(year)]
        if genres is not None:
            moviesfiltred=moviesfiltred[moviesfiltred['genres'].astype(str).str.contains(genres)]
        return  moviesfiltred.index.tolist()
         
    def recommendation(self, filtred_indexes: List[int], title: str, top_k: int = 5) -> List[str]:
        """Returns the names of the top_k most similar movies with the movie title"""
        idx = self.movies[self.movies['title'] == title].index[0]
        if idx not in  filtred_indexes:
            filtred_indexes.append(idx)
        distancefiltred=self.distance.copy()
        distancefiltred=distancefiltred.loc[filtred_indexes, filtred_indexes]
        sim_scores = list(enumerate(distancefiltred.loc[idx]))
        sim_scores = list(filter(lambda x: x[1] > 0 and x[1] < 1, sim_scores))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:top_k + 1]
        movie_indices = [i[0] for i in sim_scores]
        return self.movies['title'].iloc[movie_indices].tolist()
    

    