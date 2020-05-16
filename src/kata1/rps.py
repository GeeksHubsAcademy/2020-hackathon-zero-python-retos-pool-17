from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    # inputs => player, ai. then formatted
    player = player.lower().capitalize()
    if player == ai:
        return 'Empate!'
    elif player == 'Piedra':
        if ai == 'Papel':
            return 'Perdiste!'
        else:
            return 'Ganaste!'
    elif player == 'Papel':
        if ai == 'Tijeras':
            return 'Perdiste!'
        else:
            return 'Ganaste!'
    elif player == 'Tijeras':
        if ai == 'Piedra':
            return 'Perdiste!'
        else:
            return 'Ganaste!'

# Entry Point
def Game():
    #
    #
    player = input("Elije entre piedra, papel, tijera: ")
    ai = options[randint(0,2)]
    #
    #
    winner = quienGana(player, ai)

    print(winner)
