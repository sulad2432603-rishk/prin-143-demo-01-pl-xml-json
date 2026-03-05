import py_serializable

@py_serializable.serializable_class
class Entertainment:
  def __init__(self, *, movie_id: str, movie_title: str, genre: str, language: str, release_year: str) -> None:
    self._movie_id = movie_id
    self._movie_title = movie_title 
    self._genre = genre
    self._language = language
    self._release_year = release_year

  @property
  def movie_id (self) -> str:
    return self._movie_id
  @property
  def movie_title(self) -> str:
    return self._movie_title 
  
  @property
  def genre(self) -> str:
    return self._genre
  
  @property
  def language(self) -> str:
    return self._language
  
  @property
  def release_year(self) -> str:
    return self._release_year