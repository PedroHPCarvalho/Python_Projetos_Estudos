class CarroCadastrado:
  def __init__(self,/,status_disponivel=True,*,modelo,ano,quilometragem):
    self.modelo = modelo
    self.ano = ano
    self.quilometragem = quilometragem
    self.status_disponivel = status_disponivel

  def __str__(self):
    return f"Carro Cadastrado: {self.modelo} ({self.ano}) - {'Disponivel' if self.status_disponivel else 'Alugado'}"
  
  def __repr__(self):
    return self.__str__()
    
  def alugarCarro(self):
    self.status_disponivel = False

  def retornarCarro(self):
    self.status_disponivel = True

  def retornar_status(self):
    return self.status_disponivel
