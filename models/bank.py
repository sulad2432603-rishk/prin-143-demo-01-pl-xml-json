import py_serializable

@py_serializable.serializable_class
class Bank:
  def __init__(self, *, bank_name: str, account_id: str, account_name: str, account_status: str, balance: str,  last_transaction: str) -> None:
    self.bank_name = bank_name
    self.account_id = account_id 
    self.account_name = account_name
    self.account_status = account_status
    self.balance = balance
    self.last_transaction = last_transaction

  @property
  def bank_name (self) -> str:
    return self.bank_name
  @property
  def account_id(self) -> str:
    return self.account_id 
  
  @property
  def account_name(self) -> str:
    return self.account_name
  
  @property
  def account_status(self) -> str:
    return self.account_status

  @property
  def balance(self) -> str:
    return self.balance
  
  @property
  def   last_transaction(self) -> str:
    return self.  last_transaction