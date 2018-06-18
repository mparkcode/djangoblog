from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.http import HttpResponseForbidden
from .forms import BlogPostForm

# Create your views here.
def get_posts(request):
    posts = Post.objects.all()
    return render(request, "posts/blogposts.html", {'posts': posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "posts/postdetail.html", {'post': post})


def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = BlogPostForm()
        
    return render(request, 'posts/blogpostform.html', {'form': form})
        
        
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not(request.user == post.author or request.user.is_superuser):
        return HttpResponseForbidden()
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', post.pk)        
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'posts/blogpostform.html', {'form': form})
    