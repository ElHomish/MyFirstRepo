import random
import os

def run():
    #Definir los estados del ahorcado
    IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    #Definir una base de datos de nombres

    DB = [
        "C",
        "PYTHON",
        "JAVASCRIPT",
        "PHP"
    ]

#Voy a decir una palabra aleatoria que va a adivinar el usuario.
    word = random.choice(DB) 
#Voy a crear una lista llamada 'spaces'
    spaces = ["_"] * len(word)
#Crear una serie de intentos
    attempt = 6

#Empezar a hacer el juego
while True:
     #Lo primero que se hace es limpiar la pantalla
     os.system("cls")
     #Mostrar los guiones bajos que se tenia preparado ahi
     for character in spaces:
        print(character, end=" ") #Terminar el print con un espacio, para que cuando se haga el print no haya salto de linea 
     print(IMAGES[attemps])
     #Preguntarle al usuario sobre su elección
     letter = input("Elige una letra").upper()

     found = False
     for idx, character in enumerate(word):
        if character == letter:
            spaces[idx] = letter
            found = True
     if not found:
        attemps =- 1
     
     if "_" not in spaces:
        os.system("cls")
        print("Ganaste")
        break
        input()

     if attemps == 0:
        os.system("cls")
        print("Perdiste")
        break
        input()  

    
    

if __name__ == '__main__':
    run()   
    #Ejecutar la función y empezar a hacer el juego