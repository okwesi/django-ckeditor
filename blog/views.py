from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .form import PostForm
from blog.models import Blog
from django.views.generic import ListView
# Create your views here

# this function creates the richtext form
def home(requests):
    # postform was created in the forms.py
    form = PostForm()
    return render(requests, "blog/home.html", {'form':form,})

# the view page to display the body of the blog
class Homeview(ListView):
    template_name="blog/view.html"
    context_object_name = 'view'
    def get_queryset(self):
        return Blog.objects.order_by('id')