from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nom')


class Platform(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nom')
    constructor = models.CharField(max_length=100, null=True, blank=True, verbose_name='Constructeur')
    release_year = models.IntegerField(null=True, blank=True, verbose_name='Année de sortie')


class Editor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nom')


class Developer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nom')


class VideoGame(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titre')
    release_date = models.DateTimeField(null=True, verbose_name='Date de sortie')
    genre = models.ForeignKey('Genre', verbose_name='Genre')
    platform = models.ForeignKey('Platform', verbose_name='Plateforme')
    editor = models.ForeignKey('Editor', verbose_name='Éditeur')
    developer = models.ForeignKey('Developer', verbose_name='Développeur')
    picture = models.CharField(max_length=700, verbose_name='Jaquette')
    description = models.TextField(null=True, verbose_name='Description')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Prix')


# we add some informations at the user model which already exist on django
class Customer(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=150, verbose_name='Adresse')
    postal_code = models.IntegerField(max_digits=5, verbose_name='Code postal')
    city = models.CharField(max_length=100, verbose_name='Ville')
    country = models.CharField(max_length=75, verbose_name='Pays')
    phone = models.IntegerField(max_digits=10, verbose_name='Numéro de téléphone')
