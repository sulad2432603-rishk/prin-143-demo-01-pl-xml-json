import py_serializable

@py_serializable.serializable_class
class Entertainment:
  def __init__(self, *, movie_id: str, movie_title: str, genre: str, language: str, release_year: str) -> None:
    self.movie_id = movie_id
    self.movie_title = movie_title 
    self.genre = genre
    self.language = language
    self.release_year = release_year

  @property
  def movie_id (self) -> str:
    return self.movie_id
  @property
  def movie_title(self) -> str:
    return self.movie_title 
  
  @property
  def genre(self) -> str:
    return self.genre
  
  @property
  def language(self) -> str:
    return self.language
  
  @property
  def release_year(self) -> str:
    return self.release_year