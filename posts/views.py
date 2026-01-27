from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.
@login_required
def feed_view(request):
    posts = Post.objects.all().order_by('_created_at')
    return render(request, 'posts/feed.html', {'posts': posts})
