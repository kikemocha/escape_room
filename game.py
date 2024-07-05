import time
# define rooms and items
function_array = ['hablar', 'prueba_swifter', 'hacienda','fisio_bar','taylor_key']

def linebreak():
    print("\n\n")

def hablar(phrase):
    return(phrase)

def fisio_bar():
    print()
    print('Abres la puerta y te teletrasportas al 2 de Mayo de 2009 en el Camp Nou.')
    print('Florentino: "OH, NO, este día nos metieron 6, que horror"')
    time.sleep(7)
    print('\t\t\tMadrid 0 - 0 Barcelona')
    time.sleep(1)
    print('Higuaín 14" \t\tMadrid 1 - 0 Barcelona')
    time.sleep(1)
    print('\t\t\tMadrid 1 - 1 Barcelona\t\tHenry 18"')
    time.sleep(1)
    print('\t\t\tMadrid 1 - 2 Barcelona\t\tPuyol 20"')
    time.sleep(1)
    print('\t\t\tMadrid 1 - 3 Barcelona\t\tMessi 36"')
    time.sleep(1)
    print('Sergio Ramos 56"\tMadrid 2 - 3 Barcelona')
    time.sleep(1)
    print('\t\t\tMadrid 2 - 4 Barcelona\t\tHenry 58"')
    time.sleep(1)
    print('\t\t\tMadrid 2 - 5 Barcelona\t\tMessi 75"')
    time.sleep(1)
    print('\t\t\tMadrid 2 - 6 Barcelona\t\tPiqué 83')
    time.sleep(1)
    return('Vuelves al vestuario triste')

def prueba_swifter():
    linebreak()
    print("Se te acerca una masa furiosa de Swifters y te dicen que tienen una llave, ")
    print("pero que para conseguirla tiene que pasar una prueba")
    print("Swifters: 'Te vamos a decir 3 canciones y tienes que decir cual es de Taylor: '")
    print('Never say Never | Thank you Next | Shake it Off')
    print()
    cancion = input("Que canciones es de Taylor?: ")
    if cancion == 'Shake it Off':
        game_state["llaves_coleccionadas"].append(llave_palco)
        return("Muy bien, eres un verdadero swifter y consigues la llave del palco")
    else:
        print("INCORRECTO")
        print("Las swifter se enfadan tanto contigo que te dejan KO")
        for i in range(10):
            print('Zz Zzz Zzzz Zzzzz')
            time.sleep(1)
    return('Te despiertas!!')

def hacienda():
    game_state["habitacion_actual"] = 'vestuario'
    for i in range(5):
        print('Zz Zzz Zzzz Zzzzz')
        time.sleep(1)
    return ('Aparece un inpector de hacienda y te pide que le enseñes tus cuentas \n Te mareas del susto y apareces en el vestuario aturdido')

def taylor_key():
    print()
    print('Taylor se encuentra en el Backstage y te da las gracias por haberle dado la oportunidad \n de cantar en el Bernabéu')
    print('Te da las gracias y te da de regalo la llave del museo!!')
    print('Has obtenido la llave del museo')
    game_state["llaves_coleccionadas"].append(llave_museo)
    return('Ya casi estás!!!')

def ejecutar_funcion(function_name, args=None):
    if function_name in function_array:
        funcion = globals()[function_name]
        if args is not None:
            return funcion(args)
        else:
            return funcion()
    else:
        return('No se encuentra la función')

yacuzzi = {
    "name": "yacuzzi",
    "type": "furniture",
    "has_phrase" : True,
    "function" : 'hablar',
    'func_args' : 'Te caes y te mojas'
}

campo  = {
    "name": "campo",
    "type": "room",
}

puerta_al_campo = {
    "name": "puerta campo_vestuario",
    "type": "door",
}

oeste= {
    "name": "O",
    "type": "object",
    "has_phrase" : True,
    "function" : 'prueba_swifter'
}

este = {
    "name": "puerta campo_backstage",
    "type": "door",
}

sur = {
    "name": "puerta campo_palco",
    "type": "door",
}
norte = {
    "name": "N",
    "type": "object",
    "has_phrase" : True,
    "function" : 'hablar',
    'func_args' : 'El Norte está bloqueado por swifters'
}


llave_campo = {
    "name": "llave del campo",
    "type": "key",
    "target": "puerta campo_vestuario",
}


botiquin = {
    "name": "botiquin",
    "type": "object",
}

vestuario = {
    "name": "vestuario",
    "type": "room",
}

museo = {
  "name": "museo",
  "type": "room"
}

puerta_museo = {
    'name': 'puerta museo',
    'type' : 'door',
}

palco_presidencial = {
    "name": "palco presidencial",
    "type": "room",
}

fisio = {
    "name": "fisio",
    "type": "room",
    "has_phrase" : True,
    "function" : 'fisio_bar',
}

backstage= {
    "name": "backstage",
    "type": "room",
}

