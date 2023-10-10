import random  # Importa el módulo random para generar selecciones aleatorias.

def choose_options():
  
  options = ('piedra', 'papel', 'tijera')  # Define las opciones del juego en una tupla.
  user_option = input('piedra, papel o tijera => ')  # Solicita al usuario que ingrese su elección.
  user_option = user_option.lower()  # Convierte la entrada del usuario a minúsculas para hacerla no sensible a mayúsculas/minúsculas.

  if not user_option in options: 
    print('esa opcion no es valida')  # Si la opción del usuario no está en las opciones válidas, muestra un mensaje de error.
    return None, None  # Devuelve None para indicar que la elección no es válida.

  computer_option = random.choice(options)  # Genera una elección aleatoria para la computadora.

  print('User option =>', user_option)  # Muestra la opción del usuario.
  print('Computer option =>', computer_option)  # Muestra la opción de la computadora.
  return user_option, computer_option  # Devuelve las elecciones del usuario y la computadora.

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate!')  # Si ambas elecciones son iguales, es un empate.
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gano!')
      user_wins += 1  # Si el usuario elige piedra y la computadora elige tijera, el usuario gana.
    else:
      print('Papel gana a piedra')
      print('computer gano!')
      computer_wins += 1  # Si la computadora elige papel, gana la computadora.
  # (Las siguientes condiciones siguen un patrón similar para las otras combinaciones de opciones)

  return user_wins, computer_wins  # Devuelve las puntuaciones actualizadas del usuario y la computadora.

def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1  # Inicializa las puntuaciones y el número de rondas.

  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    rounds += 1  # Incrementa el número de rondas en cada iteración.

    user_option, computer_option = choose_options()  # Obtiene las elecciones del usuario y la computadora.
    user_wins, computer_wins = check_rules(user_option, computer_option,         
                               user_wins, computer_wins)  # Comprueba quién gana la ronda y actualiza las puntuaciones.

    if computer_wins == 2:
      print('El ganador es la computadora')  # Si la computadora gana 2 rondas, muestra un mensaje de que la computadora es el ganador.
      break

    if user_wins == 2:
      print('El ganador es el usuario')  # Si el usuario gana 2 rondas, muestra un mensaje de que el usuario es el ganador.
      break

run_game()  # Inicia el juego llamando a la función `run_game()`.
