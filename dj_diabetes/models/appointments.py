# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

from dj_diabetes.models import HatModel


class AppointmentTypes(HatModel):

    """
        AppointmentTypes
    """
    class Meta:
        verbose_name = 'Appointment Types'
        verbose_name_plural = 'Appointment Types'


@python_2_unicode_compatible
class Appointments(models.Model):

    """
        Appointments
    """
    user = models.ForeignKey(User)
    appointment_types = models.ForeignKey(AppointmentTypes)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    date_appointment = models.DateField(null=True)
    hour_appointment = models.TimeField(null=True)
    recall_one_duration = models.IntegerField(null=True)
    recall_two_duration = models.IntegerField(null=True)
    recall_one_unit = models.IntegerField(null=True)
    recall_two_unit = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Appointments'
        verbose_name_plural = 'Appointments'

    def show(self):
        return "Appointments %s %s %s %s %s" % (self.user_id, self.title,
                                                self.date_appointment,
                                                self.created, self.modified)

    def __str__(self):
        return "%s (date: %s)" % (self.title, self.date_appointment)
