#!/usr/bin/python3
from datetime import datetime, timedelta


class Workout:
    '''Parent class
       Class that handles workout
       Argument: start_time, end_time, heart_rate, distance
    '''
    def __init__(self, start_time, end_time, heart_rate, distance):
        self.start_time = datetime.strptime(start_time, "%H:%M")
        self.end_time = datetime.strptime(end_time, "%H:%M")
        self.heart_rate = heart_rate
        self.distance = distance
    

    def get_duration(self):
        return (self.end_time - self.start_time).total_seconds() / 60  # Workout in minutes


class Running(Workout):
    '''
    Class to handle running
    '''
    
    def calculate_speed(self):
        return self.distance / (self.get_duration() / 60)  # speed in Km/h
    

    def calculate_pace(self):
        return self.get_duration() / self.distance if self.distance > 0 else 0  # pace min per km


    def get_summary(self):
        return (f"Running Workout:\nDuration: {self.get_duration():.2f} minutes\n"
                f"Distance: {self.distance} km\nSpeed: {self.calculate_speed():.2f} km/h\n"
                f"Pace: {self.calculate_pace():.2f} min/km\nHeart Rate: {self.heart_rate} bpm")



class Cycling(Workout):
    def calculate_speed(self):
        return self.distance / (self.get_duration() / 60)  # speed in km/h
    
    def get_summary(self):
        return (f"Cycling Workout:\nDuration: {self.get_duration():.2f} minutes\n"
                f"Distance: {self.distance} km\nSpeed: {self.calculate_speed():.2f} km/h\n"
                f"Heart Rate: {self.heart_rate} bpm")


while True:
    print("Choose a workout type")
    print("1.Cycling\n2.Running\n3.Quit")
    user_choice = input("Enter your choice").upper()
    if user_choice == "3" or user_choice == "QUIT":
        print("Good bye! Thanks for using our services")
        break

    start_time = input("Enter your start time in (HH:MM) ")
    end_time = input("Enter your end time in (HH:MM) ")
    distance = float(input("Enter the distance covered in (Km): "))
    heart_rate = float(input("Enter your heart rate in (bpm): "))
    
    if user_choice == "1" or user_choice == "CYCLING":
        workout = Cycling(start_time, end_time, heart_rate, distance)
    elif user_choice == "2" or user_choice == "RUNNING":
        workout = Running(start_time, end_time, heart_rate, distance)
    else:
        print("Invalid choice")
        continue

    print("Your Workout summary")
    print(workout.get_summary())
