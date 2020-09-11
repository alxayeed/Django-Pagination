from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def home(request):
    # return HttpResponse('<h1 style="text-align:center">Home Page</h1>')
    all_posts = Post.objects.all()
    context = {'all_posts': all_posts}
    return render(request, 'paging/home.html', context)
