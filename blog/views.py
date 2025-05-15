from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post, Category, Comment
from .forms import CommentForm

# Create your views here.
def blog_home(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, "blog/blog_home.html", {'posts': posts})


def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post=post)
            comment.save()
            return HttpResponseRedirect(request.path_info)
        
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': CommentForm(),
    }
    return render(request, "blog/blog_details.html", context)

    