from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    #127.0.0.1/polls/ r^$ doesn't allow to add more
    # view.index is what we want display
    # name = "index" is the name of url
]