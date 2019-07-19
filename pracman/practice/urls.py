from django.urls import path

from . import views


urlpatterns = [
    path("appointments/future", views.FutureAppointmentsListView.as_view()),
    path("appointments", views.AppointmentsListView.as_view()),
]
