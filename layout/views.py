from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request, 'about.html', {})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data.get("sender")
            message = form.cleaned_data.get("message")
            name = form.cleaned_data.get("first_name")
            phone = form.cleaned_data.get("phone")
            # for key, value in form.cleaned_data.items():
            #     print(key, value)

            subject = "message from csi website"
            mail_message = " %s sends this message %s having phone no. %s \n\n Email id: %s" % (
                name, message, phone, sender)
            from_email = sender
            to_email = [settings.EMAIL_HOST_USER]
            send_mail(subject,
                      mail_message,
                      from_email,
                      to_email,
                      fail_silently=False)
    else:
        form = ContactForm()
    return render(request, 'forms.html', {'form': form})


def events(request):
    return render(request, 'events.html', {})


def gallery(request):
    return render(request, 'gallery.html', {})


def team(request):
    return render(request, 'team.html', {})
