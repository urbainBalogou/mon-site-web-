from django.shortcuts import render, get_object_or_404
from .models import Project, Skill, Formation, ContactInfo


def home(request):
    """Page d'accueil avec la liste des projets"""
    context = {
        'projects': Project.objects.all(),
        'skills': Skill.objects.all(),
        'formations': Formation.objects.filter(is_active=True),
        'contact_info': ContactInfo.get_instance(),
    }
    return render(request, 'portfolio/home.html', context)


def project_detail(request, slug):
    """Page de détail d'un projet"""
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project': project,
        'contact_info': ContactInfo.get_instance(),
    }
    return render(request, 'portfolio/project_detail.html', context)
