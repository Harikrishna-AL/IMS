import datetime
from buildings.models import Ticket, Maintenance


def viewTickets() -> list:
    """Returns a list of tickets that are pending and are due for maintenance"""
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
            ticket_data["ticket_no"] = tickets[i].id
            ticket_data["MaintenancePeriod"] = maintenance_type
            ticket_data["MaintenanceDate"] = ticket_date
            ticket_data["RoomType"] = tickets[i].room.room_type
            ticket_data["Department"] = [
                dep_name.name for dep_name in tickets[i].department.all()
            ]
            data.append(ticket_data)
            # print(ticket_data)
        if (
            maintenance_type == "Weekly"
            and tickets[i].status == "Pending"
            and (datetime.date.today() - ticket_date).days % 7 == 0
        ):
            # data.append("weekly ")
            ticket_data["ticket_no"] = tickets[i].id
            ticket_data["MaintenancePeriod"] = maintenance_type
            ticket_data["MaintenanceDate"] = ticket_date
            ticket_data["RoomType"] = tickets[i].room.room_type
            ticket_data["Department"] = [
                dep_name.name for dep_name in tickets[i].department.all()
            ]
            data.append(ticket_data)
            # dates.append(ticket_date)
        if (
            maintenance_type == "Monthly"
            and tickets[i].status == "Pending"
            and (datetime.date.today() - ticket_date).days % 30 == 0
        ):
            # data.append("monthly ")
            ticket_data["ticket_no"] = tickets[i].id
            ticket_data["MaintenancePeriod"] = maintenance_type
            ticket_data["MaintenanceDate"] = ticket_date
            ticket_data["RoomType"] = tickets[i].room.room_type
            ticket_data["Department"] = [
                dep_name.name for dep_name in tickets[i].department.all()
            ]
            data.append(ticket_data)
        if (
            maintenance_type == "Quarterly"
            and tickets[i].status == "Pending"
            and (datetime.date.today() - ticket_date).days % 90 == 0
        ):
            # data.append("quarterly ")
            ticket_data["ticket_no"] = tickets[i].id
            ticket_data["MaintenancePeriod"] = maintenance_type
            ticket_data["MaintenanceDate"] = ticket_date
            ticket_data["RoomType"] = tickets[i].room.room_type
            ticket_data["Department"] = [
                dep_name.name for dep_name in tickets[i].department.all()
            ]
            data.append(ticket_data)
        # half_yearly
        if (
            maintenance_type == "Half Yearly"
            and tickets[i].status == "Pending"
            and (datetime.date.today() - ticket_date).days % 180 == 0
        ):
            # data.append("half yearly ")
            ticket_data["ticket_no"] = tickets[i].id
            ticket_data["MaintenancePeriod"] = maintenance_type
            ticket_data["MaintenanceDate"] = ticket_date
            ticket_data["RoomType"] = tickets[i].room.room_type
            ticket_data["Department"] = [
                dep_name.name for dep_name in tickets[i].department.all()
            ]
            data.append(ticket_data)
        if (
            maintenance_type == "Yearly"
            and tickets[i].status == "Pending"
            and (datetime.date.today() - ticket_date).days % 365 == 0
        ):
            # data.append("yearly ")
            ticket_data["ticket_no"] = tickets[i].id
            ticket_data["MaintenancePeriod"] = maintenance_type
            ticket_data["MaintenanceDate"] = ticket_date
            ticket_data["RoomType"] = tickets[i].room.room_type
            ticket_data["Department"] = [
                dep_name.name for dep_name in tickets[i].department.all()
            ]
            data.append(ticket_data)

    return data
