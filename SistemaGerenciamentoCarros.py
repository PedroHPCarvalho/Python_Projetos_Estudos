# Desafio 2: Sistema de Gerenciamento de Carros
# Implemente um sistema para gerenciar uma frota de carros. As classes principais são:

# Carro: com atributos como modelo, ano, quilometragem, e status (disponível ou alugado). Adicione métodos para marcar como alugado e retornado.
# Cliente: com nome, documento e histórico de alugueis.
# Locadora: que mantém a lista de carros disponíveis. Adicione métodos para cadastrar carros, listar os disponíveis, alugar e devolver carros.
# Inclua:

# Validação para que apenas carros disponíveis sejam alugados.
# Um método para calcular o valor do aluguel com base no número de dias.

from class_ClienteCad import ClienteCadastrado
from class_CarroCad import CarroCadastrado
from funcoes_apoio import criar_carros
from class_relatorio import Relatorio

criar_carros()

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
            self.retornar_menu()
          case 1:
            self.alugar_carro()
          case 2:
            self.devolver_carro()
          case 3:
            self.cadastrar_cliente()
            self.retornar_menu()
          case 4:
            self.listar_clientes()
            self.retornar_menu()
          case _:
            self.menu()

    except ValueError:
      print("Numero informado não reconhecido")
      self.retornar_menu()

  def retornar_menu(self):
    self.menu()

  def adicionar_carros(self,obj_carro):
    self.lista_carros.append(obj_carro)

  def listar_catalogo(self):
    print("Catalogo Atual")
    print()
    for indice,carro in enumerate(self.lista_carros):
      print(f"{indice} : {carro}")

  def alugar_carro(self):
      relat = Relatorio()
      try:
        indice_selecionado_carro = int(input(f"Informe o numero do carro escolhido para ALUGAR: \n"))
        carro_selecionado = self.lista_carros[indice_selecionado_carro]
        self.listar_clientes()
        indice_selecionado_cliente = int(input(f"Informe o indice do cliente"))
        try:
          cliente_selecionado = self.lista_clientes[indice_selecionado_cliente]
        except IndexError:
          print("Cliente não existente ou Não encontrado, cadastre ou consulte os cadastros")
          self.retornar_menu()
        carro_selecionado.alugarCarro()
        print(f"O Seguinte carro foi Alugado \nModelo: {carro_selecionado.modelo} \nAno: {carro_selecionado.ano} \npara o cliente {cliente_selecionado.retornar_nome()}")
        relat.relatorio_gerar(cliente_selecionado.retornar_nome(),carro_selecionado.modelo)
      except ValueError:
        print("Informe o INDICE DO CARRO CORRETAMENTE")
        self.alugar_carro()

      self.retornar_menu()
      
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
    
  


lc = LocadoraVeiculos()
lista_base = criar_carros()
for carro in lista_base:
  lc.adicionar_carros(carro)

lc.menu()




