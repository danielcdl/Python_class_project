TRADUCOES = {
    'Este código é uma especie de simulação de um jogo para o entendimento de classes.': 'This code is kinda simulation of a real game for classes understanding.',
    
    'O usuário possui um valor de 6000 para usar para comprar ataques, que serão usadas para lutar contra os inimigos.': 'The player has a value of 6000 to buy the attacks, that will be used for fight against the enimies.',

    'Digite o seu nome de heroi/heroina: ': 'Write your hero\'s name: ',

    'Seu nome é': 'Your name is',

    'está correto? [s/n]: ': 'it\'s right? [y/n]: ',

    'digite "s" ou "n"': 'type y or n',

    'Prepare-se!': 'Get ready!',

    'Tipo de inimigo: Boss': 'Enemie type: Boss',

    'Tipo de inimigo: Comum': 'Enemie type: normal',

    'Você está a salvo, por enquanto...': 'You are safe, for now...',

    'Não existem inimigos na área':'There is no enemies',

    'inimigo': 'enemie',

    'Existem': 'There are',

    'Existe': 'There is',

    'inimigos': 'enemies'
}



class Traduzido:

    def __init__(self, idioma):
        self._idioma = idioma

    def imprimir(self, texto):
        print(self.traduzir(texto))
    
    def entrada(self, texto):
        texto_entrada = input(self.traduzir(texto))
        return texto_entrada

    def traduzir(self, texto:str):
        """
        Função que retorna a tradução de frases previamente traduzidas.
        """
    
        if texto in TRADUCOES and self._idioma == 'en-us':
            return TRADUCOES[texto]

        return texto

traduzido = Traduzido('en-us')
traduzir = traduzido.traduzir

print(traduzir('Seu nome é'))