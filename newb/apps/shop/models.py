from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


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
    postal_code = models.CharField(max_length=5, verbose_name='Code postal')
    city = models.CharField(max_length=100, verbose_name='Ville')
    country = models.CharField(max_length=75, verbose_name='Pays')
    phone = PhoneNumberField(verbose_name='Numéro de téléphone')

    def __str__(self):
        return self.user


@receiver(post_save, sender=User)
def update_user_customer(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
    instance.customer.save()


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nom')
    email = models.EmailField(verbose_name='Adresse email')
    subject = models.CharField(max_length=150, verbose_name='Sujet')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return self.name + ' > [' + self.subject + "] " + self.message
