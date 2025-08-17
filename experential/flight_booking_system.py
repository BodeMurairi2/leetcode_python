#!/usr/bin/env python3
import uuid


class Flight:
    ### Class that manage flight booking

    def __init__(self):
        self.passenger_names = []
        self.ticket_id = str(uuid.uuid4()).split('-')[0]
        self.total_weight = 125
        self.passenger_details = {}
        self.count = len(self.passenger_details)

    def register(self):
        name = input("Enter your names: ").upper()
        
        while True:
            baggage_weight = float(input("Enter your laggage weight"))
            if baggage_weight > self.total_weight:
                print("Your laggage weight exceeded!!!\nThe maximun laggage weight is 500kg")
                continue
            else:
                break

        self.passenger_details = {
        "ticket_id": self.ticket_id,
        "passenger_name": name,
        "baggage_weight": f"{baggage_weight} kg"
        }
        self.passenger_names.append(self.passenger_details)
        return self.passenger_details
    

    def passenger_count(self):
        return len(self.passenger_details)
    

    def cancel_flight(self):
        still_travelling = True
        name = input("Enter your name: ").upper()
        for passengers in self.passenger_details:
            if name == passengers["passenger_name"]:
                user_choice = input(f"Are you still travelling? {self.passenger_details["passenger_name"]} (y/n): ")
                if user_choice == 'n':
                    still_travelling = False
                    self.count = len(self.passenger_details) - 1
                    return "passenger removed successfully"
            else:
                return "Have a safe journey. Enjoy your flight!"

new_flight = Flight()

if __name__ == "__flight_booking_system__":
    new_flight.register()
    new_flight.passenger_count()
    new_flight.cancel_flight()
