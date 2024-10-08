from django.db import models
from django.urls import reverse
import uuid
from django.utils import timezone
from datetime import timedelta



class Destination(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50,
    )

    code_dest = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=5,

    )

    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False,
    )

    def get_absolute_url(self):
        return reverse('destination_detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
    
    def get_cruises(self):
        return self.cruises.all()  # Devuelve todos los cruceros asociados a este destino


class Cruise(models.Model):
    code = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50,
    )

    start_date = models.DateField( default= None , null=False)  # Fecha inicial
    duration = models.PositiveIntegerField(default=1)  # Duración en días, por defecto 1 día
    end_date = models.DateField(default= None, null=True, blank=True)  # Fecha final
    
    # El codigo que tiene se ha generado
    generated_code_check = models.BooleanField(
        default=False
    )

    # Relación con Destination (ForeignKey)
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name='cruises'  # Esto permite acceder a todos los cruceros desde un destino
    )

    def __str__(self):
        return self.code
    
    def save(self, *args, **kwargs):
    # Genera un código único si al crucero no se le ha generado
        if not self.generated_code_check:
            self.code = self.destination.code_dest + "-"+ str(uuid.uuid4())[:8]  # Generar un código único de 8 caracteres
            self.generated_code_check = True
        if self.start_date and self.duration:
            try:
                self.end_date = self.start_date + timedelta(days=self.duration)
            except:
                self.end_date = None
            
        super().save(*args, **kwargs)
