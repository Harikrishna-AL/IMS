from django.shortcuts import render, redirect
from buildings.models import Ticket, Maintenance,Activity, ActivityItem
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TicketFilter,TicketForm

# importing HttpResponse
from django.shortcuts import render
from .forms import RegisterForm, ChangePasswordForm


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
                print("Agent logged in")
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


def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Changed Successfully")
            return redirect("login")
        else:
            messages.error(request, "Password Change Failed")
    else:
        form = ChangePasswordForm(user=request.user)
        args = {"form": form}
        return render(request, "members/authenticate/change_password.html", args)


def logout_member(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def detail_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, "members/tickets/details.html", {"ticket_data": ticket})


@login_required(login_url="login")
def agent(request):
    # agent_data = viewTickets()
    tickets = Ticket.objects.all().filter(status="Pending")
    ticketFilter = TicketFilter(request.GET, queryset=tickets)
    tickets = ticketFilter.qs
    return render(
        request,
        "members/agent/index.html",
        {"agent_data": tickets, "ticketFilter": ticketFilter},
    )


@login_required(login_url="login")
def customer(request):
    customer_name = request.user
    # customer_data = Ticket.objects.filter(created_by=customer_name)
    tickets = Ticket.objects.all().filter(status="Pending",created_by=customer_name)
    ticketFilter = TicketFilter(request.GET, queryset=tickets)
    tickets = ticketFilter.qs
    
    return render(request, "members/customer/index.html", {"customer_data": tickets, "ticketFilter": ticketFilter})
@login_required(login_url="login")
def activity(request):
    activity = Activity.objects.all()
    return render(request, "members/activity/index.html", {"activity_data": activity})

@login_required(login_url="login")
def detail_activity(request,activity_id):
    activity = Activity.objects.get(id=activity_id)
    item=ActivityItem.objects.all()
    return render(request, "members/activity/details.html", {"activity_data": activity,"item_data":item})

@login_required(login_url="login")
def create_ticket(request):
    if request.method == "POST":

        form = TicketForm(request.POST,initial={'created_by':request.user, 'room':request.user.room_no.pk})
        if form.is_valid():
            form.save()
            message = form.cleaned_data.get("maintenance")
            room = form.cleaned_data.get("room")    
            department = form.cleaned_data.get("department")
            created_by = form.cleaned_data.get("created_by")
            comment = form.cleaned_data.get("message")
            messages.success(request, "Ticket Created Successfully")
            
            return redirect("customer")
            
    else:
        form = TicketForm(initial={'created_by':request.user, 'room':request.user.room_no})
    return render(request, "members/customer/ticket.html", {"form": form})