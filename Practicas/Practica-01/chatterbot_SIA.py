from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.conversation import Statement

# Creamos un nuevo ChatBot
chat = ChatBot('Recomendabot',
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                
    			statement_comparison_function=LevenshteinDistance,
                logic_adapters=[ 
                    {
                        "import_path": "chatterbot.logic.BestMatch",
                        "statement_comparison_function": "chatterbot.comparisons.LevenshteinDistance",
                    }
                ],
                )

# En los siguientes arreglos se encuentran las respuestas que el chatbot puede dar:
# Estas estan enfocadas a saludar, despedirse, dar recomendaciones de musica y peliculas, contar chistes y dar datos curiosos

# Arreglo que contiene las respuestas a los posibles saludos del usuario
saludos = [
    ['Hola', 'Hola'],
    ['Buenos dias', 'Buen dia'],
    ['Buen dia', 'Buen dia'],
    ['Como estas', "Bien, Gracias"],
    ['Buenas noches', 'Buenas noches'],
    [' Como va todo', "Todo perfecto, gracias"], #######################
    ['Encantado de conocerte', "El placer es mio"],
    ['Como te llamas', "Me llamo Maxwell,  y tu"],
    ['Mucho gusto', "Igualmente"],
    ['Que haces por aqui', "Estoy aqui para ayudarte con lo que necesites"],
    ['Me puedes ayudar', "Por supuesto,  en que puedo ayudarte"],
    ['Tienes un minuto', "Si, dime que necesitas"],
    ['De que podemos hablar', "De lo que tu quieras"],
    ['Que te parece el dia de hoy', "Un dia precioso,  verdad"],
    ['Que planes tienes para el fin de semana', "Todavia no lo se,  y tu"],
    ['Te gusta leer', "Si, me encanta leer"],
    ['Cual es tu libro favorito', "Tengo muchos libros favoritos,  y tu"],
    ['Te gusta el cine', "Si, me encanta ir al cine"],
    ['Te gusta viajar', "Si, me encanta viajar"],
    ['Cual es tu lugar favorito para viajar', "Tengo muchos lugares favoritos,  y tu"],
    ['Tienes algun sueño por cumplir', "Si, muchos sueños por cumplir"],
    ['Cual es tu mayor sueño', "Mi mayor sueño es ayudar a las personas"],
    ['Que te hace feliz', "Me hace feliz ayudar a las personas y hacerlas sonreir"],
    ['Que te hace triste', "Me hace triste ver sufrir a las personas"],
    ['Que te hace enojar', "Me enoja la injusticia y la crueldad"],
    ['Que te motiva', "Me motiva la posibilidad de hacer un cambio positivo en el mundo"],
    ['Que consejo le darias a alguien que esta pasando por un momento dificil', "Que nunca se rinda y que siempre tenga esperanza"],
    ['Que mensaje le darias al mundo', "Que seamos mas amables y compasivos con los demas"],
]

