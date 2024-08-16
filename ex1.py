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

class Aluno(Pessoa):
  class NIVEL(Enum):
    INDEFINIDO = 0
    GRADUACAO = 1
    ESPECIALIZACAO = 2
    MESTRADO = 3
    DOUTORADO = 4

    def __str__(self):
      return self.name

  def __init__(self, nome='Indefinido',
               genero=Pessoa.GENERO.INDEFINIDO,
               nascimento=datetime.today(),
               matricula='Indefinida',
               nivel=NIVEL.INDEFINIDO):
    super(Aluno, self).__init__(nome, genero, nascimento)
    self.__matricula = matricula
    self.__nivel = nivel

  def __str__(self):
    return f"[Aluno] Nome: {self.nome} | Nascimento: {self.nascimento.strftime('%d/%m/%Y %H:%M')} | Idade: {self.idade} | Gênero: {self.genero} | Matrícula: {self.matricula} | Nível: {self.nivel}"

  @property                    # permite que o atributo seja visto do lado de fora, como uma propriedade
  def matricula(self):         # propriedades chamam implicitamente o metodo (como um 'getter')
    return self.__matricula  # veja no main que a propriedade eh acessada como se fosse um atributo normal!

  @matricula.setter
  def matricula(self, matricula):  # define um metodo 'getter' para a propriedade
    self.__matricula = matricula  # poderia ter um codigo de validacao...

  @property
  def nivel(self):
    return self.__nivel

  @nivel.setter
  def nivel(self, nivel):
    self.__nivel = nivel


class Funcionario(Pessoa):
  class CATEGORIA(Enum):
    INDEFINIDO = 0
    PROGRAMADOR = 1
    ANALISTA = 2
    GERENTE = 3

    def __str__(self):
      return self.name

  def __init__(self, nome='Indefinido',
	genero=Pessoa.GENERO.INDEFINIDO,
	nascimento=datetime.today(),
	categoria=CATEGORIA.INDEFINIDO,
    ingresso=datetime.today()
  ):
    super(Funcionario, self).__init__(nome, genero, nascimento)
    self.__categoria = categoria
    self.__ingresso = ingresso

  def __str__(self):
    return f"[Funcionario] Nome: {self.nome} | Nascimento: {self.nascimento.strftime('%d/%m/%Y %H:%M')} | Idade: {self.idade} | Gênero: {self.genero} | Categoria: {self.categoria} | Ingresso: {self.ingresso}"

  @property         
  def categoria(self):    
    return self.__categoria

  @categoria.setter
  def categoria(self, categoria):
    self.__categoria = categoria 

  @property
  def ingresso(self):
    return self.__ingresso

  @ingresso.setter
  def ingresso(self, ingresso):
    self.__ingresso = ingresso


def main():
  l = [
    Aluno(nome="vini"),
    Aluno(nome="arthur"),
    Aluno(nome="eduardo"),
    Pessoa(nome="alex"),
    Pessoa(nome="tom"),
    Pessoa(nome="remi"),
    Pessoa(nome="greg"),
    Funcionario(nome="gabriel"),
    Funcionario(nome="luca"),
    Funcionario(nome="lucca")
  ]

  for p in l:
    print(p)

# o comando seguinte eh o que efetivamente inicia o programa
if (__name__ == "__main__"):
      main()