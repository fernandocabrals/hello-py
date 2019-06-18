from distutils.command.config import config
from typing import re

from distro import cached_property


class Carro:
    def __init__(self, modelo, marca, valor):
        self.modelo=modelo
        self.marca=marca
        self.valor=valor

    def exibir_carro(self):
        return '%s - %s - %s' % (self.modelo, self.marca, self.valor)

class Concessionaria:
    def __init__(self, nome, cnpj, estoqueCarros):
        self.nome=nome
        self.cnpf=cnpj
        self.estoqueCarros=estoqueCarros

    def listarEstoque(self):
        for carro in self.estoqueCarros:
            print(carro.exibir_carro())

    def pesquisarCarroPorModelo(self, modelo):
        resultPesq = []
        for carro in self.estoqueCarros:
            if carro.modelo.lower() == modelo.lower():
                resultPesq.append(carro)
        for carro in resultPesq:
            print(carro.exibir_carro())

    def venderCarro(self, carro):
        for carroT in self.estoqueCarros:
            if carroT == carro:
                self.estoqueCarros.remove(carro)



carro1 = Carro('Civic', 'Honda', 60000)
carro2 = Carro('Punto', 'Fiat', 26000)
carro3 = Carro('Corolla', 'Toyota', 78000)

estoque = [carro1, carro2, carro3]

concess1 = Concessionaria("Cabral Seminovos", '312.2132.3123/00001', estoque);
print("Listar Estoque:")
concess1.listarEstoque()
print("\nPesquisando Modelo: Civic")
concess1.pesquisarCarroPorModelo("cIVic")
print("\nCarro vendido: Punto")
concess1.venderCarro(Carro('Punto', 'Fiat', 26000))
print("\nCarro Vendido! - Listar Estoque:")
concess1.listarEstoque()