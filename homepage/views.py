from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime
from .forms import ContactForm
from django.contrib import messages
from .models import Contact, Education, Profile
from django.conf import settings



def index(request):
    
    return render(request, 'homepage/homepage.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            user = Contact.objects.create(name=name, email=email, message=message)
            user.save()
            messages.success(request, 'Your message has been sent successfully!')
            form = ContactForm()
    else:
        form = ContactForm()
        
    return render(request, 'homepage/contact.html', {'form': form})


def education(request):
    education = Education.objects.all()
    context = {
        'education': education,
        'education_url':'active',
    }
    return render(request, 'homepage/education.html', context)


def profile(request):
    links = Profile.objects.all()
    context = {
        "links": links,
    }
    return render(request, 'homepage/homepage.html', context)


