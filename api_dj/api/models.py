from django.db import models


class Documento(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True)
    expira = models.DateField()
    alerta1y = models.BooleanField()
    alerta6m = models.BooleanField()
    alerta3m = models.BooleanField()
    alerta1m = models.BooleanField()

    def __str__(self):
        return self.nombre

    def save(self, **kwargs):
        self.nombre = self.nombre.upper()
        super(Documento, self).save()

    class Meta:
        verbose_name_plural = "Documentos"
