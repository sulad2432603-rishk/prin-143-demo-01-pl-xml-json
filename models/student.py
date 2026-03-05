import py_serializable

@py_serializable.serializable_class
class Student:
  def __init__(self, *, firstName: str, lastName: str, address: str, reason: str, expectation: str) -> None:
    self._firstName = firstName
    self._lastName = lastName
    self._address = address
    self._reason = reason
    self._expectation = expectation

  @property
  def firstName(self) -> str:
    return self._firstName
  
  @property
  def lastName(self) -> str:
    return self._lastName
  
  @property
  def address(self) -> str:
    return self._address
  
  @property
  def reason(self) -> str:
    return self._reason
  
  @property
  def expectation(self) -> str:
    return self._expectation