from django.db import models

class Contact(models.Model):
  name=models.CharField(max_length=255)
  surname=models.CharField(max_length=255)
  description=models.TextField()
