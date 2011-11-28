from django.db import models
from django.contrib.auth.models import User

class Keychain(models.Model):
  user=models.OneToOneField(User)
#  private_key=
