from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.
@login_required
def feed_view(request):
    posts = Post.objects.all().order_by('_created_at')
    return render(request, 'posts/feed.html', {'posts': posts})

@login_required
def create_post_view(request):
    if request.method == 'POST':
        Post.objects.create(
            author = request.user,
            content = request.POST['content'],
            image = request.FILES.get('image')
        )
        return redirect('feed')
    return render(request, 'posts/create_post.html')
