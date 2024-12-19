# Desafio 2: Sistema de Gerenciamento de Carros
# Implemente um sistema para gerenciar uma frota de carros. As classes principais são:

# Carro: com atributos como modelo, ano, quilometragem, e status (disponível ou alugado). Adicione métodos para marcar como alugado e retornado.
# Cliente: com nome, documento e histórico de alugueis.
# Locadora: que mantém a lista de carros disponíveis. Adicione métodos para cadastrar carros, listar os disponíveis, alugar e devolver carros.
# Inclua:

# Validação para que apenas carros disponíveis sejam alugados.
# Um método para calcular o valor do aluguel com base no número de dias.

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

class ClienteCadastrado:
  def __init__(self,*,nome,documento):
    self.nome = nome
    self.documento = documento

  def retornar_nome(self):
    return self.nome
  
  def retornar_documento(self):
    return self.documento
  
class LocadoraVeiculos:
  def __init__(self):
    self.lista_carros=[] 
    
  def adicionar_carros(self,obj_carro):
    self.lista_carros.append(obj_carro)

  def listar_catalogo(self):
    print("Catalogo Atual")
    print()
    for indice,carro in enumerate(self.lista_carros):
      print(f"{indice} : {carro}")

  def alugar_carro(self):
    self.listar_catalogo()
    indice_selecionado = int(input(f"Informe o numero do carro escolhido: \n"))
    carro_selecionado = self.lista_carros[indice_selecionado]
    carro_selecionado.alugarCarro()
    print(f"O Seguinte carro foi Alugado \nModelo: {carro_selecionado.modelo} \nAno: {carro_selecionado.ano}")
     
def criar_carros():
    carros = []

    modelos = ["Argo", "Onix", "HB20", "Gol", "Civic", "Corolla", "Ka", "Polo", "Fusion", "Fit"]
    quilometragens = [29000, 35000, 41000, 18000, 23000, 50000, 32000, 15000, 27000, 39000]
    anos = [2021, 2020, 2022, 2019, 2018, 2020, 2021, 2017, 2022, 2019]

    for i in range(10):
        carro = CarroCadastrado(modelo=modelos[i], quilometragem=quilometragens[i], ano=anos[i])
        carros.append(carro)

    return carros

lc = LocadoraVeiculos()
lista_base = criar_carros()
for carro in lista_base:
  lc.adicionar_carros(carro)

lc.alugar_carro()