inspector_de_hacienda= {
    "name": "inspector de hacienda",
    "type": "object",
    "has_phrase" : True,
    "function" : 'hacienda'
}

llave_palco= {
    "name": "llave del palco",
    "type": "object",
    "target": "puerta campo_palco",
}

taylor= {
    "name": "Taylor Swift",
    "type": "object",
    "has_phrase" : True,
    "function" : 'taylor_key'
}

llave_museo= {
    "name": "llave de museo",
    "type": "object",
    "target": "puerta museo",
}


llave_este = {
    'name': 'llave este',
    'type': 'key',
    'target': 'puerta campo_backstage'
}

all_rooms = [vestuario, campo, palco_presidencial, fisio, backstage, museo]

all_doors = [puerta_al_campo, sur, este, oeste, norte,puerta_museo]
# define which items/rooms are related

object_relations = {
    "vestuario": [botiquin, yacuzzi, puerta_al_campo, fisio],
    "botiquin": [llave_campo],
    "puerta campo_backstage": [backstage, campo],
    'backstage' : [este, taylor],
    "campo": [puerta_al_campo, norte, sur, este, oeste],
    "puerta campo_vestuario": [vestuario, campo],
    "puerta campo_palco": [campo, palco_presidencial],
    "puerta museo" : [palco_presidencial, museo],
    'palco presidencial': [puerta_museo, sur]
}

# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "habitacion_actual": vestuario,
    "llaves_coleccionadas": [llave_este],
    "habitacion_final": museo,
}



def start_game():
    linebreak()
    print("Eres florentino Pérez y te ha llegado un soplo. Tu nieta fanatica de taylor swift \nha descubierto que los ultras del barsa van al concierto de taylor como excusa para robar \nla champions numero 15. Vas a hablar con Laporta para evitarlo y te deja ko de un puñetazo, \nte despiertas aturdido en el vestuario. Tu mision es salvar la 15. ")
    play_room(game_state["habitacion_actual"])


def play_room(room):
    game_state["habitacion_actual"] = room
    if(game_state["habitacion_actual"] == game_state["habitacion_final"]):
        linebreak()
        print("Felicidades! Has logrado salvar la historia del Real Madrid")
    else:
        linebreak()
        print("Estas en el " + room["name"]) #mirar pq room da problemas. Solucion: cambiar room[name] por el nombre del cuarto ya que es el principio del juego.
        intended_action = input("¿Que quieres hacer? Escribe 'explorar' o 'examinar' para continuar --> ").strip()
        linebreak()
        if intended_action == "explorar":
            explore_room(room)
            play_room(room)
        elif intended_action == "examinar":
            examine_item(input("Que quieres examinar? --> ").strip())
        else:
            print("No entiendo. Escribe 'explorar' o 'examinar' para continuar")
            play_room(room)
        linebreak()

def explore_room(room):
    items = [i["name"] for i in object_relations[room["name"]]]
    print("Exploras la habitacion. Estas en " + room["name"] + ".\nHas encontrado: ")
    for i in items:
        print(f"\t - \t {i}")
    linebreak()

def get_next_room_of_door(door, current_room):
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def examine_item(item_name):
    current_room = game_state["habitacion_actual"]
    next_room = ""
    output = None

    # Preguntamos todos los objetos que hay en la habitación actual
    for item in object_relations[current_room["name"]]:
        # Recorre todos los items de la habitación y si el objeto se encuentra en la habitación entra al bucle
        if(item["name"] == item_name):
            output = "Has examinado " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                # Si el item es una puerta, pregunta por todas las llaves y si el target de la puerta
                for key in game_state["llaves_coleccionadas"]:
                    if(key["target"] == item['name']):
                        have_key = True
                if(have_key):
                   # Si tengo la llave le pregunto a la función cual es la habitación que está en el otro lado
                    output += "Has desbloqueado la puerta con la llave."
                    linebreak()
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "La puerta está cerrada y no tienes la llave."
                    linebreak()
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                  # Quitas el objeto de object_relations y te lo guarda en el inventario ['keys collected']
                    item_found = object_relations[item["name"]].pop()
                    game_state["llaves_coleccionadas"].append(item_found)
                    output += "Has encontrado " + item_found["name"] + "."
                    linebreak()
                elif(item['has_phrase']):
                    try:
                        if item['func_args']:
                            output += ejecutar_funcion(item['function'],item['func_args'])
                    except:
                        output += ejecutar_funcion(item['function'])
                else:
                    output += "No hay nada interesante aquí."

                    linebreak()
            # Si encuentras el objeto y tiene alguna funcionalidad o no imprime el output que ha sido modificado en los ifs anteriores
            print(output)
            break

    if(output is None):
        print("Ese objeto no se encuentra en la habitación.")

    if(next_room and input("¿Quieres ir a la siguiente habitación? Escribe 'yes' o 'no' --> ").strip() == 'yes'):
        play_room(next_room)
    else:
        play_room(current_room)

game_state = INIT_GAME_STATE.copy()

start_game()