# Arreglo que contiene las respuestas a los posibles solicitudes de recomendaciones de musica del usuario
recomendar_musica = [
		# ['Me puedes recomendar musica', 'Te recomiendo el album Barrio Estacion de Los Bunkers'],
	    # ['Me puedes recomendar musica', 'Te recomiendo la cancion Death of a Bachelor de Panic at the Disco'],
	    # ['Me puedes recomendar musica', 'Te recomiendo el album Viva la Vida or Death and All His Friends de Coldplay'],
	    # ['Me puedes recomendar musica', 'Te recomiendo el album Get a Grip de Aerosmith'],
	    # ['Me puedes recomendar musica', 'Te recomiendo la cancion Fox on the Run de Sweet'],
	    # ['Me puedes recomendar musica', 'Te recomiendo la cancion Come As You Are de Nirvana'],
	    # ['Me puedes recomendar musica', 'Te recomiendo el album Programaton de Zoe'],
	    # ['Me puedes recomendar musica', 'Te recomiendo la cancion Photograph de Ed Sheeran'],
	    # ['Me puedes recomendar musica', 'Te recomiendo el album Speak Now de Taylor Swift'],
	    # ['Me puedes recomendar musica', 'Te recomiendo el album SOUR de Olivia Rodrigo'],
	    # ['Me puedes recomendar musica', 'Te recomiendo la cancion Teenage Dream de Katy Perry'],
	    # ['Me puedes recomendar musica', 'Te recomiendo la cancion Running with the Wolves de Aurora'],
		# ['Me puedes recomendar musica', 'Te recomiendo el album The New Abnormal de The Strokes'],
		['Me puedes recomendar musica', 'Te recomiendo la cancion "Uprising" de Muse'], 
		['Me recomiendas alguna cancion', 'Te recomiendo la cancion Shape of You de Ed Sheeran'],
		['Podrias sugerirme algo para escuchar', 'Te recomiendo la cancion Collide de Ed Sheeran'],
		['Tienes alguna cancion en mente', 'Te recomiendo la cancion Perfect de Ed Sheeran'],
		['Algun tema que me recomiendes', 'Te recomiendo la cancion Castle on the Hill de Ed Sheeran'],
		['Que cancion me sugieres', 'Te recomiendo la cancion Photograph de Ed Sheeran'],
		['Conoces alguna buena cancion', 'Te recomiendo la cancion Galway Girl de Ed Sheeran'],
		['Puedes recomendarme algo de musica', 'Te recomiendo la cancion 2Step de Ed Sheeran'],
		['Me das una recomendacion musical', 'Te recomiendo la cancion The A Team de Ed Sheeran'],
		['Tienes alguna cancion para compartir', 'Te recomiendo la cancion Happier de Ed Sheeran'],
		['Quiero escuchar algo,  que me sugieres', 'Te recomiendo la cancion Don\'t de Ed Sheeran'],
		['Me recomiendas alguna melodia', 'Te recomiendo la cancion Sing de Ed Sheeran'],
		['Podrias sugerirme una cancion', 'Te recomiendo la cancion Bloodstream de Ed Sheeran'],
		['Que cancion me recomiendas', 'Te recomiendo la cancion Lego House de Ed Sheeran'],
		['Puedes recomendarme algo de musica', 'Te recomiendo la cancion Give Me Love de Ed Sheeran'],
		['Me das una recomendacion musical', 'Te recomiendo la cancion One de Ed Sheeran'],
		['Tienes alguna cancion en mente', 'Te recomiendo el album Absolution de Muse'],
		['Me recomiendas algo de musica', 'Te recomiendo la cancion Take Me Out de Franz Ferdinand'],
		['Podrias sugerirme algo para escuchar', 'Te recomiendo el album Inside the Rose de These New Puritans'],
		['Que cancion me sugieres', 'Te recomiendo la cancion Paranoid Android de Radiohead'],
		['Algun tema que me recomiendes', 'Te recomiendo el album Appetite for Destruction de Guns N Roses'],
		['Conoces alguna buena cancion', 'Te recomiendo el album Led Zeppelin IV de Led Zeppelin'],
		['Puedes recomendarme algo de musica', 'Te recomiendo la cancion Bohemian Rhapsody de Queen'],
		['Me das una recomendacion musical', 'Te recomiendo la cancion Radioactive de Imagine Dragons'],
		['Tienes alguna cancion para compartir', 'Te recomiendo el album Hot Fuss de The Killers'],
		['Quiero escuchar algo,  que me sugieres', 'Te recomiendo el album Is This It de The Strokes'],
		['Me recomiendas alguna melodia', 'Te recomiendo el album Random Access Memories de Daft Punk'],
		['Podrias sugerirme una cancion', 'Te recomiendo el album Back in Black de AC DC'],
		['Que cancion me recomiendas', 'Te recomiendo el album The Golden Age de Woodkid'],
		['Puedes recomendarme algo de musica', 'Te recomiendo el album Blurryface de Twenty One Pilots'],
		['Me das una recomendacion musical', 'Te recomiendo el album Love at First Sting de Scorpions'],
		['Tienes alguna cancion en mente', 'Te recomiendo el album La Culpa de Los Bunkers'],
		['Me recomiendas algo de musica', 'Te recomiendo el album A Fever You Can\'t Sweat Out de Panic at the Disco'],
		['Podrias sugerirme algo para escuchar', 'Te recomiendo el album A Rush of Blood to the Head de Coldplay'],
		['Que cancion me sugieres', 'Te recomiendo el album Toys in the Attic de Aerosmith'],
		['Algun tema que me recomiendes', 'Te recomiendo la cancion Ballroom Blitz de Sweet'],
		['Conoces alguna buena cancion', 'Te recomiendo la cancion Smells Like Teen Spirit de Nirvana'],
		['Puedes recomendarme algo de musica', 'Te recomiendo el album Reptilectric de Zoe'],
		['Me das una recomendacion musical', 'Te recomiendo la cancion Shape of You de Ed Sheeran'],
		['Tienes alguna cancion para compartir', 'Te recomiendo el album Red de Taylor Swift'],
		['Quiero escuchar algo,  que me sugieres', 'Te recomiendo el album SOUR de Olivia Rodrigo'],
		['Me recomiendas alguna melodia', 'Te recomiendo la cancion Roar de Katy Perry'],
		['Podrias sugerirme una cancion', 'Te recomiendo la cancion Runaway de Aurora'],
		['Que cancion me recomiendas', 'Te recomiendo el album Franz Ferdinand de Franz Ferdinand'],
		['Puedes recomendarme algo de musica', 'Te recomiendo la cancion It\'s a Shame de First Aid Kit'],
		['Me das una recomendacion musical', 'Te recomiendo la cancion Creep de Radiohead'],
		['Tienes alguna cancion en mente', 'Te recomiendo la cancion Sweet Child O\' Mine de Guns N Roses'],
		['Me recomiendas algo de musica', 'Te recomiendo el album Physical Graffiti de Led Zeppelin'],
		['Podrias sugerirme algo para escuchar', 'Te recomiendo la cancion Don\'t Stop Me Now de Queen'],
		['Que cancion me sugieres', 'Te recomiendo la cancion Demons de Imagine Dragons'],
		['Algun tema que me recomiendes', 'Te recomiendo la cancion Mr. Brightside de The Killers'],
		['Conoces alguna buena cancion', 'Te recomiendo el album Room on Fire de The Strokes'],
		['Puedes recomendarme algo de musica', 'Te recomiendo la cancion Get Lucky de Daft Punk'],
		['Me das una recomendacion musical', 'Te recomiendo el album Highway to Hell de AC DC'],
		['Tienes alguna cancion para compartir', 'Te recomiendo la cancion Iron de Woodkid'],
		['Quiero escuchar algo,  que me sugieres', 'Te recomiendo la cancion Stressed Out de Twenty One Pilots'],
		['Me recomiendas alguna melodia', 'Te recomiendo la cancion Wind of Change de Scorpions'], 

]

