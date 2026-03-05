import py_serializable

@py_serializable.serializable_class
class Management:
  def __init__(self, *, student_id: str, student_name: str, course: str, section: str, year_level: str) -> None:
    self._student_id = student_id
    self._student_name = student_name 
    self._course = course
    self._section = section
    self._year_level = year_level

  @property
  def student_id (self) -> str:
    return self._student_id
  @property
  def student_name(self) -> str:
    return self._student_name 
  
  @property
  def course(self) -> str:
    return self._course
  
  @property
  def section(self) -> str:
    return self._section
  
  @property
  def year_level(self) -> str:
    return self._year_level