"""Views for Appstore."""

from django.shortcuts import render, redirect
from django.http import HttpResponse

from lib.appstore_lib import get_app_categories, install_app
from appstore.models import App

def index(request):
    apps = get_app_categories()
    return render(request, 'appstore.html', {
        'apps': apps,
    })


def app_home(request, category, app):
    """Load homepage for individual app."""
    return render(request, 'app_home.html', {
        'category': category,
        'app': app
    })


def install(request, category, app):
    """Loads installation page for given app. Installs app on POST."""

    if request.method == 'POST':
        install_app(category, app)
        save_app = App.objects.get_or_create(app_name=app, category=category)
        save_app.save()

        return redirect('app_home', category=category, app=app)
    

    return render(request, 'app_install.html', {
        'category': category,
        'app': app,
    })


def edit(request, category, app):
    """Edit page for given app."""

    if request.method == 'POST':
        install_app(category, app)

        return redirect('app_home', category=category, app=app)
    

    return render(request, 'app_edit.html', {
        'category': category,
        'app': app,
    })
