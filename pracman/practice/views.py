from django.utils import timezone
from rest_framework import generics


from pracman.views import FilterByUserMixin
from . import models
from . import serializers


class AppointmentsListView(FilterByUserMixin, generics.ListAPIView):

    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer


class FutureAppointmentsListView(FilterByUserMixin, generics.ListAPIView):

    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(at__gte=timezone.now())
