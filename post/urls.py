from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("thanks", views.thanks, name="thanks"),
    path("post_list/<cat>/", views.post_list, name="post_list"),
    path("new_post/", views.new_post, name="new_post"),
    path("project_list/", views.project_list, name="project_list"),
    path("old_post/<slug>/", views.old_post, name='old_post'),
]