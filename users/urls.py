from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('report/', views.viewTickets, name='index'),
    path("agent/", views.agent, name="agent"),
    path("customer/", views.customer, name="customer"),
]
