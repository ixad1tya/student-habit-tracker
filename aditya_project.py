import json
def load_data_file():
    try:
        f = open("habits_data.json", "r", encoding="utf-8")
        loded_data = json.load(f)
        f.close()
    except Exception:
        loded_data = {"habits": [], "logs": {}}
    return loded_data

def save_everything(d):
    with open("habits_data.json", "w", encoding="utf-8") as ff:
        json.dump(d, ff, indent=2)

def menu_print():
    print("\n=== Smart Student Habit Thingy (v1) ===")
    print("1. Add Habit")
    print("2. Edit Habit")
    print("3. View Habits")
    print("4. Log Habit Completion")
    print("5. Daily Report")
    print("6. Weekly Report")
    print("0. Exit")

def add_new_habit(db):
    habit_list = db["habits"]
    if len(habit_list) >= 15:
        print("Limit is 15 habits.")
        return
    
    name_of_habit = input("Enter habit name: ")
    hcat = input("Enter habit category: ")

    habit_list.append({"name": name_of_habit, "category": hcat})
    save_everything(db)
    print(f"Added '{name_of_habit}'.")

def edit_some_habit(db):
    hlist = db["habits"]
    if len(hlist) == 0:
        print("No habits.")
        return
    
    for i, h in enumerate(hlist, 1):
        print(f"{i}. {h['name']} ({h['category']})")
    
    try:
        num = int(input("Habit to edit: "))
        if num < 1 or num > len(hlist):
            print("Invalid.")
            return

        target = hlist[num - 1]
        
        new_n = input(f"New name (Enter to keep '{target['name']}'): ")
        new_c = input(f"New category (Enter to keep '{target['category']}'): ")

        if new_n != "":
            target["name"] = new_n
        if new_c != "":
            target["category"] = new_c

        save_everything(db)
        print("Updated.")

    except ValueError:
        print("Not a number.")

def view_all_habits(db):
    h = db["habits"]
    if len(h) == 0:
        print("No habits yet.")
    else:
        for i, hb in enumerate(h, 1):
            print(f"{i}. {hb['name']} ({hb['category']})")

def log_habit_day(db):
    h = db["habits"]
    if len(h) == 0:
        print("Add habits first.")
        return
    
    the_date = input("Enter date (YYYY-MM-DD): ")
    all_logs = []

    for one in h:
        done = input(f"Completed '{one['name']}'? (y/n): ").strip().lower()
        finished = (done == 'y')

        t_spent = 0
        if finished:
            spent_time = input("Hours spent: ")
            if spent_time:
                try:
                    t_spent = float(spent_time)
                except:
                    print("Invalid hours")

        all_logs.append({
            "name": one["name"],
            "completed": finished,
            "time": t_spent
        })
    
    db["logs"][the_date] = all_logs
    save_everything(db)
    print(f"Logged {the_date}.")

def show_daily_report(db):
    d = input("Date (YYYY-MM-DD): ")

    total_hb = len(db["habits"])
    if total_hb == 0:
        print("No habits.")
        return
    
    logs_today = db["logs"].get(d)
    
    if logs_today is None:
        print("No logs.")
        return
    
    completed = 0
    for entry in logs_today:
        if entry["completed"]:
            completed += 1
    
    missed = total_hb - completed
    pct = (completed / total_hb) * 100

    print(f"--- {d} ---")
    print("Total:", total_hb)
    print("Done:", completed)
    print("Missed:", missed)
    print(f"Consistency: {pct:.1f}%")

    if pct >= 80:
        print("Great")
    elif pct >= 50:
        print("Good")
    else:
        print("Improve")

def week_report(db):
    print("Enter 7 dates:")

    user_dates = []
    for i in range(7):
        dt = input(f"Date {i+1}: ")
        user_dates.append(dt)
    
    consistency_values = []

    for d in user_dates:
        total_h = len(db["habits"])
        logs = db["logs"].get(d)

        if logs is None or total_h == 0:
            percent = 0
        else:
            c = sum(1 for x in logs if x["completed"])
            percent = (c / total_h) * 100
        
        consistency_values.append(percent)
        print(f"{d}: {percent:.1f}%")

    if len(consistency_values) > 0:
        avg = sum(consistency_values) / len(consistency_values)
        print(f"Weekly average: {avg:.1f}%")

        if avg >= 80:
            print("Very consistent")
        elif avg >= 50:
            print("Not bad")
        else:
            print("Needs improvement")

def main_program():
    data_store = load_data_file()

    while True:
        menu_print()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_new_habit(data_store)
        elif choice == "2":
            edit_some_habit(data_store)
        elif choice == "3":
            view_all_habits(data_store)
        elif choice == "4":
            log_habit_day(data_store)
        elif choice == "5":
            show_daily_report(data_store)
        elif choice == "6":
            week_report(data_store)
        elif choice == "0":
            print("Bye")
            break
        else:
            print("option is invalid")

if __name__ == "__main__":
    main_program()