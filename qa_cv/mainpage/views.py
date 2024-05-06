from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Post
from .forms import PostForm

def index(request):
    posts = Post.objects.all().order_by('-id')
    post = Post()
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        post.post = form.data['your_post']
        post.save()
    return render(request, "index.html", {"posts":posts, "form": form})