# Arreglo que contiene las respuestas a los posibles solicitudes de recomendaciones de peliculas del usuario
recomendar_pelicula =[
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula Gladiator (2000)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula Una mente maravillosa (2001)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula Chicago (2002)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula El Señor de los Anillos: el retorno del Rey (2003)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula Million Dollar Baby (2004)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula Crash (2005)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula Los Infiltrados (2006)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula No Country for Old Men (2007)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula  Slumdog Millionaire (2008)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula The Hurt Locker (2009)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula El discurso del Rey (2010)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula The Artist (2011)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula Argo (2012)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula 12 Years a Slave (2013)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula Birdman (2014)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula Spotlight (2015)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula Moonlight (2016)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula La forma del agua (2017)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula Green Book (2018)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula Parasitos (2019)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula Nomadland (2020)"],
    # ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula CODA (2021)"],
    ["Me puedes recomendar una pelicula", "Te recomiendo la pelicula Todo a la vez en todas partes (2022)"], ############
    ["Recomiendame una pelicula", 'Te recomiendo la pelicula Dancer in the dark'],
    ['Me recomiendas alguna pelicula', 'Te recomiendo la pelicula Parasitos'],
    ["Podrias sugerirme una pelicula", 'Te recomiendo la pelicula 300 dirigida por Zack Snyder'],
    ["Que pelicula me sugieres", 'Te recomiendo la pelicula Batman v Superman: Dawn of Justice dirigida por Zack Snyder'],
    ["Tienes alguna pelicula en mente", 'Te recomiendo la pelicula Justice League dirigida por Zack Snyder'],
    ["Algun filme que me recomiendes", 'Te recomiendo la pelicula Man of Steel dirigida por Zack Snyder'],
    ["Conoces alguna buena pelicula", 'Te recomiendo la pelicula Watchmen dirigida por Zack Snyder'],
    ["Puedes recomendarme algo para ver", 'Te recomiendo la pelicula The Dark Knight dirigida por Christopher Nolan'],
    ["Me das una recomendacion de pelicula", 'Te recomiendo la pelicula Inception dirigida por Christopher Nolan'],
    ["Tienes alguna pelicula para compartir", 'Te recomiendo la pelicula Interstellar dirigida por Christopher Nolan'],
    ["Quiero ver una pelicula,  que me sugieres", 'Te recomiendo la pelicula The Shape of Water dirigida por Guillermo del Toro'],
    ["Me recomiendas alguna pelicula", 'Te recomiendo la pelicula Pan s Labyrinth dirigida por Guillermo del Toro'],
    ["Podrias sugerirme una pelicula", 'Te recomiendo la pelicula Birdman dirigida por Alejandro Gonzalez Iñarritu'],
    ["Que pelicula me sugieres", 'Te recomiendo la pelicula The Revenant dirigida por Alejandro Gonzalez Iñarritu'],
    ["Tienes alguna pelicula en mente", 'Te recomiendo la pelicula Gravity dirigida por Alfonso Cuaron'],
    ["Me recomiendas alguna pelicula", 'Te recomiendo la pelicula Y tu mama tambien dirigida por Alfonso Cuaron'],
    ["Podrias sugerirme una pelicula", 'Te recomiendo la pelicula Belle de Jour dirigida por Luis Buñuel'],
    ["Que pelicula me sugieres", 'Te recomiendo la pelicula The Discreet Charm of the Bourgeoisie dirigida por Luis Buñuel'],
    ["Tienes alguna pelicula para compartir", 'Te recomiendo la pelicula Schindler s List dirigida por Steven Spielberg'],
    ["Quiero ver una pelicula,  que me sugieres", 'Te recomiendo la pelicula Jurassic Park dirigida por Steven Spielberg'],
    ["Me das una recomendacion de pelicula", 'Te recomiendo la pelicula The Godfather dirigida por Francis Ford Coppola'],
    ["Tienes alguna pelicula para compartir", 'Te recomiendo la pelicula Apocalypse Now dirigida por Francis Ford Coppola'],
    ["Podrias sugerirme una pelicula", 'Te recomiendo la pelicula Pulp Fiction dirigida por Quentin Tarantino'],
    ["Que pelicula me sugieres", 'Te recomiendo la pelicula Reservoir Dogs dirigida por Quentin Tarantino'],
    ["Me recomiendas alguna pelicula", 'Te recomiendo la pelicula Goodfellas dirigida por Martin Scorsese'],
    ["Podrias sugerirme una pelicula", 'Te recomiendo la pelicula Taxi Driver dirigida por Martin Scorsese'],
    ["Tienes alguna pelicula para compartir", 'Te recomiendo la pelicula The Shining dirigida por Stanley Kubrick'],
    ["Quiero ver una pelicula,  que me sugieres", 'Te recomiendo la pelicula A Clockwork Orange dirigida por Stanley Kubrick'],
    ["Me das una recomendacion de pelicula", 'Te recomiendo la pelicula Avatar dirigida por James Cameron'],
    ["Tienes alguna pelicula para compartir", 'Te recomiendo la pelicula Titanic dirigida por James Cameron'],
    ["Podrias sugerirme una pelicula", 'Te recomiendo la pelicula Scent of a Woman dirigida por Martin Brest'],
    ["Que pelicula me sugieres", 'Te recomiendo la pelicula Meet Joe Black dirigida por Martin Brest'],
    ["Me recomiendas alguna pelicula", 'Te recomiendo la pelicula Avengers: Endgame dirigida por Anthony y Joe Russo'],
    ["Podrias sugerirme una pelicula", 'Te recomiendo la pelicula Avengers: Infinity War dirigida por Anthony y Joe Russo'],
    ["Tienes alguna pelicula para compartir", 'Te recomiendo la pelicula The English Patient dirigida por Anthony Minghella'],
    ["Quiero ver una pelicula,  que me sugieres", 'Te recomiendo la pelicula Cold Mountain dirigida por Anthony Minghella'],
]

