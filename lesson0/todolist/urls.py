from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from core.views import index, main, creator

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('monday', main, name='monday'),
    path('tuesday', main, name='tuesday'),
    path('wednesday', main, name='wednesday'),
    path('thursday', main, name='thursday'),
    path('friday', main, name='friday'),
    path('saturday', main, name='saturday'),
    path('sunday', main, name='sunday'),
    path('creator', creator),
]
