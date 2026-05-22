from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    qs = Post.objects.order_by('-published')
    return render(request, 'blog/list.html', {'posts': qs})

def post_detail(request, slug):
    p = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/detail.html', {'post': p})
