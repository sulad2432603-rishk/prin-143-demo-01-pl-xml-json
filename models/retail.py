import py_serializable

@py_serializable.serializable_class
class Retail:
  def __init__(self, *, product_id: str, product_category: str, coffee_flavor: str, price: str, size: str) -> None:
    self._product_id = product_id
    self._product_category = product_category 
    self._coffee_flavor = coffee_flavor
    self._price = price
    self._size = size

  @property
  def product_id (self) -> str:
    return self._product_id
  @property
  def product_category(self) -> str:
    return self._product_category 
  
  @property
  def coffee_flavor(self) -> str:
    return self._coffee_flavor
  
  @property
  def price(self) -> str:
    return self._price
  
  @property
  def size(self) -> str:
    return self._size