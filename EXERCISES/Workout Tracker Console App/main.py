import datetime 

workouts = [ ]

def add_workout():
    date_str = input("Date (YYYY-MM-DD): ")
    try:
        date = datetime.datetime.strptime(date_str , "%Y-%m-%d")
    except ValueError:
        print("Invalid Date Format ,Please use YYYY-MM-DD.")
        return

    exercise = input("Enter the name of exercise : ")
    sets = int(input("Enter the no. of sets : "))
    reps = int(input("reps per set : "))
    if ( sets < 0 or reps < 0):
        print("Set and Rep must be positive")
        return
    workouts.append({"date": date_str , "exercise name": exercise , "Set":  sets , "Reps" : reps})
    print("Workout added successfully!\n")


def view_workout():
    if not workouts:
        print("No workouts recorded.")
        return

    print("\nWorkout Log:")
    for i,w  in enumerate(workouts , 1):
         print(f"{i}. Date: {w['date']}, Exercise: {w['exercise name']}, Sets: {w['Set']}, Reps: {w['Reps']} (Total reps: {w['Set'] * w['Reps']})")

def delete_workout():
    if not workouts:
        print("No workouts recorded. Nothing to delete.")
        return
    view_workout()
    idx = int(input("Enter the record number to delete: "))
    if ( idx < 1 or idx >len(workouts)):
        print("No record at that number")
        return
    del workouts[idx-1]
    print("Record Deleted!!!")

def view_stats():
    if not workouts:
        print("No workouts to analyze.")
        return

    total = len(workouts)
    print(f"Total workout : {total}")

    total_volume = sum(w['Set'] * w['Reps'] for w in workouts)
    print(f"Total volume (set*rep)= {total_volume}")

    avg_rep = total_volume / total   
    print(f"Average Reps : {avg_rep}")


print("📋 Workout Tracker")

while True:
    print( "\n1. Add Workout    2. View Workouts   3. Delete Workout  4. View Stats  5. Exit")
    try:
     userReply = int(input("\nEnter your choice: "))
    except ValueError:
     print("Invalid input ")
     continue

    if ( userReply == 1):
        add_workout()
    elif( userReply == 2):
        view_workout()
    elif( userReply == 3):
        delete_workout()
    elif( userReply == 4):
        view_stats()
    elif( userReply == 5):
        print("Good bye!!!")
        break
    else:
        print("Invalid Input")
