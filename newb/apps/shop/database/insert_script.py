from newb.apps.shop.models import Platform

platforms = [
    ['Windows', 'Microsoft', None],
    ['Xbox One', 'Microsft', 2013],
    ['PS4', 'Sony', 2013],
    ['Switch', 'Nintendo', 2017]
]

for platform in platforms:
    Platform(name=platforms[0], constructor=platforms[1], release_year=platforms[2]).save()

