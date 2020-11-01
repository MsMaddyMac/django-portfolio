from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def all_blogs(request):
  # to get all blogs Blog.objects.all() to 
  # order by most recent date Blog.objects.order_by('-date')
  # to only allow a certain amount of blogs Blog.objects.order_by('-date')[:5] the number can be any amount you'd like
  # see how to create pagination with Django to allow five blogs to show and then have a see more button. Maybe even a search too.
  #  blogs_count = Blog.objects.count() use this if you are going to limit the amount of blogs rendered on the blogs page but want to still show an accurate count of how many blogs you've written in the all_blogs.html. See that page for how this is being rendered. You'd then have to send blogs_count into the render method 'blog_count': blog_count and then use that actual variable name to display in the file.
  blogs = Blog.objects.order_by('-date')   
  return render(request, 'blog/all_blogs.html', {'blogs': blogs})

def blog_detail(request, blog_id):
  # blog id will be passed into get_object_or_404() to pull Blog by that particular id and then pass it into blog_detail.html
  blog = get_object_or_404(Blog, pk=blog_id)
  return render(request, 'blog/blog_detail.html', {'blog': blog})  
