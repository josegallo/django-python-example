from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    #the url will be 127.0.0.1/polls/ r^$ doesn't allow to add more
    # view.index is what we want display
    # name = "index" is the name of url
    url(r'^(?P<question_id>[0-9]+/$)', views.detail, name="detail"),
    #the url will be 127.0.0.1/polls/any_number, ex: 127.0.0.1/polls/1
    url(r'^(?P<question_id>[0-9]+/results$)', views.results, name="result"),
    #the url will be 127.0.0.1/any number/results/
    url(r'^(?P<question_id>[0-9]+/vote$)', views.vote, name="vote"),
    # 127.0.0.1/1/vote/
]