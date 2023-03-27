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

    # ------------- Courses Views ---------- #
    path('courses', views.courses, name="courses"),
    path('courses/self-health', views.self_health, name="self-health"),
    path('courses/mental-health', views.mental_health, name="mental-health"),
    path('courses/care-giving', views.care_giving, name="care-giving"),
    path('courses/psycology', views.psycology, name="psycology"),
    path('courses/dental-health', views.dental_health, name="dental-health"),
    path('courses/physical-fitness-and-exercise', views.physical_fitness_and_exercise, name="physical-fitness-and-exercise"),
    path('courses/<str:slug>/', views.det, name="det"),


    # -------------- Courses Views End ------- #
    
    
    # ---------- Auth URLs End ---------- #



    # ---------- No Auth URLs ------------ #
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),

    # ---------- No Auth URLs End --------- #
]
