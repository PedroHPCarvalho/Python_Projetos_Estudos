from class_CarroCad import CarroCadastrado

def criar_carros():
    carros = []

    modelos = ["Argo", "Onix", "HB20", "Gol", "Civic", "Corolla", "Ka", "Polo", "Fusion", "Fit"]
    quilometragens = [29000, 35000, 41000, 18000, 23000, 50000, 32000, 15000, 27000, 39000]
    anos = [2021, 2020, 2022, 2019, 2018, 2020, 2021, 2017, 2022, 2019]

    for i in range(10):
        carro = CarroCadastrado(modelo=modelos[i], quilometragem=quilometragens[i], ano=anos[i])
        carros.append(carro)

    return carros