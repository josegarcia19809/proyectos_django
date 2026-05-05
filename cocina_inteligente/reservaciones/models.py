from django.db import models

# Create your models here.
from django.db import models

# 👤 Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


# 🪑 Mesa
class Mesa(models.Model):
    numero_mesa = models.IntegerField(unique=True)
    capacidad = models.IntegerField()

    def __str__(self):
        return f"Mesa {self.numero_mesa} ({self.capacidad} personas)"


# 📅 Reservación
class Reservacion(models.Model):
    ESTADOS = [
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('no_show', 'No Show'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    numero_personas = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS)

    def __str__(self):
        return f"{self.cliente} - {self.fecha} {self.hora_inicio}"


# ⭐ Reseña
class Resena(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    calificacion = models.IntegerField()

    def __str__(self):
        return f"{self.cliente} - {self.calificacion}"