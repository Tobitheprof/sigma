from django.urls import path
from . import views
urlpatterns = [
    # ---------- Auth URLs ------------- #

    path('home', views.index, name="home"),

    # ---------- Auth URLs End ---------- #



    # ---------- No Auth URLs ------------ #
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('regsiter', views.register, name="register"),

    # ---------- No Auth URLs End --------- #
]
