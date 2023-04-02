from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    # ---------- Auth URLs ------------- #

    path('home', views.home, name="home"),
    path('logout/', views.logout, name="logout"),
    path('profile', views.profile, name="profile"),
    path('doctor', views.doctor, name="doctor"),
    path('doctor/profile/<str:pk>', views.doc_profile, name="doc-profile"),
    path('first-aid', views.first_aid, name="first-aid"),
    path('first-aid/<str:pk>', views.first_det, name="first-det"),
    path('appointments', views.my_appointments, name="my-appointments"),
    path('latest-health-news', views.latest_news, name="latest-news"),
    path('latest-news/<str:pk>', views.latest_det, name="latest-det"),
    path('hospital-finder', views.hospital_finder, name="hospital-finder"),
    path('continue', views.cont, name="cont"),

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
    
    #  //////////////////////// ---------- Auth URLs End /////////////////////////// ---------- #



    # ---------- No Auth URLs ------------ #
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),

    # ---------------- PAssword RESET Views -------------- #
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_success/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
    # ---------------- Password ENd Views ---------------- #

    # ---------- No Auth URLs End --------- #
]
