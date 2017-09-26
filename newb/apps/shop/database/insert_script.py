from newb.apps.shop.models import Platform, Genre, Editor, Developer, VideoGame


platforms = [
    ['Windows', 'Microsoft', None],
    ['Xbox One', 'Microsoft', 2013],
    ['PS4', 'Sony', 2013],
    ['Switch', 'Nintendo', 2017]
]

for platform in platforms:
    Platform(name=platforms[0], constructor=platforms[1], release_year=platforms[2]).save()

genres = [
    ['Aventure'],
    ['Action'],
    ['Plate-forme'],
    ['Tir'],
    ['RPG'],
    ['Simulation'],
    ['Stratégie'],
    ['Sport'],
    ['Course']
]

for genre in genres:
    Genre(name=genres[0]).save()

# developers and editors can be the same
developers = [
    ['Ubisoft'],
    ['Cyanide'],
    ['EA Sports'],
    ['Bungie'],
    ['Activision'],
    ['Nintendo']
]

for developer in developers:
    Editor(name=developers[0]).save()
    Developer(name=developers[0]).save()

videogames = [
    ['Fifa 18', '29/09/17', [7], [0, 1, 2, 3], [2], [2], 'http://image.jeuxvideo.com/medias-sm/150529/1505290442-5803-jaquette-avant.png', 'FIFA 18 est un jeu de simulation de football sur PC, PS4 et Xbox One édité par Electronic Arts. Le mode aventure promet d\'être retravaillé en profondeur, tout en faisant suite à celui du précédent opus. Le championnat chinois fera également son apparition pour la première fois, sans oublier les traditionnelles améliorations apportées aux graphismes et au gameplay, ainsi que le retour de Pierre Ménès et Hervé Mathoux aux commentaires.', '50,99'],
    ['Destiny 2', '06/09/17', [3], [0, 1, 2], [4], [3], 'http://image.jeuxvideo.com/medias-sm/150607/1506071350-4107-jaquette-avant.jpg', 'Suite du premier opus du même nom réalisé par les créateurs de Halo, Destiny 2 est un FPS futuriste et intergalactique. Les joueurs peuvent y importer les personnages qu\'ils ont créés et améliorés dans le premier opus.', '44,99'],
    ['Super Mario Odyssey', '27/10/17', [2], [3], [5], [5], 'http://image.jeuxvideo.com/medias-sm/150166/1501664378-9988-jaquette-avant.jpg', 'La princesse Peach a été enlevée par Bowser. Pour la sauver, Mario quitte le royaume Champignon à bord de l\'Odyssey. Accompagné de Clappy, son chapeau vivant, il parcourra différents royaumes et fera tout pour vaincre, une nouvelle fois, terrible Bowser.', '44,90']
]

for videogame in videogames:
    VideoGame(title=videogames[0], release_date=videogames[1], genre=videogames[2], platform=videogames[3], editor=videogames[4], developer=videogames[5], picture=videogames[6], description=videogames[7], price=videogames[8]).save()