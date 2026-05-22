# portfolio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skills/<int:num>/', views.skill_detail, name='skill_detail'),
    path('change-lang/<str:lang_code>/', views.change_lang, name='change_lang'),
]