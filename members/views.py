from django.shortcuts import render, redirect
from buildings.models import Ticket
from buildings.models import Maintenance
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# importing HttpResponse
from django.shortcuts import render
from buildings.models import Ticket, Maintenance
from .forms import RegisterForm
from django.http import HttpResponse
import datetime


def register_member(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            messages.success(request, "Account was created for " + email)
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "members/authenticate/register.html", {"form": form})


def login_member(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        ## If user exists, login and redirect to agent page or customer page
        if user is not None:
            login(request, user)
            if user.is_agent:
                return redirect("agent")
            else:
                return redirect("customer")
        ## If user does not exist, redirect to login page
        else:
            print("Username OR password is incorrect")
            messages.info(request, "Username OR password is incorrect")
            return redirect("login")
    else:
        return render(request, "members/authenticate/login.html", {})


def logout_member(request):
    logout(request)
    return redirect("login")


def viewTickets():
    tickets = Ticket.objects.all()
    maintenance_ids = tickets.values_list("maintenance_id")
    maintenance = Maintenance.objects.all()
    dates = []
    data = []

    for i in range(len(maintenance_ids)):
        ticket_date = maintenance.values_list()[maintenance_ids[i][0] - 1][2]
        maintenance_type = maintenance.values_list()[maintenance_ids[i][0] - 1][4]
        # data.append(str(maintenance_ids[i][0]-1))
        ticket_data = {}
        if (
            maintenance_type == "Daily"
            and tickets[i].status == "Pending"
            and (datetime.date.today() - ticket_date).days % 1 == 0
        ):
            # data.append("daily ")
            ticket_data["MaintenancePeriod"] = maintenance_type
            ticket_data["MaintenanceDate"] = ticket_date
            ticket_data["Department"] = [
                dep_name.name for dep_name in tickets[i].department.all()
            ]
            ticket_data["Room"] = tickets[i].room
            data.append(ticket_data)
            # print(ticket_data)
        if (
            maintenance_type == "Weekly"
            and tickets[i].status == "Pending"
            and (datetime.date.today() - ticket_date).days % 7 == 0
        ):
            # data.append("weekly ")
            ticket_data["MaintenancePeriod"] = maintenance_type
            ticket_data["MaintenanceDate"] = ticket_date
            ticket_data["Department"] = [
                dep_name.name for dep_name in tickets[i].department.all()
            ]
            ticket_data["Room"] = tickets[i].room
            data.append(ticket_data)
            # dates.append(ticket_date)
        if (
            maintenance_type == "Monthly"
            and tickets[i].status == "Pending"
            and (datetime.date.today() - ticket_date).days % 30 == 0
        ):
            # data.append("monthly ")
            ticket_data["MaintenancePeriod"] = maintenance_type
            ticket_data["MaintenanceDate"] = ticket_date
            ticket_data["Department"] = [
                dep_name.name for dep_name in tickets[i].department.all()
            ]
            ticket_data["Room"] = tickets[i].room
            data.append(ticket_data)
        if (
            maintenance_type == "Quarterly"
            and tickets[i].status == "Pending"
            and (datetime.date.today() - ticket_date).days % 90 == 0
        ):
            # data.append("quarterly ")
            ticket_data["MaintenancePeriod"] = maintenance_type
            ticket_data["MaintenanceDate"] = ticket_date
            ticket_data["Department"] = [
                dep_name.name for dep_name in tickets[i].department.all()
            ]
            ticket_data["Room"] = tickets[i].room
            data.append(ticket_data)
        # half_yearly
        if (
            maintenance_type == "Half Yearly"
            and tickets[i].status == "Pending"
            and (datetime.date.today() - ticket_date).days % 180 == 0
        ):
            # data.append("half yearly ")
            ticket_data["MaintenancePeriod"] = maintenance_type
            ticket_data["MaintenanceDate"] = ticket_date
            ticket_data["Department"] = [
                dep_name.name for dep_name in tickets[i].department.all()
            ]
            ticket_data["Room"] = tickets[i].room
            data.append(ticket_data)
        if (
            maintenance_type == "Yearly"
            and tickets[i].status == "Pending"
            and (datetime.date.today() - ticket_date).days % 365 == 0
        ):
            # data.append("yearly ")
            ticket_data["MaintenancePeriod"] = maintenance_type
            ticket_data["MaintenanceDate"] = ticket_date
            ticket_data["Department"] = [
                dep_name.name for dep_name in tickets[i].department.all()
            ]
            ticket_data["Room"] = tickets[i].room
            data.append(ticket_data)

    return data


def agent(request):
    agent_data = viewTickets()
    return render(request, "members/agent/index.html", {"agent_data": agent_data})


def customer(request):
    return render(request, "members/customer/index.html")
