# Salary
import math

def main():
    start = input("start time HH:MM format: ")
    end = input("end time HH:MM format: ")

    print(start)
    print(end)

    start_hour, start_min = [int(i) for i in start.split(":")]
    end_hour, end_min = [int(i) for i in end.split(":")]

    print(start_hour, start_min)
    print(end_hour, end_min)

    hour = int(end_hour) - int(start_hour)
    minutes = abs(end_min-  start_min)

    print(hour)
    print(minutes)

main()
