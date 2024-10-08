"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from adminlawyer import views

urlpatterns = [

    path('login', views.login, name='login'),
     path('logout', views.logout, name='logout'),
    path('login_check', views.login_check, name='login_check'),
    path('layout', views.layout, name='layout'),
    path('profile', views.profile, name='profile'),
    path('sidebar', views.sidebar, name='sidebar'),
    path('header', views.header, name='header'),
    path('footer', views.footer, name='footer'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('table', views.table, name='table'),
    path('form', views.form, name='form'),
    path('calendar', views.calendar, name='calendar'),

    path('add_doc', views.add_doc, name='add_doc'),
    path('add_member', views.add_member, name='add_member'),
    path('add_case', views.add_case, name='add_case'),
    path('add_client', views.add_client, name='add_client'),
    path('view', views.view, name='view'),
    
    path('view_cases', views.view_cases, name='view_cases'),
    path('view_doc', views.view_doc, name='view_doc'),
    path('view_feedback', views.view_feedback, name='view_feedback'),
    path('view_appointment', views.view_appointment, name='view_appointment'),
    path('view_member', views.view_member, name='view_member'),
    path('view_client', views.view_client, name='view_client'),
    
    path('client_store', views.client_store, name='client_store'),
    path('client_delete/<int:id>', views.client_delete, name='client_delete'),
    path('client_edit/<int:id>', views.client_edit, name='client_edit'),
    path('client_update/<int:id>', views.client_update, name='client_update'),

    path('lawyer_store', views.lawyer_store, name='lawyer_store'),
    path('lawyer_delete/<int:id>', views.lawyer_delete, name='lawyer_delete'),
    path('lawyer_edit/<int:id>', views.lawyer_edit, name='lawyer_edit'),
    path('lawyer_update/<int:id>', views.lawyer_update, name='lawyer_update'),

    path('case_store', views.case_store, name='case_store'),
    path('case_delete/<int:id>', views.case_delete, name='case_delete'),
    path('case_edit/<int:id>', views.case_edit, name='case_edit'),
    path('case_update/<int:id>', views.case_update, name='case_update'),
]
