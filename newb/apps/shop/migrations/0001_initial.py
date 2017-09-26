# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 14:16
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150, verbose_name='Adresse')),
                ('postal_code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999)], verbose_name='Code postal')),
                ('city', models.CharField(max_length=100, verbose_name='Ville')),
                ('country', models.CharField(max_length=75, verbose_name='Pays')),
                ('phone', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Numéro de téléphone')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
            ],
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('constructor', models.CharField(blank=True, max_length=100, null=True, verbose_name='Constructeur')),
                ('release_year', models.IntegerField(blank=True, null=True, verbose_name='Année de sortie')),
            ],
        ),
        migrations.CreateModel(
            name='VideoGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titre')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Date de sortie')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='media/uploaded/img/shop/', verbose_name='Jaquette')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Prix')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Developer', verbose_name='Développeur')),
                ('editor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Editor', verbose_name='Éditeur')),
                ('genres', models.ManyToManyField(to='shop.Genre', verbose_name='Genres')),
                ('platforms', models.ManyToManyField(to='shop.Platform', verbose_name='Plateformes')),
            ],
        ),
    ]