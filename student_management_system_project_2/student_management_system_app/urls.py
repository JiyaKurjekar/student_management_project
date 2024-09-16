from django.urls import path
from student_management_system_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("registration/", views.registration, name="registration"),
    path("data/", views.data, name="data"),
    path("login/", views.logged, name="login"),
    path("signup/", views.signup, name="signup"),
    path("remove/<int:id>/", views.remove, name="remove"),
    path("logout/", views.Log_Out, name="logout"),
    path('edit/<int:id>/', views.edit, name='edit')
]