# Arreglo que contiene las respuestas a los posibles solicitudes de chistes del usuario
chistes = [
    # ['Me puedes contar un chiste', ' Que le dice un jaguar a otro jaguar "Jaguar you"'],
    # ['Me puedes contar un chiste', ' Que hace una abeja en el gimnasio Zum-ba'],
    # ['Me puedes contar un chiste', ' Que hace una iguana tomando el sol Hace iguana-ras.'],
    # ['Me puedes contar un chiste', ' Cual es el animal mas antiguo La cebra, porque esta en blanco y negro.'],
    ['Me puedes contar un chiste', ' Por que los pajaros no usan Facebook Porque ya tienen Twitter.'],
    ['Puedes contarme algo gracioso', ' Por que los pajaros no usan paraguas Porque ya tienen plumas'],
    ['Necesito una dosis de humor, tienes algo', ' Cual es el animal mas antiguo La cebra, porque esta en blanco y negro'],
    ['Me puedes contar una broma', ' Por que el mar esta tan enojado Porque siempre lo dejan olas'],
    ['Quiero reirme Cuentame algo divertido', ' Que hace una vaca en el espacio La vaca-gravedad'],
    ['Estoy de humor para un chiste,  tienes alguno', ' Que le dijo una iguana a su hermana gemela Somos iguanitas'],
    ['Puedes hacerme sonreir', ' Por que las focas miran siempre hacia arriba Porque ahi estan los focos'],
    ['Tienes algo para levantar el animo', ' Por que el libro de matematicas estaba triste Porque tenia demasiados problemas'],
    ['Necesito un chiste para animarme,  puedes ayudarme', ' Que hace una rana en el gimnasio Ejercicios de salto'],
    ['Me puedes contar algo gracioso para alegrar mi dia', ' Que le dice un semaforo a otro No me mires, que me pongo rojo'],
    ['Quiero una broma,  tienes alguna', ' Por que el cafe mas peligroso del mundo El ex-preso'],
    ['Puedes contarme algo gracioso', ' Que hace una impresora en el gimnasio Hojas de ejercicios'],
    ['Necesito un chiste para animarme,  puedes ayudarme', ' Que le dice un huevo a una sarten Me tienes frito'],
    ['Estoy aburrido Cuentame un chiste', ' Que hace un pato con una pata Pata-rrer'],
    ['Me cuentas un chiste', ' Que hace una ola en la playa Saluda'],
    ['Quiero una broma', ' Por que el libro de ciencias naturales estaba tan cansado Porque llevaba mucho tiempo leyendo'],
    ['Quiero reirme Cuentame algo divertido', ' Que hace una abeja en el cine Zumbidos'],
    ['Estoy de humor para un chiste,  tienes alguno', ' Cual es el colmo de un astronauta Tener mal humor'],
    ['Puedes hacerme sonreir', ' Que le dice un arbol a otro Que pasa tronco'],
    ['Tienes algo para levantar el animo', ' Por que el mar no tiene frenos Porque tiene olas'],
    ['Necesito un chiste para animarme,  puedes ayudarme', ' Que hace una abeja en el gimnasio Zum-ba'],
    ['Quiero reir un poco', ' Que le dijo un pez a otro pez "Nada, estamos en el agua"'],
    ['Necesito un chiste para animarme', ' Que hace una vaca en una montaña Vaca-escalando'],
    ['Me siento aburrido, dame un chiste', ' Por que el libro de matematicas estaba triste Porque tenia demasiados problemas'],
    ['Puedes alegrarme el dia', ' Que hace un perro con un taladro Perforar'],
    ['Tienes algo para hacerme sonreir', ' Como se llama el campeon de buceo japones Tokofondo'],
    ['Cuentame algo gracioso', ' Que hace una abeja en el gimnasio Zum-ba'],
    ['Quiero reir un poco', ' Que le dijo un pez a otro pez "Nada, estamos en el agua"'],
    ['Necesito un chiste para animarme', ' Que hace una vaca en una montaña Vaca-escalando'],
    ['Me siento aburrido, dame un chiste', ' Por que el libro de matematicas estaba triste Porque tenia demasiados problemas'],
    ['Puedes alegrarme el dia', ' Que hace un perro con un taladro Perforar'],
    ['Tienes algo para hacerme sonreir', ' Como se llama el campeon de buceo japones Tokofondo'],
	['Puedes contarme algo gracioso', ' Que hace una vaca en el espacio La vaca-gravedad'],
    ['Necesito una dosis de humor,  tienes algo', ' Por que el mar esta tan enojado Porque siempre lo dejan olas'],
    ['Me puedes contar una broma', ' Que hace una abeja en el gimnasio Zum-ba'],
    ['Quiero reirme Cuentame algo divertido', ' Como se llama un perro mago Labracadabrador'],
    ['Estoy de humor para un chiste,  tienes alguno', ' Cual es el colmo de un electricista No tener corriente de trabajo'],
    ['Puedes hacerme sonreir', ' Que le dice un semaforo a otro No me mires, que me pongo rojo'],
    ['Tienes algo para levantar el animo', ' Cual es el animal mas antiguo La cebra, porque esta en blanco y negro'],
    ['Necesito un chiste para animarme,  puedes ayudarme', ' Por que los pajaros no usan Facebook Porque ya tienen Twitter'],
    ['Me puedes contar algo gracioso para alegrar mi dia', ' Como se llama el campeon de buceo japones Tokofondo'],
    ['Quiero una broma,  tienes alguna', ' Que hace un pato con una pata Pata-rrer'],
    ['Puedes contarme algo chistoso', ' Que hace una ola en la playa Saluda'],
    ['Necesito un poco de humor,  tienes un chiste', ' Por que el libro de matematicas estaba triste Porque tenia demasiados problemas'],
    ['Cuentame un chiste', ' Que le dijo una iguana a su hermana gemela Somos iguanitas'],
    ['Tienes algo para hacerme reir', ' Por que las focas miran siempre hacia arriba Porque ahi estan los focos'],
    ['Puedes contarme algo gracioso', ' Que hace una rana en el gimnasio Ejercicios de salto'],
    ['Necesito un chiste para animarme,  puedes ayudarme', ' Por que los pajaros no usan paraguas Porque ya tienen plumas'],
    ['Me cuentas un chiste', ' Que hace una impresora en el gimnasio Hojas de ejercicios'],
    ['Quiero una broma,  tienes alguna', ' Cual es el cafe mas peligroso del mundo El ex-preso'],
    ['Quiero reirme Cuentame algo divertido', ' Que hace una abeja en el cine Zumbidos'],
    ['Estoy de humor para un chiste,  tienes alguno', ' Cual es el colmo de un jardinero Tener mala tierra'],
    ['Puedes hacerme sonreir', ' Por que el libro de historia estaba tan nervioso Porque iba a perder el tiempo'],
    ['Tienes algo para levantar el animo', ' Que hace una oveja cuando tiene frio Se pone una ovejita'],
    ['Necesito un chiste para animarme,  puedes ayudarme', ' Por que el pan no se pierde en el mar Porque siempre tiene miga'],
    ['Me puedes contar algo gracioso para alegrar mi dia', ' Que le dice un huevo a una sarten Me tienes frito'],
    ['Quiero una broma,  tienes alguna', ' Por que el libro de ciencias naturales estaba tan cansado Porque llevaba mucho tiempo leyendo'],
    ['Quiero reirme Cuentame algo divertido', ' Que le dice una iguana a su hermana gemela Somos iguanitas'],
    ['Estoy de humor para un chiste,  tienes alguno', ' Cual es el colmo de un astronauta Tener mal humor'],
    ['Puedes hacerme sonreir', ' Que le dice un arbol a otro Que pasa tronco'],
    ['Tienes algo para levantar el animo', ' Por que el mar no tiene frenos Porque tiene olas'],
    ['Necesito un chiste para animarme,  puedes ayudarme', ' Que hace una abeja en el gimnasio Zum-ba'],
    ['Me puedes contar algo gracioso para alegrar mi dia', ' Que hace una rata con una metralleta Ratatatata'],
    ['Quiero una broma,  tienes alguna', ' Cual es el animal mas antiguo La cebra, porque esta en blanco y negro'],
    ['Quiero reirme Cuentame algo divertido', ' Que le dice un arbol a otro Que pasa tronco'],
    ['Estoy de humor para un chiste,  tienes alguno', ' Que hace una abeja en el gimnasio Zum-ba'],
    ['Puedes hacerme sonreir', ' Por que el mar esta tan salado Porque nunca le dicen nada bonito'],
    ['Tienes algo para levantar el animo', ' Cual es el animal mas antiguo La cebra, porque esta en blanco y negro'],
    ['Necesito un chiste para animarme,  puedes ayudarme', ' Que le dice un jardinero a otro jardinero Eres un rastrero'],
]

