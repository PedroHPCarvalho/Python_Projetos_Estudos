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

  def __str__(self):
    return f"Cliente Cadastrado: {self.nome} Doc: {self.documento}"
  
  def __repr__(self):
    return self.__str__

  def retornar_nome(self):
    return self.nome
  
  def retornar_documento(self):
    return self.documento
  
class LocadoraVeiculos:
  def __init__(self):
    self.lista_carros=[]
    self.lista_clientes=[] 

  def menu(self):
    menu = """ 
  ---------MENU OPÇÕES---------
  0 - LISTAR CATALOGO
  1 - ALUGAR CARRO
  2 - DEVOLVER CARRO
  3 - CADASTRAR CLIENTE
  4 - LISTAR CLIENTES
  -----------------------------
  """
    print(menu)
    try:
      opcao_selecionada = int(input("Digite a opção escolhida:"))
      match opcao_selecionada:
          case 0:
            self.listar_catalogo()
          case 1:
            self.alugar_carro()
          case 2:
            self.devolver_carro()
          case 3:
            self.cadastrar_cliente()
          case 4:
            self.listar_clientes()

    except ValueError:
      print("Numero informado não reconhecido")
      self.menu()

  def adicionar_carros(self,obj_carro):
    self.lista_carros.append(obj_carro)

  def listar_catalogo(self):
    print("Catalogo Atual")
    print()
    for indice,carro in enumerate(self.lista_carros):
      print(f"{indice} : {carro}")
    self.menu()

  def alugar_carro(self):
    try:
      indice_selecionado = int(input(f"Informe o numero do carro escolhido para ALUGAR: \n"))
      carro_selecionado = self.lista_carros[indice_selecionado]
      carro_selecionado.alugarCarro()
      print(f"O Seguinte carro foi Alugado \nModelo: {carro_selecionado.modelo} \nAno: {carro_selecionado.ano}")
      self.menu()
    except ValueError:
      print("Informe o INDICE DO CARRO CORRETAMENTE")
      self.alugar_carro()

  def devolver_carro(self):
    indice_selecionado = int(input(f"Informe o numero do carro escolhido para DEVOLVER: \n"))
    carro_selecionado = self.lista_carros[indice_selecionado]
    carro_selecionado.retornarCarro()
    print(f"O Seguinte carro foi Devolvido \nModelo: {carro_selecionado.modelo} \nAno: {carro_selecionado.ano}")
    self.menu()

  def cadastrar_cliente(self):
    print(f"Cadastrar o cliente, preeencha as informações")
    nome = input("Informe o nome completo: \n")

    def cad_documento():
      documento = int(input("Informe o documento: \n"))
      cliente = ClienteCadastrado(nome=nome,documento=documento)
      self.lista_clientes.append(cliente)
      return documento
    try:
      cad_documento()
      print("Cadastro do documento feito")
      self.menu()
    except ValueError:
      print("documento possui apenas numeros")
      cad_documento()

  def listar_clientes(self):
    print("Clientes Atuais")
    for indice, cliente in enumerate(self.lista_clientes):
      print(f"{indice}: {cliente}")
    self.menu()

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

lc.menu()



