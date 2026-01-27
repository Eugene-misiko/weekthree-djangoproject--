from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.
@login_required
def feed_view(request):
    posts = Post.objects.all().order_by('-created_at')
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

@login_required
def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})

@login_required
def like_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes.add(request.user)
    return redirect('feed')

from .models import Post, Comment

@login_required
def add_comment_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        Comment.objects.create(
            post=post,
            author=request.user,
            content=request.POST['content']
        )
        return redirect('post_detail', post_id=post_id)
    
@login_required
def unlike_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes.remove(request.user)
    return redirect('feed')

@login_required
def delete_comment_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author == request.user:
        comment.delete()

    return redirect('post_detail', post_id=comment.post.id)

@login_required
def edit_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # security check
    if post.author != request.user:
        return redirect('feed')

    if request.method == 'POST':
        post.content = request.POST['content']
        if request.FILES.get('image'):
            post.image = request.FILES.get('image')
        post.save()
        return redirect('post_detail', post_id=post.id)

    return render(request, 'posts/edit_post.html', {'post': post})

