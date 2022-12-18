# import datetime
# from buildings.models import Ticket, Maintenance
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
