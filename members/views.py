from django.shortcuts import render, redirect
from buildings.models import Ticket, Maintenance, Activity, ItemSwap
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (
    ActivityForm,
    TicketFilter,
    TicketForm,
    ChangePasswordForm,
    RegisterForm,
    ActivityFilter,
    EditProfile,
)
from .utils import get_ip_address, ticketData
from userlog.models import UserLog

# importing HttpResponse
from django.shortcuts import render
from django.middleware import csrf
from django.forms.models import (
    inlineformset_factory,
)
from rest_framework.views import APIView
from rest_framework.response import Response


def register_member(request):
    """Register a new user."""
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
    """Login a user."""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        ## If user exists, login and redirect to agent page or customer page
        if user is not None:
            ipAddress = get_ip_address(request)
            token = csrf.get_token(request)
            UserLog.objects.create(
                user=user, ipAddress=ipAddress, token=token, log_type="login"
            )
            login(request, user)
            if user.is_agent:
                return redirect("agent")
            else:
                return redirect("customer")
        ## If user does not exist, redirect to login page
        else:
            messages.info(request, "Username OR password is incorrect")
            return redirect("login")
    else:
        return render(request, "members/authenticate/login.html", {})


def change_password(request):
    """Change a user's password."""
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
    """Logout a user."""
    ipAddress = get_ip_address(request)
    token = csrf.get_token(request)
    UserLog.objects.create(
        user=request.user, ipAddress=ipAddress, token=token, log_type="logout"
    )
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def detail_ticket(request, ticket_id):
    """View details of a ticket."""
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, "members/tickets/details.html", {"ticket_data": ticket})


@login_required(login_url="login")
def agent(request):
    """View all tickets for an agent."""
    tickets = (
        Ticket.objects.all().filter(status="Pending").order_by("created_at").reverse()
    )
    ticketFilter = TicketFilter(request.GET, queryset=tickets)
    tickets = ticketFilter.qs
    return render(
        request,
        "members/agent/index.html",
        {"agent_data": tickets, "ticketFilter": ticketFilter},
    )


@login_required(login_url="login")
def customer(request):
    """View all tickets for a customer."""
    customer_name = request.user
    tickets = (
        Ticket.objects.all()
        .filter(status="Pending", created_by=customer_name)
        .order_by("created_at")
        .reverse()
    )
    ticketFilter = TicketFilter(request.GET, queryset=tickets)
    tickets = ticketFilter.qs

    return render(
        request,
        "members/customer/index.html",
        {"customer_data": tickets, "ticketFilter": ticketFilter},
    )


@login_required(login_url="login")
def activity(request):
    """View all activities."""
    activity = Activity.objects.all().order_by("closed_at").reverse()
    activityFilter = ActivityFilter(request.GET, queryset=activity)
    activity = activityFilter.qs
    return render(
        request,
        "members/activity/index.html",
        {"activity_data": activity, "activityFilter": activityFilter},
    )


@login_required(login_url="login")
def detail_activity(request, activity_id):
    """View details of an activity."""
    activity = Activity.objects.get(id=activity_id)
    swap_items = ItemSwap.objects.all().filter(activity=activity_id)
    return render(
        request,
        "members/activity/details.html",
        {"activity_data": activity, "item_data": swap_items},
    )


@login_required(login_url="login")
def create_ticket(request):
    """Create a new ticket."""
    if request.method == "POST":

        form = TicketForm(
            request.POST,
            initial={"created_by": request.user.pk, "room": request.user.room_no.pk},
        )
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
        form = TicketForm(
            initial={"created_by": request.user, "room": request.user.room_no}
        )
    return render(request, "members/customer/ticket.html", {"form": form})


@login_required(login_url="login")
def activityCreation(request):
    """Activity Creation Form"""
    ActivityFormSet = inlineformset_factory(
        Activity, ItemSwap, fields="__all__", extra=0, can_delete=False
    )

    if request.method == "POST":
        form = ActivityForm(request.POST or None)
        formset = ActivityFormSet(request.POST or None)
        if form.is_valid() and formset.is_valid():
            activity = form.save()
            ## Check if all the departments have completed the activity
            ## If yes, change the status of the ticket to completed
            ticket = Ticket.objects.get(activity=activity)
            if ticket.activity_set.all().count() == ticket.department.all().count():
                ticket.status = "Completed"
                ticket.save()
            for form in formset.forms:
                item = form.save(commit=False)
                item.activity = activity
                item.save()
            messages.success(request, "Activity Created Successfully")
            return redirect("activity")

        else:
            messages.error(request, "Activity Creation Failed")
            return redirect("activity")
    else:
        form = ActivityForm()
        formset = ActivityFormSet()
        return render(
            request,
            "members/agent/activityform.html",
            {"form": form, "formset": formset},
        )


class reportAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = ticketData()
        return Response(data)

def report(request):
    report_data = list(ticketData())
    # report_data = dumps(report_data)
    return render(request, "members/report/index.html")


@login_required(login_url="login")
def profile(request):
    form = EditProfile(request.POST or None, instance=request.user)
    userTickets = Ticket.objects.filter(created_by=request.user)
    if form.is_valid():
        form.save()
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")
        room_no = form.cleaned_data.get("room_no")

        # update tickets created by the user
        userTickets.update(room=room_no)
        userTickets.update(created_by=request.user)
        messages.success(request, "Profile Updated Successfully")

        return redirect("customer")
    return render(request, "members/customer/profile.html", {"form": form})
