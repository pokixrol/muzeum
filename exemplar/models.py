from django.db import models


def attachment_path(instance, exemplar_nazev):
    return "exemplar/" + str(instance.exemplar.id) + "/attachments/" + exemplar_nazev


class Odvetvi(models.Model):
    nazev = models.CharField(max_length=100, unique=True, null=True, blank=True,
                             verbose_name="Název uměleckého stylu",
                             help_text='Zadejte odvětví, do kterého spadá daný exemplář (Biologie, Historie)')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Odvětví'
        verbose_name_plural = 'Odvětví'

    def __str__(self):
        return self.nazev


class Exemplar(models.Model):
    nazev = models.CharField(max_length=50, verbose_name="Název")
    # datum_vytvoreni = models.DateField(blank=True, null=True, verbose_name="Datum vytvoření")
    popis = models.TextField(blank=True, null=True, verbose_name="Popis")
    odvetvi = models.ManyToManyField(Odvetvi, help_text='Vyberte odvětví, do kterého spadá tento exemplář.')

    class Meta:
        verbose_name = 'Exemplář'
        verbose_name_plural = 'Exempláře'

    def __str__(self):
        # return f"{self.nazev}, datum vytvoření: {str(self.datum_vytvoreni)}"
        return f"{self.nazev}, odvětví: {str(self.odvetvi)}"


class Priloha(models.Model):
    nazev = models.CharField(max_length=200, verbose_name="Název")
    soubor = models.FileField(upload_to=attachment_path, null=True, verbose_name="Soubor")
    exemplar = models.ForeignKey(Exemplar, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Příloha'
        verbose_name_plural = 'Přílohy'

    def __str__(self):
        return f"{self.nazev}"
