from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nom')

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nom')
    constructor = models.CharField(max_length=100, null=True, blank=True, verbose_name='Constructeur')
    release_year = models.IntegerField(null=True, blank=True, verbose_name='Année de sortie')

    def __str__(self):
        return self.name


class Editor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nom')

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nom')

    def __str__(self):
        return self.name


class VideoGame(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titre')
    release_date = models.DateField(null=True, blank=True, verbose_name='Date de sortie')
    genres = models.ManyToManyField('Genre', verbose_name='Genres')
    platforms = models.ManyToManyField('Platform', verbose_name='Plateformes')
    editor = models.ForeignKey('Editor', verbose_name='Éditeur', null=True, blank=True)
    developer = models.ForeignKey('Developer', verbose_name='Développeur')
    picture = models.ImageField(upload_to="media/uploaded/img/shop/", null=True, blank=True, verbose_name='Jaquette')
    description = models.TextField(null=True, verbose_name='Description')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Prix')

    def __str__(self):
        return self.title


# we add some informations at the user model which already exist on django
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=150, verbose_name='Adresse')
    postal_code = models.PositiveIntegerField(verbose_name='Code postal', validators=[MaxValueValidator(99999)])
    city = models.CharField(max_length=100, verbose_name='Ville')
    country = models.CharField(max_length=75, verbose_name='Pays')
    phone = models.PositiveIntegerField(verbose_name='Numéro de téléphone', validators=[MaxValueValidator(9999999999)])

    def __str__(self):
        return self.user


# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Customer.objects.create(user=instance)
#     instance.profile.save()
