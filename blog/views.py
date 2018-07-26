from django.shortcuts import render
from . models import Category,Blog
from . forms import CommentForm
def homepage(request):
    context={'categories':Category.objects.order_by()}
    return render(request,'index.html',context)
def category(request,category_slug):
    cat=Category.objects.get(slug=category_slug)
    content={"categories":Category.objects.order_by('title'),
             "blogs":cat.blog_set.order_by('-pub_date'),
             "category":cat}
    return render(request,'category.html',content)
def blog(request,blog_id):
    blog=Blog.objects.get(pk=blog_id)
    form=CommentForm()
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.blog=blog
            comment.save()
            form=CommentForm()
    else:
        form=CommentForm()
    content = {"categories": Category.objects.order_by('title'),
               "blog":blog,
               'form':form}
    return render(request,'blog.html',content)

