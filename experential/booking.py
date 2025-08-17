#!/usr/bin/env python3
import uuid


passenger_count = 0
ticket_price = 400.0
max_baggage_weight = 500.0
passenger_details = {}


def booking():
    global passenger_count, ticket_price, max_baggage_weight, passenger_details
    passanger_name = input("Enter your name: ")
    while True:
        baggage_weight = float(input("Enter your laggage weight: "))
        if baggage_weight > max_baggage_weight:
            print("Your laggage weight exceeded!!!\nThe maximun laggage weight is 500kg")
            continue
        else:
            break
    ticket_id = str(uuid.uuid4()).split('-')[0]
    passenger_count += 1
    passenger_details = {
        "ticket_id": ticket_id,
        "passenger_name": passanger_name,
        "baggage_weight": f"{baggage_weight} kg"
    }
    return passenger_details, passenger_count


def cancel(passenger_details):
    global passenger_count
    still_travelling = True
    user_choice = input(f"Are you still travelling? {passenger_details["passenger_name"]} (y/n): ")
    if user_choice == 'n':
        still_travelling = False
        passenger_count -= 1
    else:
        print("Have a safe journey")
    return passenger_details


def check_total_count():
    return passenger_count


"""

""" 


#print(booking())
print(booking())
print(cancel(passenger_details))
print(check_total_count())
