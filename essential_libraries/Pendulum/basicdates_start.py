# Python Essential Libraries by Joe Marini course example
# Example file for Pendulum library
from datetime import datetime
import time
import pendulum

# TODO: create a new datetime using pendulum
# Create a new datetime using pendulum
dt = pendulum.datetime(2020, 2, 25, 23, 30, 0, 0)
print(dt)
# TODO: convert the time to another time zone
dt.in_timezone('US/Pacific')
print(dt.in_timezone('US/Pacific'))


# TODO: create a new datetime using the now() function


# TODO: Use the local function function


# TODO: Use today, tomorrow, yesterday


# TODO: create a datetime from a system timestamp
