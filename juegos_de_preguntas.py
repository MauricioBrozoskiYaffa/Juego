# Preguntas y respuestas
# Definimos listas con diferentes preguntas y las opciones de respuestas con la correcta indicada
preguntas_nivel_1 = [
    ("¿Cuántos jugadores por equipo pueden estar en la cancha?", "C", ["A) 3", "B) 7", "C) 5", "D) 6"]),
    ("¿Cuántas faltas debe tener un jugador para ser expulsado del juego?", "B", ["A) 4", "B) 5", "C) 6", "D) 8"]),
    ("¿En qué momento se cobra caminata cuando tienes la pelota en mano?", "A", ["A) Cuando el jugador hace 3 pasos sin picar el balón", "B) Cuando el jugador hace 2 pasos sin picar el balón", "C) Cuando el jugador hace 4 pasos sin picar el balón", "D) Cuando el jugador hace 1 paso sin picar el balón"]),
    ("El tiro libre. ¿Cuántos puntos vale?", "A", ["A) Vale 1 punto", "B) Vale 2 puntos", "C) Vale 0 puntos", "D) Cuenta como falta"]),
    ("¿Cuándo se considera un juego de 4 puntos?", "B", ["A) Cuando el jugador mete un doble antes que le cometan falta y tiene un tiro libre", "B) Cuando el jugador mete un triple antes que le cometan falta y tiene un tiro libre", "C) Cuando el jugador mete dos dobles seguidos", "D) Cuando el árbitro cobra una jugada indebida y da al jugador 4 tiros"]),
    ("¿Qué sucede si el jugador pisa la línea que está al borde de la cancha con la pelota en mano?", "B", ["A) El árbitro deja seguir el juego", "B) El árbitro cobra fuera", "C) El árbitro lo considera jugada indebida", "D) El árbitro considera que el jugador debe sacar de ese lugar"]),
    ("¿Qué sucede si el partido termina en empate?", "C", ["A) El juego termina igualado", "B) El equipo que llegó primero al número más alto gana", "C) Se extiende un tiempo más para desempatar", "D) Se hace un sorteo para ver al ganador"]),
    ("¿Cuántos jugadores hay por equipo, contando los suplentes?", "B", ["A) 10 jugadores", "B) 12 jugadores", "C) 8 jugadores", "D) 15 jugadores"]),
    ("¿En qué momento se cobra una falta?", "D", ["A) Cuando un jugador golpea a otro", "B) Cuando un jugador choca a otro", "C) Mientras realiza un tiro, el otro jugador tiene contacto con el lanzador", "D) Todas son correctas"]),
    ("¿Cómo son llamados los puntos anotados por los equipos?", "D", ["A) Doble", "B) Simple", "C) Triple", "D) Todas son correctas"]),
]
#-----------------------
# Definimos otra lista con preguntas más específicas sobre la NBA y las opciones de respuestas con la correcta indicada
preguntas_nivel_2 = [
    ("¿Quién es el jugador con más puntos anotados en la NBA?", "C", ["A) Stephen Curry", "B) Kevin Durant", "C) LeBron James", "D) Luka Dončić"]),
    ("¿A quién apodan el 'Cafetero' en la NBA?", "B", ["A) Tyler Herro", "B) Jimmy Butler", "C) Kevin Love", "D) Devin Booker"]),
    ("¿Qué jugador es el líder histórico en triples en la NBA?", "A", ["A) Stephen Curry", "B) Damian Lillard", "C) Larry Bird", "D) Ray Allen"]),
    ("¿En qué equipo juega actualmente Jayson Tatum?", "D", ["A) Minnesota Timberwolves", "B) Indiana Pacers", "C) Sacramento Kings", "D) Boston Celtics"]),
    ("¿Qué jugador ganó el rookie del año 2023/2024?", "A", ["A) Victor Wembanyama", "B) Scoot Henderson", "C) Chet Holmgren", "D) Brandon Miller"]),
    ("¿Quién es el jugador con más asistencias en la historia de la NBA?", "C", ["A) Jason Kidd", "B) Steve Nash", "C) John Stockton", "D) Chris Paul"]),
    ("¿Quién era conocido como Black Mamba en la NBA?", "C", ["A) Chris Bosh", "B) Udonis Haslem", "C) Kobe Bryant", "D) Kevin Garnett"]),
    ("¿Qué jugadores son hermanos dentro de la NBA?", "D", ["A) Paul y Jokic", "B) Vince y McGrady", "C) Giannis y Russell", "D) Robin y Brook"]),
    ("¿Quién es el jugador con más campeonatos ganados en la historia de la NBA?", "B", ["A) Sam Jones", "B) Bill Russell", "C) Robert Horry", "D) Michael Jordan"]),
    ("¿Quién es el entrenador con más victorias en la historia de la NBA?", "A", ["A) Gregg Popovich", "B) Phil Jackson", "C) Doc Rivers", "D) Pat Riley"]),
]

# Mostramos una pequeña introducción del juego y de qué se trata
print("-----------------------") # Lo utilizamos para crear una línea divisoria
print("¡Hola! Bienvenidos a la Trivia de la NBA 🏀🏀🏀.\n")
print("Vamos a hacer un juego de preguntas y respuestas, para saber cuánto conoces sobre el baloncesto y la NBA. Esto se dividirá en niveles. Se tomará el formato de multiple choice, será una pregunta con 4 opciones, solo una será la correcta. Un total de 10 preguntas por cada nivel con un porcentaje total del 100%. Para subir al siguiente nivel, deberás tener al menos un 70% de respuestas correctas. Una vez alcanzado el puntaje ideal, pondremos a prueba tus conocimientos sobre la NBA.\n")
#-----------------------

