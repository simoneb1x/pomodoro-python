### Importing libraries ###
import osascript
import time

### Notification when pomodoro is finished ###
def notification():
    display_notification = osascript.run('display notification "Feel free to take a 5min break." with title "Time finished!"')

### Timer ###
def pomodoro(t):
    print("Pomodoro started! Now focus on.")
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    notification()

### Main function that will start the script ###
def main():
    ### Welcome message with time request ###
    print("Welcome to Pomodoro timer!")
    print("Please, select between 25 or 30 minutes.")

    ### Requesting input ('25' or '30' expected)###
    timer_selection = int(input("25/30?\n"))

    ### Converting from minutes to seconds ###
    timer_selection = timer_selection * 60

    ### Starting the timer ###
    pomodoro(timer_selection)       

main()