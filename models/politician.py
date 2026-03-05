import py_serializable

@py_serializable.serializable_class
class Politician:
  def __init__(self, *, candidate_name: str, position_running_for: str, political_party: str, election_year: str, platform: str) -> None:
    self._candidate_name = candidate_name
    self._position_running_for = position_running_for 
    self._political_party = political_party
    self._election_year = election_year
    self._platform = platform

  @property
  def candidate_name (self) -> str:
    return self._candidate_name
  @property
  def position_running_for(self) -> str:
    return self._position_running_for 
  
  @property
  def political_party(self) -> str:
    return self._political_party
  
  @property
  def election_year(self) -> str:
    return self._election_year
  
  @property
  def platform(self) -> str:
    return self._platform