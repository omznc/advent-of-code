from datetime import datetime
import os


def clearConsole():
    os.system("cls" if os.name in ("nt", "dos") else "clear")


clearConsole()

print(
    "Hey there! This is a simple script to run my finished Advent of Code solutions."
)

finished_days = sum(
    bool("." not in folder and os.path.isdir(folder)) for folder in os.listdir(".")
)


while True:
    tmp = input(
        f"What day's problem would you like to run? (1 - {finished_days}, blank for all): "
    )
    if len(tmp) == 0:
        choice = "all"
        break
    try:
        if int(tmp) > finished_days or int(tmp) < 1:
            clearConsole()
            print("Hmm, I don't think I've finished that one yet.")
            continue
        choice = tmp.zfill(2)
        break
    except ValueError:
        clearConsole()
        print("That's not a number. Try again.")

if choice != "all":
    current_time = datetime.now()
    print(f"---- Day {choice} ----")
    os.system(f"python3.10 ./{choice}/main.py")
    print(
        f"---- Runtime ----\n{(datetime.now() - current_time).total_seconds()} Seconds"
    )
else:
    current_time = datetime.now()
    for day in range(1, finished_days + 1):
        print(f"---- Day {str(day).zfill(2)} ----")
        os.system(f"python3.10 ./{str(day).zfill(2)}/main.py")
    print(
        f"---- Total Runtime ----\n{(datetime.now() - current_time).total_seconds()} Seconds"
    )
