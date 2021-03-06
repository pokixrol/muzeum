# Generated by Django 4.0.4 on 2022-04-12 14:06

from django.db import migrations, models
import django.db.models.deletion
import exemplar.models


class Migration(migrations.Migration):

    dependencies = [
        ('exemplar', '0002_odvetvi_alter_exemplar_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priloha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=200, verbose_name='Název')),
                ('soubor', models.FileField(null=True, upload_to=exemplar.models.attachment_path, verbose_name='Soubor')),
                ('exemplar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exemplar.exemplar')),
            ],
        ),
    ]
