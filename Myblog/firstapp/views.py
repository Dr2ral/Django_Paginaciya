from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


# Create your views here.
def game(request):
    posts = Game.objects.all().order_by('title')
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'index.html', context)