# Arreglo que contiene las respuestas a los posibles solicitudes de datos curiosos del usuario
datos_curiosos = [
    # ['Me puedes contar un dato curioso', 'Rusia es mas grande que Pluton'],
    # ['Me puedes contar un dato curioso', 'Minecraft ya es el videojuego mas vendido en el mundo'],
    ['Dame un dato curioso', 'Las galletas oreos son aptas para veganos'],
    ['Me puedes contar un dato curioso', 'Los pulpos tienen tres corazones y azul de sangre'],
    ['Me puedes contar un hecho interesante', 'En Japon, es comun que las personas usen paraguas en dias soleados para protegerse de los rayos UV'],
    ['Sabes algun dato curioso', 'El corazon de una ballena azul es del tamaño de un coche pequeño'],
    ['Tienes algun dato interesante', 'La Gran Muralla China no es visible desde la luna a simple vista'],
    ['Puedes compartir un dato curioso', 'Los pingüinos tienen glandulas especiales para beber agua salada'],
    ['Dame un hecho interesante', 'Las abejas pueden reconocer rostros humanos'],
    ['Conoces algun dato curioso', 'El hielo es menos denso que el agua, por eso flota'],
    ['Me das un dato interesante', 'El primer producto que llevo codigo de barras fue un paquete de chicles Wrigley'],
    ['Tienes algun dato curioso para mi', 'La cantidad de dinero que se tira cada año en la basura podria alimentar a millones de personas'],
    ['Algun dato interesante que quieras compartir', 'Las vacas tienen mejores amigos y pueden sufrir de estres si estan separadas'],
    ['Me puedes contar una curiosidad', 'La miel nunca caduca, puede durar miles de años'],
    ['Puedes decirme algo sorprendente', 'Los ojos de los avestruces son mas grandes que su cerebro'],
    ['Tienes un dato curioso para revelar', 'El agujero en la capa de ozono es mas pequeño que hace 20 años'],
    ['Sabes algo interesante', 'La sandia es una fruta y una verdura'],
    ['Puedes compartir un dato intrigante', 'El elefante es el unico animal con 4 rodillas'],
    ['Conoces alguna curiosidad interesante', 'El estado de Florida es mas grande que Inglaterra'],
    ['Me puedes decir un hecho curioso', 'Las mariposas pueden saborear con sus patas'],
    ['Tienes algun dato asombroso', 'Las hormigas duermen aproximadamente 8 minutos en un periodo de 12 horas'],
    ['Sabes algo que me sorprenda', 'Los delfines tienen nombres propios para comunicarse'],
    ['Puedes revelarme un dato curioso', 'El nombre completo de Barbie es Barbara Millicent Roberts'],
    ['Me cuentas algo que no sepa', 'Las cebras tienen rayas unicas, al igual que las huellas dactilares de los humanos'],
    ['Algun dato que me deje pensando', 'En 20 minutos, el cuerpo humano produce suficiente calor para hervir agua'],
    ['Me puedes contar algo interesante', 'Los koalas tienen huellas dactilares indistinguibles de las de los humanos'],
    ['Puedes darme un dato sorprendente', 'La miel de abeja nunca se echa a perder'],
    ['Conoces algun hecho curioso', 'La estatua de la libertad fue un regalo de Francia para Estados Unidos'],
    ['Puedes compartir algo inusual', 'El platano es una baya, pero el platano es una fruta'],
    ['Me puedes decir un dato extraordinario', 'El corazon humano late alrededor de 100,000 veces al dia'],
    ['Algun dato que me haga reflexionar', 'El 8 es el unico numero que tiene la misma cantidad de letras que su valor'],
    ['Tienes alguna curiosidad para compartir', 'El oido humano puede distinguir mas de 1 millon de sonidos diferentes'],
    ['Puedes revelarme algo fascinante', 'El 10 Porciento de la poblacion mundial es zurda'],
    ['Sabes alguna curiosidad intrigante', 'El ojo de un avestruz es mas grande que su cerebro'],
    ['Me cuentas un dato poco conocido', 'Las jirafas tienen la misma cantidad de huesos en su cuello que los humanos'],
    ['Tienes algun dato curioso que contarme', 'Los gatos tienen mas huesos en sus cuerpos que los humanos'],
    ['Puedes darme un dato inusual', 'Las estrellas de mar no tienen cerebro'],
    ['Conoces algun hecho sorprendente', 'Los flamencos pueden dormir de pie'],
    ['Me puedes contar algo que me deje asombrado', 'El sol libera mas energia en un segundo que toda la energia consumida por la humanidad a lo largo de la historia'],
    ['Sabes alguna curiosidad interesante', 'Los pingüinos tienen glandulas especiales para desalinizar el agua de mar'],
    ['Tienes algun dato sorprendente para revelar', 'El alfabeto mas largo del mundo tiene 74 letras'],
    ['Me cuentas un dato asombroso', 'El corazon humano es tan fuerte que podria lanzar la sangre a una altura de 10 metros'],
    ['Puedes compartir algo que me haga reflexionar', 'Los elefantes son los unicos animales que no pueden saltar'],
    ['Conoces alguna curiosidad intrigante', 'Los ojos de un avestruz son mas grandes que su cerebro'],
    ['Tienes algun dato fascinante para compartir', 'Las vacas tienen mejores amigos y se estresan cuando estan separadas'],
    ['Puedes decirme un dato poco conocido', 'Las mariposas pueden oler con sus patas'],
    ['Me puedes revelar un hecho inusual', 'Las abejas pueden comunicarse con otras abejas a traves de la danza'],
    ['Sabes alguna curiosidad interesante', 'Los escorpiones brillan bajo luz ultravioleta'],
    ['Tienes algun dato sorprendente', 'Las cebras tienen rayas unicas, como las huellas dactilares de los humanos'],
    ['Puedes contarme algo que no sepa', 'Los koalas tienen huellas dactilares indistinguibles de las de los humanos'],
    ['Conoces alguna curiosidad asombrosa', 'La miel de abeja nunca se echa a perder'],
    ['Me puedes contar un dato que me deje pensando', 'El 40 Porciento de las personas que miran un reloj lo hacen justo en el momento en que los dos minutos son iguales'],
    ['Puedes decirme algo que me sorprenda', 'Los delfines tienen nombres propios para comunicarse'],
]

