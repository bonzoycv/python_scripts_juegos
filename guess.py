# Este es un juego basico de adivinar el numero
import random

guessesTaken = 0 

print('Como te llamas?')
myName = input()

number = random.randint(1, 20)
print('Hola, ' + myName + ', estoy pensando en un numero del 1 al 20.')

for guessesTaken in range(5):
        print('Adivina el numero')
        guess = input()
        guess = int(guess)
        
        if guess < number: 
            print('Tu numero es muy bajo')
            
        if guess > number:
            print('Tu numero es muy alto')
            
        if guess == number:
            break
        
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Bien hecho, ' + myName + '! Adivinaste el numero en ' + guessesTaken + ' intentos!')
    
if guess != number:
    number = str(number)
    print('Nop. El numero era ' + number + '.')                                    
            