from django.contrib import admin
from django.urls import path, include

from django.conf import settings

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", include("post.urls")),
    path("about", views.about, name="about"),
    path("contact", include("ContactForm.urls")),
]