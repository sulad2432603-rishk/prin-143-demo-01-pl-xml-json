import py_serializable

@py_serializable.serializable_class
class Politician:
  def __init__(self, *, candidate_name: str, position_running_for: str, political_party: str, election_year: str, platform: str) -> None:
    self.candidate_name = candidate_name
    self.position_running_for = position_running_for 
    self.political_party = political_party
    self.election_year = election_year
    self.platform = platform

  @property
  def candidate_name (self) -> str:
    return self.candidate_name
  @property
  def position_running_for(self) -> str:
    return self.position_running_for 
  
  @property
  def political_party(self) -> str:
    return self.political_party
  
  @property
  def election_year(self) -> str:
    return self.election_year
  
  @property
  def platform(self) -> str:
    return self.platform