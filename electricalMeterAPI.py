from flask import Flask
import json
import jsonpickle
from datetime import date

app = Flask(__name__)


class House():
    def __init__(self, address, wattsPerDay, electricalIssues, cablesPulled, electricalLocation, lightIssues) -> None:
        self.address = address
        self.wattsPerDay = wattsPerDay
        self.electricalIssues = electricalIssues
        self.cablesPulled = cablesPulled
        self.electricalLocation = electricalLocation
        self.lightIssues = lightIssues


class ServiceEvent():
    """
    A single technician goes to a single house.
    """
    
    def __init__(self, techName, houseName, date) -> None:
        self.techName=techName
        self.houseName=houseName
        self.date=date

ALL_HOUSES = [
    House("6060 N Ridge Ave", 100, True, 20, 'Pantry', 3),
    House("Closet House", 250, False, 15, 'Closet', 1),
    House("567 Cool Way", 250, False, 15, 'Basement', 0),
]

ALL_SERVICE_EVENTS = [
    ServiceEvent("Miguel","6060 N Ridge Ave", str(date.fromisoformat('2019-12-04')))
]


@app.route("/")
def hello_world():

    routes = [
        'houses',
        'events',
    ]

    route_lis = [f'<li><a href={route}>{route}</a></li>' for route in routes]
    route_lis = '\n'.join(route_lis)

    return f"""
    
    <p>Welcome to Electrical Meter website! Try:
    
    <ul>
    {route_lis}
    </ul>
    
    
    """


@app.route("/houses")
def houses():
    return jsonpickle.encode(ALL_HOUSES)


@app.route("/events")
def events():
    return jsonpickle.encode(ALL_SERVICE_EVENTS)