from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_post, name="view_post"),
    path("view_post/<slug>/", views.view_post, name='view_post'),
    path("thanks/", views.thanks, name="thanks"),
    path("post_list/<cat>/", views.post_list, name="post_list"),
    path("new_post/", views.new_post, name="new_post"),
]