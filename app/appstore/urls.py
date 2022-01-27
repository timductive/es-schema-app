from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('install/<str:category>/<str:app>', views.install, name="install"),
    path('edit/<str:category>/<str:app>', views.edit, name="edit"),
    path('home/<str:category>/<str:app>', views.app_home, name="app_home")
]