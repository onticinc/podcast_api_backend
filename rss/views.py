from django.shortcuts import render
from .rss_info import item_results
# from .sandbox_3 import data
from math import ceil

# def rss_home(request):
#     return render(request, 'rss/home.html')

def home(request):
    page_size = 10
    page = int(request.GET.get('page'))
    offset = page*page_size
    total_pages = ceil(len(item_results)/page_size)
    print(total_pages)
    context = {
        'items': item_results[offset:offset+page_size],
        'total_pages': total_pages,
    }
    
    return render(request, 'rss/home.html', context)

def splash(request):
    return render(request, 'rss/rss_splash.html')













