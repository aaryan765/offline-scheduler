# tasks.py
# person 1

tasks = []
#priority function
def show_priority(priority):
    if priority == 1:
        return "★☆☆☆☆"
    elif priority == 2:
        return "★★☆☆☆"
    elif priority == 3:
        return "★★★☆☆"
    elif priority == 4:
        return "★★★★☆"
    elif priority == 5:
        return "★★★★★"    
#adds task
def add_task():
    print("Add a new task")
    name = input("Enter task name: ")
    date = input("Enter due date (YYYY-MM-DD): ")
    time = input("Enter due time (HH:MM): ")
    try:
        priority = int(input("Enter priority (1-5): "))
    except ValueError:
        print("Invalid input. Priority must be an integer between 1 and 5.")
        return
#check priority
    if priority < 1 or priority > 5:
        print("Invalid priority. Please enter a number between 1 and 5.")
        return
#give task a unique ID
    if len(tasks) == 0:
            task_id = 1
    else:
            task_id = tasks[-1]["id"] + 1
#create task  
    task = {
        "id": task_id,
        "name": name,
        "date": date,
        "time": time,
        "priority": priority,
        "status": "Pending"
    }
#add task to list
    tasks.append(task)

    print(f"Task '{name}' added successfully with ID {task_id}.")
    print(f"Priority: {show_priority(priority)}")
#this function displays all tasks in a formatted manner
def view_tasks():
     print("View all tasks")
     if len(tasks) == 0:
            print("No tasks available.")
            return
     for task in tasks:
        print("-----------------------------")
        print(f"ID: {task['id']}, Name: {task['name']}, Due: {task['date']} {task['time']}, Priority: {show_priority(task['priority'])}, Status: {task['status']}")
        print("-----------------------------")
#complete task function
def complete_task():
    print("Complete a task")
    if len(tasks) == 0:
        print("No tasks available.")
        return
    try:
        task_id = int(input("Enter the ID of the task to complete: "))
    except ValueError:
        print("Invalid input. Task ID must be an integer.")
        return
    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "Completed":
                print(f"Task '{task['name']}' is already completed.")
                return
            task["status"] = "Completed"
            print(f"Task '{task['name']}' marked as completed.")
            return
    print(f"No task found with ID {task_id}.")
#Delete task function
def delete_task():
     print("Delete a task")
     if len(tasks) == 0:
            print("No tasks available.")
            return
     try:
      task_id = int(input("Enter the ID of the task to delete: "))
     except ValueError:    
        print("please enter a number")
        return
     for task in tasks:
        if task["id"] == task_id:
                tasks.remove(task)
                print(f"Task '{task['name']}' deleted successfully.")
                return
     print (f"No task found with ID {task_id}.")
#changes the priority of a task
def change_priority():
    print("Change task priority")
    if len(tasks) == 0:
        print("No tasks available.")
        return
    try:
        task_id = int(input("Enter the ID of the task to change priority: "))
    except ValueError:
        print("Invalid input. Task ID must be an integer.")
        return
    for task in tasks:
        if task["id"] == task_id:
            try:
                new_priority = int(input("Enter new priority (1-5): "))
            except ValueError:
                print("Invalid input. Priority must be an integer between 1 and 5.")
                return
            if new_priority < 1 or new_priority > 5:
                print("Invalid priority. Please enter a number between 1 and 5.")
                return
            task["priority"] = new_priority
            print(f"Task '{task['name']}' priority changed to {show_priority(new_priority)}.")
            return
    print(f"No task found with ID {task_id}.")         
