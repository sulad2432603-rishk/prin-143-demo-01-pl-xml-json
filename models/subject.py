from typing import Iterable, List, Optional
from models.student import Student
import py_serializable

@py_serializable.serializable_class
class Subject:
  def __init__(self, *, code: str, students: Optional[Iterable[Student]] = None) -> None:
    self._code = code
    self._students = list(students or [])

  @property
  def code(self) -> str:
    return self._code
  
  @property
  @py_serializable.xml_array(py_serializable.XmlArraySerializationType.NESTED, 'student')
  def students(self) -> List[Student]:
    return self._students
  
  @students.setter
  def students(self, students: Iterable[Student]) -> None:
    self._students = list(students)