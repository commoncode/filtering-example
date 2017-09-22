from rest_framework import serializers

from . import models


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Appointment
        fields = (
            'id',
            'doctor',
            'patient',
            'at',
            'created_at',
        )
