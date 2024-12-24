
class Relatorio():
  def __init__(self,):
    pass

  def relatorio_gerar(self):
    try:
      arquivo = open("C/\Users/pedro/Documents/Python Scripts/Python_Projetos_Estudos/Relatorios/relatorio.txt","w")
      arquivo.write("Teste")
    except IOError as exc:
      print(f"o seguinte erro ocorreu : {exc}")

    