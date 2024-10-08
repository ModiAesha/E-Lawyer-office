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
from client import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('login_check', views.login_check, name='login_check'),
    path('hello', views.hello, name='hello'),
    path('layout', views.layout, name='layout'),
    path('contact', views.contact, name='contact'),
    path('appointment', views.appointment, name='appointment'),
    path('sidebar', views.sidebar, name='sidebar'),
    path('header', views.header, name='header'),
    path('footer', views.footer, name='footer'),
    path('home', views.home, name='home'),
    path('cases', views.cases, name='cases'),
    path('menu', views.menu, name='menu'),
    path('feedback_store', views.feedback_store, name='feedback_store'),
    # path('layout', views.layout, name='layout'),
    # path('sidebar', views.sidebar, name='sidebar'),
    # path('header', views.header, name='header'),
    # path('footer', views.footer, name='footer'),
    # path('dashboard', views.dashboard, name='dashboard'),
    # path('table', views.table, name='table'),
    # path('form', views.form, name='form'),
    # path('calendar', views.calendar, name='calendar'),
    # path('add_doc', views.add_doc, name='add_doc'),
    # path('add_member', views.add_member, name='add_member'),
    # path('add_case', views.add_case, name='add_case'),
    # path('add_client', views.add_client, name='add_client'),
    # path('view', views.view, name='view'),
    # path('delete/<int:id>', views.delete, name='delete'),
    # path('edit/<int:id>', views.edit, name='edit'),
    # path('update/<int:id>', views.update, name='update'),
    # path('view_cases', views.view_cases, name='view_cases'),
    # path('view_doc', views.view_doc, name='view_doc'),
    # path('view_feedback', views.view_feedback, name='view_feedback'),
    # path('view_appointment', views.view_appointment, name='view_appointment'),
    # path('view_member', views.view_member, name='view_member'),
    # path('view_client', views.view_client, name='view_client'),
    # path('login', views.login, name='login'),
    # path('store', views.store, name='store'),
    urlpatterns = [
    path("profile/<slug:slug>", ProfileDetailView.as_view(), name="profile"),
    path('ajax/load-states/', views.load_states, name='ajax_load_states'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-streets/', views.load_streets, name='ajax_load_streets'),
]
]
