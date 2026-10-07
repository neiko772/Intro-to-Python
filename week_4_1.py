# Functions 
import time # This will import the time module, which provides various time-related functions
#! Functions without Parameters 
#? NASA Themed Examples 
def launch_countdown():
    print("T-minus 10 seconds and counting...")
    for i in range(10, 0, -2):
        print(i)
        time.sleep(1)
        print("Liftoff! The rocket has launched into space.")

launch_countdown()

#On Monday NASA Launches Rocket 1 
launch_countdown()

