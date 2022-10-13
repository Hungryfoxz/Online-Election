from django.contrib import admin
from django.urls import path,include
from home import views


urlpatterns = [
    path("", views.index, name='home'),
    path("register/", views.register, name='register'),
    path("contact/", views.contact, name='contact'),
    path("login/", views.login, name='login'),
    path("about/", views.about, name='about'),
    path("developer/", views.developer, name='developer' ),
    path("vote/", views.vote, name='vote' ),
    path("SGlkZGVuIExvZ2luIFBhbmVs/", views.SGlkZGVuIExvZ2luIFBhbmVs, name='SGlkZGVuIExvZ2luIFBhbmVs'),
    path("success/", views.success, name='success')
]