from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid
import datetime

@deconstructible
class Card(models.Model):
    low = 'low'
    medium = 'medium'
    high = 'high'

    task_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    taskid = models.UUIDField(primary_key=True, default=uuid.uuid1, unique = True)
    task_name = models.CharField(max_length=25)
    task_progress = models.IntegerField(default=0)
    task_time = models.DateTimeField(auto_now=True)
    task_deadline_date = models.DateField(auto_now=False, default=datetime.date(2020,1,1))
    task_deadline_time = models.TimeField(auto_now=False, default=datetime.time(11, 59, 59))
    task_deadline = models.DateTimeField(auto_now=False, null=True)
    task_urgency_choices = [
        (low, 'low'),
        (medium, 'medium'),
        (high, 'high'),
    ]
    task_urgency = models.CharField(max_length=6,choices=task_urgency_choices, default=low)
    task_status = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name


class SubCard(models.Model):
    # subtask_id = models.IntegerField()
    subtask_name = models.CharField(max_length=25)
    subtask_time = models.DateTimeField(auto_now=True)
    task_name = models.ForeignKey(Card , on_delete=models.CASCADE)
    subtask_state = models.BooleanField(default=False)

    class Meta:
        unique_together = ('subtask_name', 'task_name',)

    def str(self):
        return self.subtask_name

# class SubCard(models.Model):
#     subtask_id = models.IntegerField()
#     subtask_name = models.CharField(max_length=25)
#     subtask_state = models.IntegerField()



#     def __str__(self):
#         return self.subtask_name

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)