from django.contrib.auth.models import AbstractUser
from django.db import models
from . import querysets


class Practice(models.Model):

    name = models.CharField(max_length=64)
    address = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Doctor(AbstractUser):

    practice = models.ForeignKey('practice.Practice', null=True, blank=True, related_name='doctors')

    class Meta:
        verbose_name_plural = 'Doctors'


class Patient(models.Model):

    name = models.CharField(max_length=128)
    practice = models.ForeignKey('practice.Practice')
    create_at = models.DateTimeField(auto_now_add=True)

    objects = querysets.PatientQuerySet.as_manager()

    def __str__(self):
        return self.name


class Appointment(models.Model):

    doctor = models.ForeignKey('practice.Doctor')
    patient = models.ForeignKey('practice.Patient')
    at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = querysets.AppointmentQuerySet.as_manager()

    class Meta:
        ordering = ('-at',)
        unique_together = (
            'doctor',
            'at'
        )

    def __str__(self):
        return '{} at {}'.format(self.patient, self.at)
