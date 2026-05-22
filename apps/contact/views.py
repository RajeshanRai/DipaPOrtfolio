from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def contact_view(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # store message in DB
            from .models import ContactMessage
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            # send simple notification to site admin (console in dev)
            try:
                send_mail(
                    subject=f"New contact from {form.cleaned_data['name']}",
                    message=form.cleaned_data['message'],
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass
            sent = True
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form, 'sent': sent})
