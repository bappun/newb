from django.db import models


class Platform(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    constructor = models.CharField(max_length=100, null=True, blank=True, verbose_name="Constructeur")
    release_year = models.IntegerField(null=True, blank=True, verbose_name="Année de sortie")


class Editor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")


class Developer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")


class VideoGame(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre")
    release_date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de sortie")
    description = models.TextField(null=True, verbose_name="Description")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Prix")
    picture = models.CharField(max_length=700, verbose_name="Jaquette")
    platform = models.ForeignKey('Platform')
    editor = models.ForeignKey('Editor')
    developer = models.ForeignKey('Developer')
    genre = models.ForeignKey('Genre')