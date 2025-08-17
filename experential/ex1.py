#!/usr/bin/env python


def greeting(name):
    greet = f"Hello {name}"
    return greet

def add_student_to_cohort(name, cohort):
    greet_message = greeting(name)
    add_student = f"{greet_message} is welcomed to Cohort {cohort}"
    print(add_student)

add_student_to_cohort("Frank", 2)
