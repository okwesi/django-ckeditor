from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    body = RichTextField(blank= True , null=True)
