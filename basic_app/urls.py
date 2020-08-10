from django.urls import path
from basic_app import views

# Template URLs!
app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('registration', views.registration, name="registration"),
    path('login', views.login, name="login"),
]

