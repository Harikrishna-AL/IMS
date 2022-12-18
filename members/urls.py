from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("agent/", views.agent, name="agent"),
    path("customer/", views.customer, name="customer"),
    path("member_login/", views.login_member, name="login"),
    path("member_logout/", views.logout_member, name="logout"),
    path("register/", views.register_member, name="register"),
    path("detail_ticket/<int:ticket_id>/", views.detail_ticket, name="detail_ticket"),
    path("activity/", views.activity, name="activity"),
    path("detail_activity/<int:activity_id>/", views.detail_activity, name="detail_activity"),
    path("change_password/", views.change_password, name="change_password"),
    path("ticket/",views.create_ticket,name="ticket"),
    path("activity/activitycreation/", views.activityCreation,name="activitycreation")
 ]
