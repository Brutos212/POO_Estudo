import os
from time import sleep
from random import randint, sample

"""
Iniciamos nossa classe com o uso da palavra class, é uma convenção nomear uma classe,
com a incial em maiscula. O metodo __init__ é chamado sempre que um objeto e criado
e nesse caso o nome é um parametro obrigatorio para a criação do Objeto
As demias propriedade já são-determinadas.
"""


class Guerreiro:
    def __init__(self, nome):
        self.nome = nome
        self.forca = randint(5, 10)
        self.defesa = randint(3, 7)
        self.vida = 10
        self.mana = 3


"""
O método, __str__ é usado para determinar como deve se aparecer o objeto quando for impresso,
como print(Objeto), por exemplo.
"""


def __str__(self):
    return f'{self.nome:< 8} | Força: {str(self.forca):< 3} | Defesa: {str(self.defesa):< 3}' \
           f' | Vida: {str(self.vida):< 3} | Mana: {str(self.mana):< 3}'

"""
O método atacar recebe como parêmetro 'outro', que se refere a outro objeto da mesma classe e que será nosso defensor.
É realizada uma verificação de que nosso atacante possui força superior a defesa do outro, 
então calculamos a forca_do_ataque baseada na diferença dessas duas propriedades.

"""
def atacar(self, outro):
    if self.forca > outro.defesa:
        forca_do_ataque = self.forca - outro.defesa
        outro.vida -= forca_do_ataque
        print(f'\n{self.nome} causa {forca_do_ataque} de danos em {outro.nome}\n')

    else:
        print(f'\n{self.nome} não tem força suficiente para atacar {outro.nome}\n')

"""
Da mesma forma que o método 'atacar' o método usar_magia_ataque também 'outro' como parámentro.
È verificado se o atacante tem mana suficiente e então o valor de poder_da_magia é calculado aleatoriamente.
Da vuda do defensor é subtraindo esse valor. Caso o atacante não tenha mana, o ataque falha.
"""

def usar_magia_ataque(self, outro):
    if self.mana >=1:
        poder_da_magia = randint(1, 5)
        outro.vida -= poder_da_magia
        self.mana -= 1
        print(f'\n{self.nome} causa {poder_da_magia} de danos usando magia em {outro.nome}\n')

    else:
        print(f'\n{self.nome} tenta usar magia em {outro.nome}, mas falha\n')

"""
Esse método verifica se o atacante tem man suficiente e recupera uma quantidade de vida calculada
eleatoriamente.
"""

def usar_magia_saude(self):
    if self.mana >=1:
        vida_recuperada = randint(1,5)
        self.vida += vida_recuperada
        self.mana -= 1
        print(f'\n{self.nome} recupera {vida_recuperada}, pontos de vida\n')

    else:
        print(f'\n{self.nome} tenta usar magia para recuperar a saúde, mas falha\n')

"""
já fora da classe, criamos 3 instâncias da classe Guerreiro, passando como paramentro o nome de cada um
"""
guerreiro1 = Guerreiro('Gandalf')
guerreiro2 = Guerreiro('Aragon')
guerreiro3 = Guerreiro('Legolas')

""" Adicione os guerreiros criados em uma lista """

guerreiros = [guerreiro1, guerreiro2, guerreiro3]

"""
Aqui própriamente dito é onde acontece nossa batalha, seguindo o seguinte esquema:
1 É verificado o tamanho da lista guerreiros. se for maior que 1:
    
    a. Limpamos a tela do console unsando a função os.system('clear') - Linux - ou os.system('cls') - Windows.
    
    b. Imprimimos cada guerreiro da lista (o resultado desse print é o que definimos em __str__)
    
    c. Usamos a função sample, para selecionar dois elementos da lista que não sejam repetidos e atribuimos
                o primeiro elemento ao atacante e o segundo ao defensor
                
    d. Sorteamos um número entre 0 e 9 para definir qual tipo de movimento o atacante vai realizar
     -Se for menor que 5, o atacante usa o método atacar, recebendo o defensor como parâmentro
     -Se for igual e 5 ou menor que 8, o atacante usa o método usar_magia_ataque recebendo o defensor como parãmetro
     -Se for maior que 8, o atacante usa o método usar_magia_saude não precisando receber nada como parâmentro
     
    e. Verificando em cada elemento da lista se este possui vida > caso contrário ele é removido
    
    f. Usamos sleep(1) para dar um intervali de tempo entre um ataque e outro.

2. Caso a lista possua somente um elemento, é sinal de que a batalha terminou e há um vencedor.
    O loop while é encerrado com o uso do break
"""

while True:
    """(1)"""
    if len(guerreiros) >=1:
        """(a)"""
        try:
            os.system('clear')
        except:
            os.system('cls')

        """(b)"""
        [print(g) for g in guerreiros]

        """(c)"""
        atacante, defensor = sample(guerreiros,2)

        """(d)"""
        tipo_de_movimento = randint(0, 10)

        if tipo_de_movimento < 5:
            atacante.atacar(defensor)

        elif tipo_de_movimento < 8:
            atacante.usar_magia_ataque(defensor)

        else:
            atacante.usar_magia_saude()
        """(e)"""
        for g in guerreiros:
            if g.vida <=0:
                print(f'\n{g.nome} está morto\n')
                del guerreiros[guerreiros.index(g)]

        """(f)"""
        sleep(1)

        """(2)"""

    else:
        print(f'\n\nApós uma dura batalha, {guerreiros[0].nome} foi o vencedor!\n\n')

        break

    """Esse input é apenas para o terminal não fechar após o break """

    input('Tecla ENTER para finalizar...')
