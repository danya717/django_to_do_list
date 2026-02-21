from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('monday', TemplateView.as_view(template_name='monday.html')),
    path('tuesday', TemplateView.as_view(template_name='tuesday.html')),
    path('wednesday', TemplateView.as_view(template_name='wednesday.html')),
    path('creator', TemplateView.as_view(template_name='creator.html')),
]
