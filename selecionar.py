from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:leon2016@localhost/lecture4'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    flights = Flight.query.all()

    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")


    flight = Flight.query.get(2)
    print(flight.origin)

    print("****")

    flights = Flight.query.filter(Flight.duration < 500).all()

    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

    print("-----")
    flights = Flight.query.filter(Flight.origin.like("P%")).all()

    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")


    print("-----")
    flights = Flight.query.filter(Flight.origin.in_(['Paris','Tokyo'])).all()

    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

    # JOIN
    print("-*-*-*")
    gg = db.session.query(Flight,Passenger).filter(Flight.id == Passenger.flight_id).all()

    for elem in gg:
        print(elem[0].origin,elem[0].destination,elem[1].name)


if __name__ == "__main__":
    with app.app_context():
        main()
