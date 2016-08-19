from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^lily$', views.LilyView.as_view(), name='lily'),
]
