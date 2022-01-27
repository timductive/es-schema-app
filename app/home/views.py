from django.shortcuts import render

from django.http import HttpResponse

from appstore.models import App

def index(request):
    installed_apps = App.objects.all()
    return render(request, 'index.html', {
        'installed_apps': installed_apps
    })
