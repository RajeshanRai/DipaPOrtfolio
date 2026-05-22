from django.shortcuts import render, get_object_or_404
from .models import Project

def project_list(request):
    qs = Project.objects.all()
    return render(request, 'projects/list.html', {'projects': qs})

def project_detail(request, slug):
    p = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/detail.html', {'project': p})
