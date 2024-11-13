# myapp/admin.py
from django.contrib import admin
from .models import UserProfile  # Impor model UserProfile setelah mendefinisikan model di models.py

admin.site.register(UserProfile)
