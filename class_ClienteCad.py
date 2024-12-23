class ClienteCadastrado:
  def __init__(self,*,nome,documento):
    self.nome = nome
    self.__documento = documento

  def __str__(self):
    return f"Cliente Cadastrado: {self.nome} Doc: {self.__documento}"
  
  def __repr__(self):
    return self.__str__

  def retornar_nome(self):
    return self.nome
  
  def retornar_documento(self):
    return self.documento