import csv

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:leon2016@localhost/lecture4'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():

    # Flights
    # f = open("flights.csv")
    # reader = csv.reader(f)
    # for origin, destination, duration in reader:
    #     flight = Flight(origin=origin, destination=destination, duration=duration)
    #     db.session.add(flight)
    #     print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    # db.session.commit()

    # Passengers
    f = open("passengers.csv")
    reader = csv.reader(f)
    for n, f in reader:
        passenger = Passenger(name= n, flight_id = f)
        db.session.add(passenger)
        print(f"Added passenger {n}  y {f}.")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
