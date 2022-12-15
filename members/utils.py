# import datetime
# from buildings.models import Ticket, Maintenance
# from .forms import TicketFilter


# def viewTickets():
#     """Returns a list of tickets that are pending and are due for maintenance"""
#     tickets = Ticket.objects.all().filter(status="Pending")
#     ticketFilter = TicketFilter(request.GET, queryset=tickets)
#     return tickets
