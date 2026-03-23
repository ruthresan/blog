from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path("", index, name="index"),
    path("post/detail/<str:slug>/",detail, name="detail"),
    # path("oldurl/", old_url_redirect, name='old_page'),
    # path("newurl/", new_url_view, name = "new_page"),
    path("contact/", contact_view, name = "contact"),
    path("about/",about_view, name = "about")
]