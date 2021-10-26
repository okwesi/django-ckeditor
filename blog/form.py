from blog.models import Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from ckeditor.widgets import  CKEditorWidget


#this field changes the usercreation form from its default and adds the name and email fields to the post form
# containing the richtext box
class PostForm(forms.ModelForm):
    body = forms.CharField(max_length=100,  widget= CKEditorWidget(attrs={'class': 'form-control'}))
#the widget changes the default styling to to a bootstrap default form stylings
    class Meta:
        model = Blog
        fields = ('body',)