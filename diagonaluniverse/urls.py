from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("post.urls")),
    path("projects", include("projects.urls")),
    path("about", views.about, name="about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)