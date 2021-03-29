#pt Este programa é um estudo sobre classes e tem um exemplo claro e básico de classe
#En This program is a study of classes and it has an example simple and easy of class

from random import randint
from time import sleep

from Enimie import numero_i, Ataque_personagem
from traducao import Traduzido


class Heroi:

    def __init__(self, nome):
        self.nome = nome
        self.vivo = True
        self.vida = 300
        self.dinheiro_ataque = 6000

    

class Inimigo:
    vivo = True
    vida = 300

class Boss:
    vivo = True
    vida = 1000

lista = ((90,200,30,20),('Espada', 'Lança', 'Pedra', 'Soco'),(800, 1200, 500, 250))

inimigo1 = Inimigo()
inimigo2 = Inimigo()
inimigo2.vida = 500
boss = Boss()
listae = (inimigo1.vida, inimigo2.vida, boss.vida)

print('Escolha seu idioma / Choose your language')
while True:    
    idioma = input('ENGLISH[1]/PORTUGUÊS[2]:')

    if idioma == '1':
        traduzido = Traduzido('en-us')
        break
    elif idioma == '2':
        traduzido = Traduzido('pt-br')
        break
    else:
        print('escolha inválida / invalid choice')
    
entrada = traduzido.entrada
imprimir = traduzido.imprimir
traduzir = traduzido.traduzir

imprimir('Este código é uma especie de simulação de um jogo para o entendimento de classes.')
imprimir('O usuário possui um valor de 6000 para usar para comprar ataques, que serão usadas para lutar contra os inimigos.')

while True:
    nome = traduzido.entrada('Digite o seu nome de heroi/heroina: ')
    while True:
        print(f'{traduzir("Seu nome é")} {nome}, {traduzir("está correto? [s/n]: ")}', end=' ')
        correto = input().lower()
        if correto in 'sny':
            break
        else:
            imprimir('Digite "s" ou "n"')
    if correto in 'sy':
        break

tate_no_yusha = Heroi(nome)
while tate_no_yusha.vivo:
    numero_inim = numero_i()

    if numero_inim == 0:
        imprimir('Não existem inimigos na área')
        sleep(2)
        imprimir('Você está a salvo, por enquanto...')
        sleep(2)
    else:
        print(f'{traduzir("Existe")} {numero_inim} {traduzir("inimigo")}' if numero_inim == 1 else f'{traduzir("Existem")} {numero_inim} {traduzir("inimigos")}')
        if numero_inim == 1:
            eescolha = 0
            eescolha = randint(0,2)
            if eescolha == 2:
                imprimir('Tipo de inimigo: Boss')
                imprimir('Prepare-se!')
                Ataque_personagem(tate_no_yusha.vida, listae[eescolha], 6000, lista)
                break
            else:
                imprimir('Tipo de inimigo: Comum')
                Ataque_personagem(tate_no_yusha.vida, listae[eescolha], 6000, lista)
                break
        else:
            print('='*10)
            print('2 inimigos')
            print('Em desenvolvimento...')
            print('='*10)
               
                


        
        
    