# Arreglo que contiene las respuestas a los posibles solicitudes de recomendaciones de videojuegos del usuario
videojuegos =[
    ['Me puedes recomendar un videojuego', 'Te recomiendo el videojuego de Halo'],
    ['Me puedes recomendar un juego', 'Te recomiendo el videojuego de Minecraft'],
    ['Recomiendame un videojuego', 'Te recomiendo el videojuego de Club Penguin'],
    ["Me puedes recomendar un videojuego", 'Te recomiendo el videojuego The Witcher 3: Wild Hunt'], ##############
    ["Me recomiendas algun videojuego", 'Te recomiendo el videojuego Red Dead Redemption 2'],
    ["Podrias sugerirme un videojuego", 'Te recomiendo el videojuego The Legend of Zelda: Breath of the Wild'],
    ["Que videojuego me sugieres", 'Te recomiendo el videojuego Dark Souls III'],
    ["Tienes algun videojuego en mente", 'Te recomiendo el videojuego Grand Theft Auto V'],
    ["Un juego que me recomiendes", 'Te recomiendo el videojuego Persona 5'],
    ["Conoces algun buen videojuego", 'Te recomiendo el videojuego Bloodborne'],
    ["Puedes recomendarme algo para jugar", 'Te recomiendo el videojuego Horizon Zero Dawn'],
    ["Me das una recomendacion de videojuego", 'Te recomiendo el videojuego God of War (2018)'],
    ["Tienes algun videojuego para compartir", 'Te recomiendo el videojuego Super Mario Odyssey'],
    ["Quiero jugar un videojuego", 'Te recomiendo el videojuego Sekiro: Shadows Die Twice'],
    ["Me recomiendas algun videojuego", 'Te recomiendo el videojuego Overwatch'],
    ["Podrias sugerirme un videojuego", 'Te recomiendo el videojuego Fortnite'],
    ["Que videojuego me sugieres", 'Te recomiendo el videojuego Minecraft'],
    ["Tienes algun videojuego en mente", 'Te recomiendo el videojuego Animal Crossing: New Horizons'],
    ["Me puedes recomendar un juego para jugar", 'Te recomiendo el videojuego Celeste'], #######################
    ["Me recomiendas algun videojuego", 'Te recomiendo el videojuego Hollow Knight'],
    ["Podrias sugerirme un juego", 'Te recomiendo el videojuego Stardew Valley'],
    ["Que juego me sugieres", 'Te recomiendo el videojuego Ori and the Blind Forest'],
    ["Tienes algun juego en mente", 'Te recomiendo el videojuego Cuphead'],
    ["Algun juego que me recomiendes", 'Te recomiendo el videojuego Dead Cells'],
    ["Conoces algun buen videojuego", 'Te recomiendo el videojuego Undertale'],
    ["Puedes recomendarme algo para jugar", 'Te recomiendo el videojuego Terraria'],
    ["Me das una recomendacion de videojuego", 'Te recomiendo el videojuego A Plague Tale: Innocence'],
    ["Tienes algun juego para compartir", 'Te recomiendo el videojuego Ori and the Will of the Wisps'],
    ["Quiero jugar un videojuego", 'Te recomiendo el videojuego Outer Wilds'],
    ["Me recomiendas algun videojuego", 'Te recomiendo el videojuego Monster Hunter: World'],
    ["Podrias sugerirme un juego", 'Te recomiendo el videojuego Sekiro: Shadows Die Twice'],
    ["Qu e videojuego me sugieres", 'Te recomiendo el videojuego Control'],
    ["Tienes algun videojuego en mente", 'Te recomiendo el videojuego Resident Evil 2 (2019)'],
    ["Algun juego que me recomiendes", 'Te recomiendo el videojuego Returnal'],
    ["Conoces algun buen videojuego", 'Te recomiendo el videojuego Death Stranding'],
    ["Puedes recomendarme algo para jugar", 'Te recomiendo el videojuego Hades'],
    ["Me das una recomendacion de videojuego", 'Te recomiendo el videojuego Nier: Automata'],
    ["Tienes algun juego para compartir", 'Te recomiendo el videojuego Ghost of Tsushima'],
    ["Quiero jugar un videojuego", 'Te recomiendo el videojuego The Last of Us Part II'],
    ["Me recomiendas algun videojuego", 'Te recomiendo el videojuego Cyberpunk 2077'],
    ["Podrias sugerirme un juego", 'Te recomiendo el videojuego Assassins Creed Valhalla'],
    ["Que videojuego me sugieres", 'Te recomiendo el videojuego Final Fantasy VII Remake'],
    ["Tienes algun videojuego en mente", 'Te recomiendo el videojuego Ghost Recon Breakpoint'],
    ["Algun juego que me recomiendes", 'Te recomiendo el videojuego Genshin Impact'],
    ["Conoces algun buen videojuego", 'Te recomiendo el videojuego Days Gone'],
    ["Puedes recomendarme algo para jugar", 'Te recomiendo el videojuego Watch Dogs: Legion'],
    ["Me das una recomendacion de videojuego", 'Te recomiendo el videojuego Demons Souls (2020)'],
    ["Tienes algun juego para compartir", 'Te recomiendo el videojuego Marvels Spider-Man: Miles Morales'],
    ["Quiero jugar un videojuego", 'Te recomiendo el videojuego Demons Souls (2020)'],
    ["Me recomiendas algun videojuego", 'Te recomiendo el videojuego Doom Eternal'],
    ["Podrias sugerirme un juego", 'Te recomiendo el videojuego Assassins Creed Odyssey'],
    ["Que videojuego me sugieres", 'Te recomiendo el videojuego Resident Evil 3 (2020)'],
    ["Tienes algun videojuego en mente", 'Te recomiendo el videojuego The Outer Worlds'],
    ["Alg un juego que me recomiendes", 'Te recomiendo el videojuego Borderlands 3'],
    ["Conoces algun buen videojuego", 'Te recomiendo el videojuego Destiny 2'],
    ["Puedes recomendarme algo para jugar", 'Te recomiendo el videojuego Tom Clancys Rainbow Six Siege'],
    ["Me das una recomendacion de videojuego", 'Te recomiendo el videojuego Warframe'],
    ["Tienes algun juego para compartir", 'Te recomiendo el videojuego Control'],
    ["Quiero jugar un videojuego", 'Te recomiendo el videojuego The Witcher 3: Wild Hunt'],
    ["Me recomiendas algun videojuego", 'Te recomiendo el videojuego Celeste'],
    ["Podrias sugerirme un juego", 'Te recomiendo el videojuego Cuphead'],
    ["Que videojuego me sugieres", 'Te recomiendo el videojuego Dead Cells'],
    ["Tienes algun videojuego en mente", 'Te recomiendo el videojuego Hollow Knight'],
    ["Algun juego que me recomiendes", 'Te recomiendo el videojuego Ori and the Will of the Wisps'],
    ["Conoces algun buen videojuego", 'Te recomiendo el videojuego Stardew Valley'],
    ["Puedes recomendarme algo para jugar", 'Te recomiendo el videojuego Terraria'],
    ["Me das una recomendacion de videojuego", 'Te recomiendo el videojuego A Plague Tale: Innocence'],
    ["Tienes algun juego para compartir", 'Te recomiendo el videojuego Outer Wilds'],
]

