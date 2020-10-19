from django.db import models
from django.forms import ModelForm

# Create your models here.
class Invitation(models.Model):
    invitation_owner_name = models.CharField(max_length=90, verbose_name="Propietario de la invitación")
    email = models.EmailField(max_length = 128, unique=True)
    telephone = models.CharField(max_length=16)
    guest_names = models.CharField(max_length=256, verbose_name="Nombres de invitados")
    number_of_guests = models.IntegerField(verbose_name="Total de invitados")
    guests_confirmed = models.CharField(max_length=256, null=True, blank=True, verbose_name="Nombres confirmados")
    total_guests_confirmed = models.IntegerField(null=True, blank=True, verbose_name="Total de confirmados")
    is_RSVP = models.BooleanField(null=True, blank=True, verbose_name="¿Confirmó?")
    date_RSVP =models.DateField(null=True, blank=True, verbose_name="Fecha confirmación")

    def __str__(self):
        return str(self.guest_names)

    class Meta:
        verbose_name_plural = "Invitaciones"
