from django.db import models
from django.contrib.auth.models import User
from gnupg import GPG

import os

GNUPG_HOME='gpg'

class Keychain(models.Model):
  user=models.OneToOneField(User)
  def gen(this):
    gpg=GPG(gnupghome=os.path.join(GNUPG_HOME,user.pk))
    input_data = gpg.gen_key_input(key_type="RSA", key_length=1024)
    key=gpg.gen_key(input_data)
