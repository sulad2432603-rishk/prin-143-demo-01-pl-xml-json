import py_serializable

@py_serializable.serializable_class
class Management:
  def __init__(self, *, student_id: str, student_name: str, course: str, section: str, year_level: str) -> None:
    self.student_id = student_id
    self.student_name = student_name 
    self.course = course
    self.section = section
    self.year_level = year_level

  @property
  def student_id (self) -> str:
    return self.student_id
  @property
  def student_name(self) -> str:
    return self.student_name 
  
  @property
  def course(self) -> str:
    return self.course
  
  @property
  def section(self) -> str:
    return self.section
  
  @property
  def year_level(self) -> str:
    return self.year_level