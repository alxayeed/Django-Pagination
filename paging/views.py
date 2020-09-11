from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    all_posts = Post.objects.all()

    # creating Paginator object
    paginator = Paginator(all_posts, 5, 3)
    # getting current page number from request.GET.get dictionary
    page_number = request.GET.get('page')
    # all posts of the current page
    posts = paginator.page(page_number)

    context = {'posts': posts}
    return render(request, 'paging/home.html', context)
