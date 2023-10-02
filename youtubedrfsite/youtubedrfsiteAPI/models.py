from django.db import models

class TranscribedText(models.Model):
    link = models.CharField(max_length=100)
    text = models.TextField()
