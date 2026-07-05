import time
from pyler import notifications


while True:
    print("Drink Water Reminder")
    print("It's time to drink water!")
    notifications.notify(title="Drink Water Reminder", message="It's time to drink water!") 
    time.sleep(3600)  # Wait for 1 hour (3600 seconds)

