from django.shortcuts import render
from .models import Post


def blog(request):
    pots = Post.objects.all()
    return render(request, 'blog/blog.html', {'pots': pots})
