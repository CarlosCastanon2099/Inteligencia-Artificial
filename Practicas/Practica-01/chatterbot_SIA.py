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
	['Me puedes recomendar musica', 'Te recomiendo la canción "Uprising" de Muse'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Shape of You" de Ed Sheeran'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Thinking Out Loud" de Ed Sheeran'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Perfect" de Ed Sheeran'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Castle on the Hill" de Ed Sheeran'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Photograph" de Ed Sheeran'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Galway Girl" de Ed Sheeran'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "I See Fire" de Ed Sheeran'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "The A Team" de Ed Sheeran'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Happier" de Ed Sheeran'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Don\'t" de Ed Sheeran'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Sing" de Ed Sheeran'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Bloodstream" de Ed Sheeran'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Lego House" de Ed Sheeran'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Give Me Love" de Ed Sheeran'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "One" de Ed Sheeran'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Absolution" de Muse'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Take Me Out" de Franz Ferdinand'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Inside the Rose" de These New Puritans'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Paranoid Android" de Radiohead'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Appetite for Destruction" de Guns N Roses'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Led Zeppelin IV" de Led Zeppelin'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Bohemian Rhapsody" de Queen'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Radioactive" de Imagine Dragons'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Hot Fuss" de The Killers'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Is This It" de The Strokes'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Random Access Memories" de Daft Punk'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Back in Black" de AC DC'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "The Golden Age" de Woodkid'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Blurryface" de Twenty One Pilots'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Love at First Sting" de Scorpions'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "La Culpa" de Los Bunkers'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "A Fever You Can\'t Sweat Out" de Panic! at the Disco'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "A Rush of Blood to the Head" de Coldplay'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Toys in the Attic" de Aerosmith'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Ballroom Blitz" de Sweet'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Smells Like Teen Spirit" de Nirvana'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Reptilectric" de Zoé'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Shape of You" de Ed Sheeran'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Red" de Taylor Swift'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "SOUR" de Olivia Rodrigo'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Roar" de Katy Perry'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Runaway" de Aurora'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Franz Ferdinand" de Franz Ferdinand'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "It\'s a Shame" de First Aid Kit'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Creep" de Radiohead'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Sweet Child O\' Mine" de Guns N Roses'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Physical Graffiti" de Led Zeppelin'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Don\'t Stop Me Now" de Queen'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Demons" de Imagine Dragons'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Mr. Brightside" de The Killers'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Room on Fire" de The Strokes'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Get Lucky" de Daft Punk'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Highway to Hell" de AC DC'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Iron" de Woodkid'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Stressed Out" de Twenty One Pilots'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Wind of Change" de Scorpions'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "La Marcha del Desierto" de Los Bunkers'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "I Write Sins Not Tragedies" de Panic! at the Disco'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "X&Y" de Coldplay'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Permanent Vacation" de Aerosmith'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "The Ballroom Blitz" de Sweet'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Come As You Are" de Nirvana'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Reptilectric Revisitado" de Zoé'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Perfect" de Ed Sheeran'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "1989" de Taylor Swift'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "SOUR" de Olivia Rodrigo'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Firework" de Katy Perry'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Runaway" de Aurora'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "The Resistance" de Muse'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Do You Want To" de Franz Ferdinand'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Dust Bowl Dance" de Mumford & Sons'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Karma Police" de Radiohead'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "November Rain" de Guns N Roses'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Led Zeppelin II" de Led Zeppelin'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "We Will Rock You" de Queen'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Whatever It Takes" de Imagine Dragons'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Somebody Told Me" de The Killers'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Angles" de The Strokes'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Around the World" de Daft Punk'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Back in Black" de AC DC'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Run Boy Run" de Woodkid'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Heathens" de Twenty One Pilots'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Rock You Like a Hurricane" de Scorpions'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Barrio Estación" de Los Bunkers'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Death of a Bachelor" de Panic! at the Disco'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Viva la Vida or Death and All His Friends" de Coldplay'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Get a Grip" de Aerosmith'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Fox on the Run" de Sweet'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Come As You Are" de Nirvana'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Programatón" de Zoé'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Photograph" de Ed Sheeran'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "Speak Now" de Taylor Swift'],
	    ['Me puedes recomendar musica', 'Te recomiendo el álbum "SOUR" de Olivia Rodrigo'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Teenage Dream" de Katy Perry'],
	    ['Me puedes recomendar musica', 'Te recomiendo la canción "Running with the Wolves" de Aurora'],
	['Me puedes recomendar musica', 'Te recomiendo el album The New Abnormal de The Strokes'],
]

recomendar_pelicula =[
    ["Me puedes recomendar una pelicula", 'Te recomiendo la pelicula "Dancer in the dark"'],
    ['Me recomiendas una pelicula', 'Te recomiendo la pelicula "Parasitos"'],
        ["Me puedes recomendar una pelicula", 'Te recomiendo la película 300 dirigida por Zack Snyder'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Batman v Superman: Dawn of Justice dirigida por Zack Snyder'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Justice League dirigida por Zack Snyder'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Man of Steel dirigida por Zack Snyder'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Watchmen dirigida por Zack Snyder'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película The Dark Knight dirigida por Christopher Nolan'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Inception dirigida por Christopher Nolan'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Interstellar dirigida por Christopher Nolan'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película The Shape of Water dirigida por Guillermo del Toro'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Pan s Labyrinth dirigida por Guillermo del Toro'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Birdman dirigida por Alejandro González Iñárritu'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película The Revenant dirigida por Alejandro González Iñárritu'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Gravity dirigida por Alfonso Cuarón'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Y tu mamá también dirigida por Alfonso Cuarón'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Belle de Jour dirigida por Luis Buñuel'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película The Discreet Charm of the Bourgeoisie" dirigida por Luis Buñuel'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Schindler s List dirigida por Steven Spielberg'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Jurassic Park dirigida por Steven Spielberg'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película The Godfather dirigida por Francis Ford Coppola'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Apocalypse Now dirigida por Francis Ford Coppola'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Pulp Fiction dirigida por Quentin Tarantino'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Reservoir Dogs dirigida por Quentin Tarantino'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Goodfellas dirigida por Martin Scorsese'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Taxi Driver dirigida por Martin Scorsese'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película The Shining dirigida por Stanley Kubrick'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película A Clockwork Orange dirigida por Stanley Kubrick'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Avatar dirigida por James Cameron'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Titanic dirigida por James Cameron'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Scent of a Woman dirigida por Martin Brest'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Meet Joe Black dirigida por Martin Brest'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Avengers: Endgame dirigida por Anthony y Joe Russo'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Avengers: Infinity War dirigida por Anthony y Joe Russo'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película The English Patient dirigida por Anthony Minghella'],
    ["Me puedes recomendar una pelicula", 'Te recomiendo la película Cold Mountain dirigida por Anthony Minghella']
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
