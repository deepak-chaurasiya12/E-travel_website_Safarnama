from django.urls import path
from . import views
urlpatterns=[
    path("", views.index, name="index"),
    path("Search", views.Search, name="Search"),
    path("terms", views.Search, name="terms"),
    path("logout", views.logout_request, name="logout"),

]
