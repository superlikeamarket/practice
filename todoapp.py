#python 3.7.1
# Define a function to add a task
def add_task(task_list):
    # Prompt user to enter a task 
    tasks_raw = input("What do you need to do? (Separate the tasks with '|')\nYou: ")
    # split the strings into multiple , if there're multiple tasks 
    tasks = tasks_raw.split('|')
    # Append the task(-s) to the tasks list
    for task in tasks:
        task = task.strip().lower()
        task = (task, False)
        task_list.append(task)

# Define a function to view all tasks
def view_tasks(task_list):
    # Display each task with its status (completed or not)
    print("\nYour to-do list:\n")
    if task_list == []:
        print("No tasks.\n")
    for task in task_list:
        if task[1]: 
          print (f"{task[0]}: Completed\n")
        else:
          print (f"{task[0]}: Not completed\n")

# Define a function to mark a task as completed
def complete_task(task_list):
    # Ask user which task to mark as completed
    done_tasks = input("What did you complete?\nYou: ")
    done_tasks = done_tasks.split('|')
    # Update the task status, but only one task if there's duplicates
    for done_task in done_tasks:
        done_task = done_task.strip().lower()
        for i, task in enumerate(task_list):
          if (task[0] == done_task) and (task[1] == False):
            task_list[i] = (task[0], True)
            break

# Define a function to delete a task
def delete_task(task_list):
    # Ask user which task to delete and split into individual tasks
    to_delete = input("What do you want to remove from the list?\n").split('|')
    to_delete = [task.strip().lower() for task in to_delete]

    for delete in to_delete:
        # Count completed and incomplete versions of the task
        completed_count = sum(1 for task in task_list if task[0] == delete and task[1])
        incomplete_count = sum(1 for task in task_list if task[0] == delete and not task[1])
        
        # Determine the status based on counts
        if completed_count > 0 and incomplete_count > 0:
            # If both completed and incomplete tasks exist, prompt the user once
            status_input = input("The task appears as both completed and incomplete. Do you want to delete the 'completed' or 'incomplete' task? ").strip().lower()
            status = True if status_input == 'completed' else False
        elif completed_count > 0:
            # Only completed tasks exist
            status = True
        elif incomplete_count > 0:
            # Only incomplete tasks exist
            status = False
        else:
            # If the task doesn't exist at all
            print(f"The task '{delete}' does not exist.")
            continue

        # Delete the task based on the determined status
        for i, task in enumerate(task_list):
            if task[0] == delete and task[1] == status:
                task_list.pop(i)
                print(f"Task '{delete}' removed from the list.")
                break

# Main function to run the application loop
def main():
    import json
    try:
        with open("todolist.txt", "r") as task_doc:
          task_list = json.load(task_doc) # Initialize an empty list for tasks
    except FileNotFoundError:
        task_list = []
    print("Hello! Welcome to your to-do list manager!")

    # Loop to keep the program running and prompt user actions
    while True:
        # Call appropriate functions based on user input
        command = input("What do you want to do?\nA – add task();\nB – view task(s)\nC – mark task(s) as completed;\nD – delete task(s);\nE – exit the program\nYou: ")
        if command.lower() == "a":
            add_task(task_list)
        elif command.lower() == "b":
            view_tasks(task_list)
        elif command.lower() == "c":
            complete_task(task_list)
        elif command.lower() == "d":
            delete_task(task_list)
        elif command.lower() == "e":
            with open("todolist.txt", "w") as task_doc:
                json.dump(task_list, task_doc)
            break
        else:
            print("Wrong input.\nThere is no such command.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()