"""final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('', views.page_index),
    path('about/', views.page_about),
    path('checklist/', views.page_checklist),
    path('futurework/', views.page_future_work),
    path('login/', views.page_login),
    path('signup/', views.page_signup),
    path('myjobs/', views.page_job_dashboard),
    path('user_logout/', views.user_logout),
    path('new_user_signup/', views.ajax_new_user),
    path('user_login/', views.ajax_user_login),
    path('save_job/', views.ajax_save_job),
    path('save_event/', views.ajax_save_event),
    path('delete_job/', views.ajax_delete_job),
    path('refresh_jobs/', views.ajax_refresh_job_list),
    path('check_urls/', views.ajax_refresh_urls)
]
