# import datetime
from buildings.models import Ticket, Maintenance, Department, Activity, Building
import datetime

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
        print(ticket.room.floor.block.building.name)
    dates = set(dates)
    for date in dates:
        chartdata = []
        department = {}
        day_data = x.filter(created_at=date)
        for i in departments:
            chartdata.append(len(day_data.filter(department__name=i).values()))
        data[date.strftime("%d/%m/%Y")] = {
            "labels": departments,
            "chartdata": chartdata,
        }

    return data


def tableData():
    activities = Activity.objects.all()
    tickets = Ticket.objects.all()
    departments = Department.objects.all().values_list("name", flat=True)
    row_data = {}
    
    table_date_data = {}
    dates = []
    for ticket in tickets:
        dates.append(ticket.created_at)
    dates = set(dates)
    for date in dates:
        filter_ticket = tickets.filter(created_at=date)
        table_data = []
        for i in departments:
            filter_ticket = tickets.filter(department__name=i)
            service_time = 0
            for j in filter_ticket:
                created_at = j.created_at
                ticket_id = j.id
                closed_at = activities.filter(ticket_id=ticket_id).values_list("closed_at",flat=True)
                if closed_at:
                    closed_at = closed_at[0]
                    service_time += (closed_at - created_at).total_seconds()/60
                else:
                    service_time += 0
            row_data = {}   
            row_data['department'] = i
            row_data['opened']= len(tickets.filter(department__name=i).values())
            row_data['closed'] = len(tickets.filter(department__name=i, status="Completed").values())
            row_data['ServiceTime'] = service_time
            table_data.append(row_data)
        table_date_data[date.strftime("%d/%m/%Y")] = table_data

    return table_date_data

def buildingWiseData():
    buildings = Building.objects.all()
    departments = Department.objects.all().values_list("name", flat=True)
    departments = set(departments)
    tickets = Ticket.objects.all()
    dates = []
    data = {}
    for ticket in tickets:
        dates.append(ticket.created_at)
    dates = set(dates)    
    print(departments)
    
    for date in dates:
        tickets = tickets.filter(created_at=date)
        table_data = []
        for building in buildings:
            building_data = {}
            
            for department in departments:
                building_data[department] = len(tickets.filter(room__floor__block__building=building, department__name=department).values())
                row_data = {}   
                row_data['department'] = department
                row_data['opened']= len(tickets.filter(room__floor__block__building=building).filter(department__name=department).values())
                row_data['closed'] = len(tickets.filter(room__floor__block__building=building).filter(department__name=department, status="Completed").values())
                # row_data['ServiceTime'] = service_time
                row_data['building'] = building.name
                table_data.append(row_data)
        data[date.strftime("%d/%m/%Y")] = table_data
    return data
