# Generated by Django 4.0.3 on 2022-04-11 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mascotasapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conejos',
            old_name='raza',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='gatos',
            old_name='raza',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='perros',
            old_name='raza',
            new_name='color',
        ),
    ]