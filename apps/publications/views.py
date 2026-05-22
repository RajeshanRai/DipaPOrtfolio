from django.shortcuts import render
from .models import Publication

def pub_list(request):
    qs = Publication.objects.order_by('-year')
    return render(request, 'publications/list.html', {'publications': qs})
