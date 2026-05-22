from django.shortcuts import render
from django.http import FileResponse, Http404
from django.conf import settings
from pathlib import Path

from .models import CVDownload


def home(request):
    version = request.GET.get('version', 'medium')

    notes = {
        'short': {
            'title': 'Professional Note',
            'lead': 'I am Dipa Rai, a mushroom biotech engineer turning living fungal systems into precise, playful research platforms.',
            'paragraphs': [
                'I craft cultivation workflows that feel like an artful lattice: controlled humidity, clean transfer, and reliable growth from lab bench to harvest.',
            ],
            'cta_text': 'Start a Conversation',
            'cta_link': '/contact/'
        },
        'medium': {
            'title': 'Professional Note',
            'lead': 'I combine mycology, automation, and data design to make mushroom science feel confident, creative, and repeatable.',
            'paragraphs': [
                'I design systems that translate fungal behavior into usable lab tools: sensor arrays, substrate maps, and SOPs that guide teams through every stage of a grow cycle.',
                'My projects connect sterile technique, strain selection, and environmental control in a compact, elegant workflow that supports both discovery and production.',
                'I work with growers, researchers, and innovators to move mycelium ideas from pilot scale toward impactful applications. Reach out through the contact page.'
            ],
            'cta_text': 'Collaborate on Growth',
            'cta_link': '/contact/'
        },
        'long': {
            'title': 'Professional Note',
            'lead': 'I am Dipa Rai, a biotechnology engineer shaping mushroom cultivation and experimental ecosystems with a pixelated sense of design.',
            'paragraphs': [
                'My work blends lab-grade rigor, mycelium insight, and simple automation to build cultivation systems that are resilient, measurable, and easy to follow.',
                'I help teams create reproducible substrate recipes, sterile propagation workflows, and lightweight data flows that make every harvest more predictable and more beautiful.',
                'Whether you are scaling production, refining a lab process, or launching a mushroom innovation, I consult on system design, pilot deployment, and thoughtful operational handoff.'
            ],
            'cta_text': 'Explore the Lab Story',
            'cta_link': '/contact/'
        }
    }

    note = notes.get(version, notes['medium'])
    return render(request, 'core/home.html', {
        'professional_note': note,
        'note_versions': ['short', 'medium', 'long'],
        'active_version': version
    })


def download_cv(request):
    try:
        ip = request.META.get('REMOTE_ADDR')
        ua = request.META.get('HTTP_USER_AGENT', '')[:512]
        CVDownload.objects.create(ip=ip, user_agent=ua)
        cv_path = Path(settings.BASE_DIR) / 'static' / 'core' / 'cv' / 'Dipa_Rai_CV.pdf'
        if not cv_path.exists():
            raise Http404()
        return FileResponse(open(cv_path, 'rb'), as_attachment=True, filename='Dipa_Rai_CV.pdf')
    except Exception:
        raise Http404()
