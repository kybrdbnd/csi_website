from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm



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
            for key, value in form.cleaned_data.items():
                print(key, value)
            subject = "message from csi website"
            mail_message = " %s sends this message %s having phone no. %s" % (
                name, message, phone)
            from_email = settings.EMAIL_HOST_USER
            to_email = [sender]
            send_mail(subject,
                      mail_message,
                      from_email,
                      to_email,
                      fail_silently=False)
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()
    return render(request, 'forms.html', {'form':form})


def events(request):
    return render(request, 'events.html', {})


def gallery(request):
    return render(request, 'gallery.html', {})


def team(request):
    return render(request, 'team.html', {})
