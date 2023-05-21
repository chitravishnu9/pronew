from django.urls import path
from hoo import views

urlpatterns = [
    path('',views.signup),
    path('home',views.home),
    path('newpassword',views.newpassword),
    path('logout',views.logout),


    path('register',views.register)
]