# Arreglo que contiene las respuestas de agradecimiento para el usuario de parte del bot
agradecimientos = [
    ['Gracias', 'De nada'],
    ['Muchas gracias', 'Un placer ayudarte'],
    ['Muchisimas grcias', 'Descuida, es un placer'],
    ['gracias', 'Es un placer ayudar'],
    ['Gracias', 'De nada espero algo te haya ayudado'],
    ['Es todo Muchas gracias', 'Espero aver ayudado'],
    ['Gracias', 'De nada, ten un buen dia/noche'],
    ['muchas gracias', 'Fue un gusto ayudar'],
    ['Gracias', 'De nada, fue todo un placer'],
]

# Le decimos al chatbot que idioma debe usar (español)
levenshtein_distance = LevenshteinDistance('spanish')

# Entrenamos al chatbot con las respuestas a las posibles solicitudes del usuario
trainer = ListTrainer(chat)
for i in range(1):
    for saludo in saludos: trainer.train(saludo)
    for musica in recomendar_musica: trainer.train(musica)
    for pelicula in recomendar_pelicula: trainer.train(pelicula)
    for chiste in chistes: trainer.train(chiste)
    for agradecimiento in agradecimientos: trainer.train(agradecimiento)
    for videojuego in videojuegos: trainer.train(videojuego)
peticion = ""

print('\n\n\n')
print('Este es el Recomendabot\nTe puedo recomendar musica, Peliculas, Videojuegos, contarte un chiste, o darte un dato curioso')
print('Si quisiera terminar la interaccion, proceda a despedirse :D')

# Iniciamos la interaccion con el usuario y el chatbot
while levenshtein_distance.compare(Statement(peticion) , Statement('Adios') ) < 0.50:
    peticion = input('User: ' )
    respuesta = chat.get_response(peticion)
    print('Bot:', respuesta)

print('Gracias por usar el recomendabot\nTiene alguna sugerencia para mejorar el bot')
input('Tu: ')
print('Gracias, nos sirve mucho su sugerencia, que tenga un buen dia')
