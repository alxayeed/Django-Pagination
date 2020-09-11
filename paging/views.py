from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    all_posts = Post.objects.all()

    # creating Paginator object
    paginator = Paginator(all_posts, 5, 3)
    # page = paginator.get_page()
    page_number = request.GET.get('page')
    # print(request.GET.get('page', 1))
    # print(request.GET.get.__doc__)
    print(page_number)
    posts = paginator.page(page_number)

    context = {'posts': posts}
    return render(request, 'paging/home.html', context)
