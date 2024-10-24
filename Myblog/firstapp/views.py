from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


# Create your views here.
def game(request):
    posts = Game.objects.all().order_by('title')
    page_number = request.GET.get('page')
    pages = request.GET.get('pages', 2)
    paginator = Paginator(posts, pages)
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj': page_obj,
        'pages': pages
    }
    return render(request, 'index.html', context)


#def choose_elem(request):
#    games = Game.objects.all()
#    page = request.GET.get('page', 1)
#    paginator = Paginator(games, page)
#
#    page_number = request.GET.get('page')
#    page_obj = paginator.get_page(page_number)
#
#    context = {
#        'page_obj': page_obj,
#        'page': page,
#    }
#    return render(request, 'index.html', context)