#python 3.12.3

class Task:
    def __init__(self, description):
        """
        Initialize a Task object with a description and set the completed status to False.
        
        :param description: A string representing the task description.
        """
        self.description = description  # Description of the task
        self.completed = False  # Default status is not completed
        
    def mark_completed(self):
        # Mark the task as completed
        self.completed = True
        
    def change_description(self, new_description):
        # Change the task description
        self.description = new_description
    
    def display(self):
        # Print task details (description and status)
        if self.completed == True:
            status = "Completed"
        else:
            status = "Not completed"
        print(f"{self.description}\n{status}")
        
        
class ToDoList:
    def __init__(self):
        # Initialize an empty list of tasks
        self.task_list = []
    
    def add_task(self, description):
        # Add a new task to the list
        task = Task(description)
        self.task_list.append(task)
    
    def complete_task(self, description):
        # Mark a task as completed
        # Find the task by its description and mark it as completed
        for task in self.task_list:
            if task.description == description:
                task.mark_completed()
                print(f"Task '{description}' marked as completed.")
                return
        print(f"Task '{description}' not found.")
    
    def delete_task(self, description):
        # Delete a task by description
        for task in self.task_list:
            if task.description == description:
                self.task_list.remove(task)
                print(f"Task '{description}' removed from the list.")
                return
        print(f"Task '{description}' not found.")
              
    
    def view_tasks(self):
        # Display all tasks with their status
        for task in self.task_list:
            task.display() # Display each task using its own display method
            