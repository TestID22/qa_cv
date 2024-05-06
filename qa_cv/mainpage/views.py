from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Post

def index(request):
    context = {
               "context": ['Author', "not an Author"]
               }
    posts = Post.objects.all()
    for post in posts:
        print(post)
    return render(request, "index.html", {"posts":posts})