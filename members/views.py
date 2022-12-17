from django.shortcuts import render, redirect
from buildings.models import Ticket, Maintenance,Activity, ActivityItem
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# from .utils import viewTickets
from .forms import TicketFilter

# importing HttpResponse
from django.shortcuts import render
from .forms import RegisterForm, ChangePasswordForm,ActivityForm

def activityCreation(request):
    if request.method=='POST':
        form=ActivityForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ActivityForm()
    return render(request,"members/agent/activityform.html",{"form":form})
        
    

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
    return render(request, "members/customer/index.html")

@login_required(login_url="login")
def activity(request):
    activity = Activity.objects.all()
    return render(request, "members/activity/index.html", {"activity_data": activity})

@login_required(login_url="login")
def detail_activity(request,activity_id):
    activity = Activity.objects.get(id=activity_id)
    item=ActivityItem.objects.all()
    return render(request, "members/activity/details.html", {"activity_data": activity,"item_data":item})