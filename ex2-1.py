from enum import Enum
from datetime import datetime

class Pessoa(object):

  class GENERO(Enum):          # inner class / classe filha de 'Enum'
    INDEFINIDO = 0             # variável de classe que simula um valor de enumeração
    HOMEM_CIS = 1
    MULHER_CIS = 2
    NAO_BINARIO = 3
    TRANSGENERO = 4

    def __str__(self):         # ToString de Python (retorna a string correspondente ao gênero)
     return self.name

  def __init__(self, nome='INDEFINIDO', genero=GENERO.INDEFINIDO, nascimento=datetime.today()):
    super(Pessoa, self).__init__()
    self.nascimento = nascimento     # inicializa através de properties
    self.nome = nome                 # inicializa através de properties
    self.genero = genero             # inicializa através de properties

  @property
  def idade(self):
    hoje = datetime.today()
    nascimento = self.__nascimento
    return hoje.year-nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

  @property
  def nome(self):
    return self.__nome

  @property
  def nascimento(self):
    return self.__nascimento

  @property
  def genero(self):
    return self.__genero

  @nome.setter
  def nome(self, nome):
    self.__nome = nome

  @nascimento.setter
  def nascimento(self, nascimento):
    if nascimento <= datetime.today():
      self.__nascimento = nascimento

  @genero.setter
  def genero(self, genero):
    self.__genero = genero

  def __str__(self):
    return f"[Pessoa] Nome: {self.nome} | Nascimento: {self.nascimento.strftime('%d/%m/%Y %H:%M')} | Idade: {self.idade} | Gênero: {self.genero}"
  
def main():
	p1 = Pessoa("Leonardo da Silva", Pessoa.GENERO.HOMEM_CIS, datetime(2020, 11, 21))
	p2 = Pessoa("Ana Clara da Silva", Pessoa.GENERO.MULHER_CIS, datetime(2014, 7, 20))

	# podemos adicionar atributos a uma instância de uma classe em tempo de execução
	# pois em linguagens dinâmicas, classes funcionam similarmente a dicionários/maps/hashmaps
	p1.atributo = "Novo atributo"
	print(p1.atributo) 

    # a variável p2 não tem esse novo atributo, pois essa instância não foi modificada
	print(p2.atributo)

# o comando seguinte eh o que efetivamente inicia o programa
if (__name__ == "__main__"):
      main()