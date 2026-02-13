import numpy as np

def get_user_input():
    try:
        avg_sleep = float(input("Enter average sleep hours (per day): "))
        sleep_std = float(input("Enter sleep variability (std in hours): "))
        avg_steps = float(input("Enter average daily steps: "))
        steps_std = float(input("Enter steps variability (std): "))
        screen_avg = float(input("Enter average screen time hours/day: "))
        screen_std = float(input("Enter screen time variability (std): "))
        bedtime_std = float(input("Enter bedtime variability in minutes: "))
        return np.array([[avg_sleep, sleep_std, avg_steps, steps_std, screen_avg, screen_std, bedtime_std]])
    except:
        print("Invalid input. Please enter numeric values.")
        return None
