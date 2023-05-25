from django.shortcuts import render, redirect
from .forms import CreatePostForm
from .models import Post


# Create your views here.
def home(request):
    post = list(Post.objects.all())
    total_post = len(post)
    post.reverse()

    return render(request, 'post/home.html', {'post': post, 'total_post': total_post})


def create_post(request):
    if request.method == 'POST':
        new_post = CreatePostForm(request.POST)
        if new_post.is_valid():
            new_post.save()
            return redirect('home')
    else:
        new_post = CreatePostForm()
        return render(request, 'post/create_post.html', {'new_post': new_post})