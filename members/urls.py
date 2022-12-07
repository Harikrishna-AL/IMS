from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("agent/", views.agent, name="agent"),
    path("customer/", views.customer, name="customer"),
    path("login_member/", views.login_member, name="login"),
    path("logout_member/", views.logout_member, name="logout"),
    path("register_member/", views.register_member, name="register"),
    path("detail_ticket/<int:ticket_id>/", views.detail_ticket, name="detail_ticket"),
]
