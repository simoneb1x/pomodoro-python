### Importing libraries ###
import osascript
import time

### Notification when pomodoro is finished ###
def notification():
    display_notification = osascript.run('display notification "Feel free to take a 5min break." with title "Time finished!"')

### Countdown ###
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


### 5 min break when pomodoro finishes ###
def pomodoro_break():
    break_timer = 300 # 5 mins

    countdown(break_timer)

### Timer ###
def pomodoro(t):
    print("\nPomodoro started! Now focus on.")
    
    countdown(t) # countdown starts

    notification() # when pomodoro finishes, a popup notification appears

    pomodoro_break() # 5min break

    pomodoro(t) # call the function itself recursively!

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