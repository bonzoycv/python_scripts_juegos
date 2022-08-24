# Juego simple de seleccion
import random
import time

def displayIntro():
    print('''Estás en una tierra llena de dragones. Frente a ti,
ves dos cuevas. En una de ellas, el dragón es amistoso
y compartirá su tesoro contigo. El otro dragón
es codicioso y hambriento, y te comerá en cuanto te vea.''') 
print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('¿En qué cueva vas a entrar? (1 o 2)')
        cave = input()
    return cave

def checkCave(chooseCave):
    print('Te acercas a la cueva...')
    time.sleep(2)
    print('Es oscura y tenebrosa')
    time.sleep(2)
    print('Un gran dragón salta delante de ti. Abre sus mandíbulas y...')
    print()
    time.sleep(2)
    
    friendlyCave = random.randint(1, 2)
    
    if chooseCave == str(friendlyCave):
        print('¡El Dragón te regala su tesoro!')
    else:
        print('¡El Dragón te engulle de un solo bocado!')

playAgain = 'si'
while playAgain == 'si' or playAgain == 's':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
        
    print('¿Quieres volver a jugar? (sí o no)')   
    playAgain = input() 
        