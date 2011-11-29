"Do I want http://packages.python.org/CouchDB/client.html ?"
from django.contrib.auth.models import User
from django.db import models

class Couch(models.Model):
  "Connection to a Couch"
  pass

class Archive(models.Model):
  "A link to a transaction stored in a Couch"
  couch=models.ForeignKey(Couch)
  uuid=models.CharField(max_length=100)
  owner=models.ForeignKey(User)
