from django.contrib import admin
from models import Keychain

for model in [Keychain]:
  admin.site.register(model)
