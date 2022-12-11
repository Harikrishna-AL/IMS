import datetime
from buildings.models import Ticket, Maintenance


def viewTickets():
    """Returns a list of tickets that are pending and are due for maintenance"""
    tickets = Ticket.objects.all().filter(status="Pending")
    return tickets
