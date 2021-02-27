from django.urls import path
from . import views
from UI.views import home
urlpatterns = [
    path('', views.home, name="home"),
]