import requests
from typing import Optional, List


class OMDBApi:

    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://www.omdbapi.com"

    def _images_path(self, title: str) -> Optional[str]:
        response=requests.get(self.url, {'t':title, 'apikey': self.api_key})
        if response.status_code==200:
            data=response.json()
            if 'Poster' in data:
                return data['Poster']
        return None

    def get_posters(self, titles: List[str]) -> List[str]:
        posters = []
        for title in titles:
            path = self._images_path(title)
            if path:  # If image isn`t exist
                posters.append(path)
            else:
                posters.append('assets/no_poster.jpeg')
        return posters
    

    
    def _imdb_id(self, title: str) -> Optional[str]:
        response=requests.get(self.url, {'t':title, 'apikey': self.api_key})
        if response.status_code==200:
            data=response.json()
            if 'imdbID' in data:
                return data['imdbID']
        return None
    
    def get_id_for_links(self, titles: List[str]) -> List[str]:  
        inmdbid = []
        for title in titles:
            id = self._imdb_id(title)
            if id:  
                inmdbid.append(id)
            else:
                inmdbid.append('404') 
        return inmdbid