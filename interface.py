def show_menu():
    print("\n==========================")
    print("      TASK SCHEDULER")
    print("==========================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Change Priority")
    print("6. Search Task")
    print("7. Filter Tasks")
    print("8. Statistics")
    print("9. Exit")
    print("==========================")


def get_choice():
    try:
        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        print("Please enter a number.")
        return 0


def display_results(results):
    if len(results) == 0:
        print("No tasks found.")
        return

    print("\n--- Tasks ---")

    for task in results:
        print("--------------------------")
        print("ID:", task["id"])
        print("Name:", task["name"])
        print("Date:", task["date"])
        print("Time:", task["time"])
        print("Priority:", "★" * task["priority"])
        print("Status:", task["status"])

    print("--------------------------")


def get_keyword():
    return input("Enter keyword: ")


def get_filter():
    print("\n1. Filter by Priority")
    print("2. Filter by Status")
    print("3. Filter by Both")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid choice.")
        return None, None

    priority = None
    status = None

    if choice == 1:
        try:
            priority = int(input("Enter priority (1-5): "))
        except ValueError:
            print("Invalid priority.")
            return None, None

    elif choice == 2:
        status = input("Enter status (Pending/Completed): ")

    elif choice == 3:
        try:
            priority = int(input("Enter priority (1-5): "))
        except ValueError:
            print("Invalid priority.")
            return None, None

        status = input("Enter status (Pending/Completed): ")

    else:
        print("Invalid choice.")
        return None, None

    return priority, status