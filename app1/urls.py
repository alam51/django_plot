from django.urls import path
from . import views


#URLConf
urlpatterns = [
    path('', views.homepage),
    path('hello/', views.say_hello),
    path('plotly/', views.test_plot),
]

