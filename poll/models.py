from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    qtext = models.CharField(max_length=200)
    pupdate = models.DateTimeField('date')

    def __str__(self):
        return self.qtext

    def was_published_recently(self):
        return self.pupdate >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
