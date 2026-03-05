import py_serializable

@py_serializable.serializable_class
class Bank:
  def __init__(self, *, bank_name: str, account_id: str, account_name: str, account_status: str, balance: str,  last_transaction: str) -> None:
    self._bank_name = bank_name
    self._account_id = account_id 
    self._account_name = account_name
    self._account_status = account_status
    self._balance = balance
    self._last_transaction = last_transaction

  @property
  def bank_name (self) -> str:
    return self._bank_name
  @property
  def account_id(self) -> str:
    return self._account_id 
  
  @property
  def account_name(self) -> str:
    return self._account_name
  
  @property
  def account_status(self) -> str:
    return self._account_status

  @property
  def balance(self) -> str:
    return self._balance
  
  @property
  def   last_transaction(self) -> str:
    return self._last_transaction