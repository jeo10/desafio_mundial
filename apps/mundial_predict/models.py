from django.db import models


class Seleccion(models.Model):
    codigo_seleccion = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Seleccion'
        verbose_name_plural = 'Seleccionnes'
        ordering = ['codigo_seleccion']

    def __str__(self):
        return self.nombre


class Partido(models.Model):
    codigo_partido = models.CharField(max_length=10, primary_key=True)
    fecha = models.DateField()
    horario = models.TimeField()
    estadio = models.CharField(max_length=25)
    fase = models.CharField(max_length=25)
    fase_desc = models.CharField(max_length=30, default=None)
    equipo1 = models.ForeignKey(Seleccion, related_name='equipo1', default=None, on_delete=models.CASCADE,
                                blank=True, null=True)
    equipo2 = models.ForeignKey(Seleccion, related_name='equipo2', default=None, on_delete=models.CASCADE,
                                blank=True, null=True)

    class Meta:
        verbose_name = 'Partido'
        verbose_name_plural = 'Partidos'


class Prediccion(models.Model):
    id_prediccion = models.AutoField(primary_key=True)
    codigo_partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    codigo_seleccion = models.ForeignKey(Seleccion, on_delete=models.CASCADE)
    goles = models.IntegerField(default=None, blank=True, null=True)
    puntos = models.IntegerField(default=None, blank=True, null=True)
