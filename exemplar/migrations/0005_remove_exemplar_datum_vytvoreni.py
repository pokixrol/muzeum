# Generated by Django 4.0.4 on 2022-05-30 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exemplar', '0004_alter_priloha_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exemplar',
            name='datum_vytvoreni',
        ),
    ]
