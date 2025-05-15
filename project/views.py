from django.shortcuts import render
from .models import Service
# Create your views here.
def service(request):
    services = Service.objects.all()
    context = {
        "services": services,
    }
    return render(request, 'service.html', context)
