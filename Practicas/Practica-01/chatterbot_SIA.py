from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.conversation import Statement


chat = ChatBot('Recomendabot',
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                

                logic_adapters=[ 
                    {
                        "import_path": "chatterbot.logic.BestMatch",
                        "statement_comparison_function": "chatterbot.comparisons.LevenshteinDistance",
                    }
                ],
                )
saludos=[
    ['Hola', 'Hola'],
    ['Buenos dias', 'Buen dia'],
    ['Buen dia', 'Buen dia'],
    ['Como estas', "Bien, Gracias"]
]

recomendar_musica = [
	['Me puedes recomendar musica', 'Te recomiendo el album The New Abnormal de The Strokes'],
]

recomendar_pelicula =[
    ["Me puedes recomendar una pelicula", 'Te recomiendo la pelicula "Dancer in the dark"'],
    ['Me recomiendas una pelicula', 'Te recomiendo la pelicula "Parasitos"'],
]

chistes=[
    ['Me puedes contar un chiste', 'Por qué nunca puedes ver a hipopotamos escondidos en los arboles? Porque son muy buenos'],
    ['Me puedes contar un chiste', 'Qué es rojo y malo para tus diente? Un ladrillo'],
    ['Me puedes contar un chiste', 'Que le dijo un pollo policia a otro pollo policia? "Necesitamos apollo"'],
    ['Cuentame un chiste', 'Que hace una vaca en una mina? Vaca-minando'],
]
datos_curiosos=[
    ['Me puedes contar un dato curioso', 'Rusia es mas grande que Pluton'],
    ['Me puedes contar un dato curioso', 'Minecraft ya es el videojuego mas vendido en el mundo'],
    ['Me puedes contar un dato curioso', 'Las galletas oreos son aptas para veganos'],
]

agradecimientos = [
    ['Gracias', 'De nada'],
    ['Muchas gracias', 'Un placer ayudarte']
]

levenshtein_distance = LevenshteinDistance('spanish ')

trainer = ListTrainer(chat)
for i in range(10):
    for saludo in saludos: trainer.train(saludo)
    for musica in recomendar_musica: trainer.train(musica)
    for pelicula in recomendar_pelicula: trainer.train(pelicula)
    for chiste in chistes: trainer.train(chiste)
    for agradecimiento in agradecimientos: trainer.train(agradecimiento)

peticion = ""


while levenshtein_distance.compare(Statement(peticion) , Statement('Adios') ) < 0.50:
    peticion = input('Tú: ' )
    respuesta = chat.get_response(peticion)
    print('Bot: ', respuesta)

print('Gracias por usar el recomendabot\nTiene alguna sugerencia para mejorar el bot?')
input('Tu: ')
print('Gracias, Nos sirve mucho su sugerencia, Que tenga un buen dia!')
