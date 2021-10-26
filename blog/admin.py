from django.contrib import admin
from .models import Blog

# adding the  blog to the admin area
admin.site.register(Blog)