# Función para jugar un nivel
def jugar_nivel(preguntas):
    respuestas_correctas = 0 # Inicializamos el contador de respuestas correctas
    respuestas_usuario = []  # Lista para almacenar las respuestas del usuario
    
    # Iteramos sobre cada pregunta del nivel
    for i, (pregunta, respuesta_correcta, opciones) in enumerate(preguntas):
        # Mostramos la pregunta y las opciones de respuesta
        print(f"\nPregunta {i+1}: {pregunta}🏀")
        for opcion in opciones:
            print(opcion)
        
        # Solicitamos la respuesta del usuario
        respuesta = input("Tu respuesta: ").upper()
        respuestas_usuario.append(respuesta) # Almacenamos la respuesta del usuario
        
        # Verificamos si la respuesta es correcta
        if respuesta == respuesta_correcta:
            respuestas_correctas += 1 # Incrementamos el contador de respuestas correctas
    
    return respuestas_correctas, respuestas_usuario # Devolvemos el número de respuestas correctas y las respuestas del usuario
#----------------------
# Función para mostrar los resultados de un nivel
def mostrar_resultados(preguntas, respuestas_usuario, respuestas_correctas):
    print("\nRespuestas Correctas:")
    # Iteramos sobre cada pregunta para mostrar si la respuesta fue correcta o incorrecta
    for i, (pregunta, respuesta_correcta, opciones) in enumerate(preguntas):
        if respuestas_usuario[i] == respuesta_correcta:
            print(f"Pregunta {i+1}: Correcta ✅ ({respuestas_usuario[i]})")
        else:
            print(f"Pregunta {i+1}: Incorrecta ❌ ({respuestas_usuario[i]}) - Correcta: {respuesta_correcta}")

    print(f"\nTu puntaje total fue: {respuestas_correctas}/{len(preguntas)} ⭐")#Utilizamos len() para contar la cantidad de caracteres
#----------------------
# Función principal del juego
def main():
    print("¿Estás preparado? (SI/NO) 🎉")
    preparado = input().upper()
    
    if preparado != "SI":
        print("Juego terminado. Gracias, vuelve pronto! 🏀")
        return
    
    print("\n¡Que comience el juego! 🎉")

    print("\nNivel 1: Conocimientos generales sobre baloncesto 🏀")
    # Jugamos el nivel 1
    respuestas_correctas_nivel_1, respuestas_usuario_nivel_1 = jugar_nivel(preguntas_nivel_1)
    
    # Mostramos los resultados del nivel 1
    mostrar_resultados(preguntas_nivel_1, respuestas_usuario_nivel_1, respuestas_correctas_nivel_1)
    
    # Verificamos si el usuario pasó al siguiente nivel
    if respuestas_correctas_nivel_1 >= 7:
        print("\n¡Interesante! Veo que sabes sobre las reglas básicas del baloncesto.")
        print("\n¡Bien hecho, has pasado al siguiente nivel! 🎉")
        print("¿Estás preparado para la segunda parte? Esto se pondrá más complicado. (SI/NO) 🎉")
        preparado_segundo_nivel = input().upper()
        
        if preparado_segundo_nivel != "SI":
            print("Juego terminado. ❌")
            return
        
        print("\nNivel 2: Ahora veremos tus conocimientos sobre la NBA!!!")
        # Jugamos el nivel 2
        respuestas_correctas_nivel_2, respuestas_usuario_nivel_2 = jugar_nivel(preguntas_nivel_2)
        
        # Mostramos los resultados del nivel 2
        mostrar_resultados(preguntas_nivel_2, respuestas_usuario_nivel_2, respuestas_correctas_nivel_2)
        
        # Calculamos el puntaje total sumando los puntajes de ambos niveles
        puntaje_total = respuestas_correctas_nivel_1 + respuestas_correctas_nivel_2
        print(f"\nTu puntaje total fue: {puntaje_total}/{len(preguntas_nivel_1) + len(preguntas_nivel_2)} ⭐")
        
        # Mensajes adicionales basados en el puntaje total
        if puntaje_total == 20:
            print("¡Increíble! Respondiste todas las preguntas correctamente. Eres un verdadero experto en el Basquet y la NBA. 🎉🏀")
        elif puntaje_total > 16:
            print("¡Fantástico! Tienes un conocimiento impresionante sobre Basquet y la NBA. ¡Felicidades! 🎉🏀")
        elif puntaje_total >= 15:
            print("¡Muy bien! Tienes un buen conocimiento sobre Basquet y la NBA. ¡Buen trabajo! 🎉🏀")
        elif puntaje_total >= 13:
            print("Nada mal, nada mal. ✅")
    else:
        print("\nQué lástima. No has superado la primera parte. Mejor suerte para la próxima. ❌")
    
    # Preguntamos al usuario si desea volver a jugar
    print("\n¿Te gustaría volver a jugar? (SI/NO) 🎉")
    volver_a_jugar = input().upper()
    if volver_a_jugar == "SI":
        main() # Reiniciamos el juego
    else:
        print("Juego terminado. Gracias, vuelve pronto! 🏀")
#-------------------
# Ejecutamos la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()
