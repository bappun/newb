import sys
import os
import django

sys.path.append("/home/bachi/projects/newb/")
os.environ["DJANGO_SETTINGS_MODULE"] = "newb.settings"
django.setup()

if __name__ == '__main__':
    from newb.apps.shop.models import Platform, Genre, Editor, Developer, VideoGame

    platforms = [
        ['Windows', 'Microsoft', None],
        ['Xbox One', 'Microsoft', 2013],
        ['PS4', 'Sony', 2013],
        ['Switch', 'Nintendo', 2017]
    ]

    for platform in platforms:
        Platform(name=platform[0], constructor=platform[1], release_year=platform[2]).save()

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
        Genre(name=genre[0]).save()

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
        Editor(name=developer[0]).save()
        Developer(name=developer[0]).save()

    videogames = [
        ['Fifa 18', '2017-09-29', [Genre.objects.get(name='Sport')], [Platform.objects.get(name='Windows'), Platform.objects.get(name='Xbox One'), Platform.objects.get(name='PS4'), Platform.objects.get(name='Switch')], Editor.objects.get(name='EA Sports'), Developer.objects.get(name='EA Sports'), '/media/uploaded/img/shop/fifa_18.jpg', 'FIFA 18 est un jeu de simulation de football sur PC, PS4 et Xbox One édité par Electronic Arts. Le mode aventure promet d\'être retravaillé en profondeur, tout en faisant suite à celui du précédent opus. Le championnat chinois fera également son apparition pour la première fois, sans oublier les traditionnelles améliorations apportées aux graphismes et au gameplay, ainsi que le retour de Pierre Ménès et Hervé Mathoux aux commentaires.', 50.99],
        ['Destiny 2', '2017-09-06', [Genre.objects.get(name='Tir')], [Platform.objects.get(name='Windows'), Platform.objects.get(name='Xbox One'), Platform.objects.get(name='PS4')], Editor.objects.get(name='Activision'), Developer.objects.get(name='Bungie'), '/media/uploaded/img/shop/destiny_2.jpg', 'Suite du premier opus du même nom réalisé par les créateurs de Halo, Destiny 2 est un FPS futuriste et intergalactique. Les joueurs peuvent y importer les personnages qu\'ils ont créés et améliorés dans le premier opus.', 44.99],
        ['Super Mario Odyssey', '2017-10-27', [Genre.objects.get(name='Plate-forme')], [Platform.objects.get(name='Switch')], Editor.objects.get(name='Nintendo'), Developer.objects.get(name='Nintendo'), '/media/uploaded/img/shop/super_mario_odyssey.jpg', 'La princesse Peach a été enlevée par Bowser. Pour la sauver, Mario quitte le royaume Champignon à bord de l\'Odyssey. Accompagné de Clappy, son chapeau vivant, il parcourra différents royaumes et fera tout pour vaincre, une nouvelle fois, terrible Bowser.', 44.90]
    ]

    i=1
    for videogame in videogames:
        VideoGame(id=i, title=videogame[0], release_date=videogame[1], genres=videogame[2], platforms=videogame[3], editor=videogame[4], developer=videogame[5], picture=videogame[6], description=videogame[7], price=videogame[8]).save()
        i += 1
