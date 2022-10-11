from django.urls import path
from . import views

urlpatterns = [
    path('greet/', views.say_hello),
    path('team/', views.team_view)
]