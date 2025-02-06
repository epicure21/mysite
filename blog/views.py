from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(status=1,published_date__lte=timezone.now())
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html',context)


def blog_single(request,pid):
    #post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, id=pid,status = 1, published_date__lte=timezone.now())
    last_post = Post.objects.filter(status=1 , published_date__lt = post.published_date,  published_date__lte=timezone.now()).order_by('-published_date').first()
    next_post = Post.objects.filter(status=1 , published_date__gt = post.published_date,  published_date__lte=timezone.now()).order_by('-published_date').first()
    post.counted_views += 1
    post.save()
    print("last" , last_post, "next", next_post)
    context = {'post': post, 'last_post': last_post, 'next_post': next_post}
    return render(request, 'blog/blog-single.html',context)