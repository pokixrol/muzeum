# Generated by Django 4.0.4 on 2022-04-12 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exemplar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Odvetvi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(blank=True, help_text='Zadejte odvětví, do kterého spadá daný exemplář (Biologie, Historie)', max_length=100, null=True, unique=True, verbose_name='Název uměleckého stylu')),
            ],
            options={
                'verbose_name': 'Odvětví',
                'verbose_name_plural': 'Odvětví',
                'ordering': ['nazev'],
            },
        ),
        migrations.AlterModelOptions(
            name='exemplar',
            options={'verbose_name': 'Exemplář', 'verbose_name_plural': 'Exempláře'},
        ),
        migrations.AddField(
            model_name='exemplar',
            name='datum_vytvoreni',
            field=models.DateField(blank=True, null=True, verbose_name='Datum vytvoření'),
        ),
        migrations.AddField(
            model_name='exemplar',
            name='nazev',
            field=models.CharField(default='Historie', max_length=50, verbose_name='Název'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exemplar',
            name='popis',
            field=models.TextField(blank=True, null=True, verbose_name='Popis'),
        ),
        migrations.AddField(
            model_name='exemplar',
            name='odvetvi',
            field=models.ManyToManyField(help_text='Vyberte odvětví, do kterého spadá tento exemplář.', to='exemplar.odvetvi'),
        ),
    ]
