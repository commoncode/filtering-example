from django.db.models.query import QuerySet

from pracman.querysets import UserRelatedQuerySetMixin


class PatientQuerySet(UserRelatedQuerySetMixin, QuerySet):
    user_filter_key = 'practice__doctors'


class AppointmentQuerySet(UserRelatedQuerySetMixin, QuerySet):
    user_filter_key = 'doctor'
