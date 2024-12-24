from datetime import datetime 

class Relatorio():
  def __init__(self,):
    pass

  def relatorio_gerar(self,cliente,modelo):
    mascara_horario = "%d-%m-%Y %H:%M"
    horario_pos_mascara = datetime.strftime(datetime.now(),mascara_horario)
    texto_inserir = f"{horario_pos_mascara}|{cliente}|{modelo}"
    try:
      arquivo = open("C:/Users/pedro/Documents/Python Scripts/Python_Projetos_Estudos/Relatorios/relatorio.txt", "a")
      arquivo.write(texto_inserir)
    except IOError as exc:
      print(f"o seguinte erro ocorreu : {exc}")

    