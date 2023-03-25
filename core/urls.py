from django.urls import path
from . import views
urlpatterns = [
    # ---------- Auth URLs ------------- #

    path('home', views.home, name="home"),
    path('logout/', views.logout, name="logout"),
    path('profile', views.profile, name="profile"),
    path('appointment', views.appointment, name="appointment"),
    path('doctor', views.doctor, name="doctor"),
    path('doctor/profile/<str:pk>', views.doc_profile, name="doc-profile"),
    path('courses', views.courses, name="courses"),
    # ---------- Auth URLs End ---------- #



    # ---------- No Auth URLs ------------ #
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),

    # ---------- No Auth URLs End --------- #
]
