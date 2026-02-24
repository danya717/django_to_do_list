from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from core.views import index, monday, tuesday, wednesday

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('monday', monday),
    path('tuesday', tuesday),
    path('wednesday', wednesday),
    path('creator', TemplateView.as_view(template_name='creator.html')),
]
