#!/usr/bin/env python3
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database
DATABASE_url = "sqlite:///doctors_data.db"
engine = create_engine(DATABASE_url)
Session = sessionmaker(bind=engine)

# define the ORM model


class Doctor:
    def __init__(self):
        self.doctors = {
            "first_name" : input("Enter your first name"),
            "last_name" : input("Enter your last name"),
            "specialization" : input("Enter your specialization"),
            "date of birth": input("Enter the date of birth in yy-mm-dd: "),
            "license": input("Enter your license: "),
            "sex" : input("Enter your sex: M or F"),
            "email": input("Enter your email: "),
            "phone number": input("Enter phone number: "),
            "home address": input("Enter home address")
        }

