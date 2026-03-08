from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from core.views import index, monday, tuesday, wednesday, thursday, friday, saturday, sunday, creator

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('monday', monday),
    path('tuesday', tuesday),
    path('wednesday', wednesday),
    path('thursday', thursday),
    path('friday', friday),
    path('saturday', saturday),
    path('sunday', sunday),
    path('creator', creator),
]
