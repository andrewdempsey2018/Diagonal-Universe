from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("thanks", views.thanks, name="thanks"),
    path("post_list/<cat>/", views.post_list, name="post_list"),
    path("project_list2/", views.project_list2, name="project_list2"),
    path("old_post/<slug>/", views.old_post, name='old_post'),
]