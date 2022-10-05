from email.policy import default
from secrets import choice
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Question(models.Model):
  # Atributos
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField("date published")

class Choices(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
