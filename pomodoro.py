### Importing libraries ###
import osascript
import time

### Notification when pomodoro is finished ###
def notification_pomodoro_finished():
    display_notification = osascript.run('display notification "Here is a 5min break." with title "Pomodoro finished!" sound name "Glass"')

### Notification when break is finished ###
def notification_break_finished():
    display_notification = osascript.run('display notification "Back to work. Another pomodoro started." with title "Break finished!" sound name "Tink"')

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

    print("\nPomodoro finished! Here is a 5 min break.")

    countdown(break_timer)

    print("\nBreak finished!\n")
    notification_break_finished()

### Timer ###
def pomodoro(t):
    print("\nPomodoro started! Now focus on.")
    
    countdown(t) # countdown starts

    notification_pomodoro_finished() # when pomodoro finishes, a popup notification appears

    pomodoro_break() # 5min break

    pomodoro(t) # call the function itself recursively!

### Main function that will start the script ###
def main():
    ### Welcome message with time request ###
    print("Welcome to Pomodoro timer!")
    print("Please, select between 25 or 30 minutes.")

    while True:
        timer_selection = input("25/30?\n") # Requesting input ('25' or '30' expected)
        
        try:
            timer_selection = int(timer_selection)
        except ValueError:
            print("\nInvalid input. Please, select between 25 or 30 minutes.")
            continue
        if timer_selection == 25 or timer_selection == 30:
            break
        else:
            print("\nInvalid number. Select between 25 or 30 minutes.")
    
    timer_selection = timer_selection * 60 # Converting from minutes to seconds
    pomodoro(timer_selection) # Starting the timer 

main()