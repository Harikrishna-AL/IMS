# import datetime
from buildings.models import Ticket, Maintenance, Department

# from .forms import TicketFilter


# def viewTickets():
#     """Returns a list of tickets that are pending and are due for maintenance"""
#     tickets = Ticket.objects.all().filter(status="Pending")
#     ticketFilter = TicketFilter(request.GET, queryset=tickets)
#     return tickets
def get_ip_address(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def ticketData():
    department = {}
    x = Ticket.objects.all()
    departments = Department.objects.all().values_list("name", flat=True)
    filtered = len(x.filter(department__name="Medical").values())
    dates = []
    data = {}
    labels = []
    chartdata = []
    for ticket in x:
        dates.append(ticket.created_at)
    dates = set(dates)
    for date in dates:
        department = {}
        day_data = x.filter(created_at=date)
        for i in departments:
            chartdata.append(len(day_data.filter(department__name=i).values()))
            # department[i] = len(day_data.filter(department__name=i).values())
        data[date.strftime("%d/%m/%Y")] = {
            "labels": departments,
            "chartdata": chartdata,
        }

    return data
