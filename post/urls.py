from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("thanks", views.thanks, name="thanks"),
    path("post_list/<cat>/", views.post_list, name="post_list"),
]