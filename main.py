"""
Task Management System - Main Program
Allows users to manage tasks, track progress, and mark tasks as complete.
"""

from task_utils import (
    add_task,
    mark_task_complete,
    get_pending_tasks,
    get_progress,
    display_tasks,
    display_pending_tasks
)
from validation import validate_task_name, validate_task_id


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*60)
    print("TASK MANAGEMENT SYSTEM")
    print("="*60)
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. View pending tasks")
    print("4. Mark task as complete")
    print("5. View progress")
    print("6. Exit")
    print("="*60)


def add_task_menu(tasks):
    """Handle adding a new task."""
    print("\n--- Add New Task ---")
    task_name = input("Enter task name: ").strip()
    
    is_valid, message = validate_task_name(task_name)
    if not is_valid:
        print(message)
        return
    
    task_description = input("Enter task description (optional): ").strip()
    
    new_task = add_task(tasks, task_name, task_description)
    print(f"\n✓ Task added successfully!")
    print(f"  Task ID: {new_task['id']}")
    print(f"  Task Name: {new_task['name']}")


def view_all_tasks(tasks):
    """Display all tasks."""
    print("\n--- All Tasks ---")
    if not tasks:
        print("No tasks found. Add a task to get started!")
    else:
        display_tasks(tasks)


def view_pending_tasks(tasks):
    """Display pending tasks."""
    print("\n--- Pending Tasks ---")
    display_pending_tasks(tasks)


def mark_complete_menu(tasks):
    """Handle marking a task as complete."""
    print("\n--- Mark Task as Complete ---")
    
    if not tasks:
        print("No tasks available.")
        return
    
    display_tasks(tasks)
    
    try:
        task_id = int(input("Enter the task ID to mark as complete: "))
    except ValueError:
        print("Error: Task ID must be a number.")
        return
    
    is_valid, message = validate_task_id(task_id, tasks)
    if not is_valid:
        print(message)
        return
    
    completed_task = mark_task_complete(tasks, task_id)
    if completed_task:
        print(f"\n✓ Task '{completed_task['name']}' marked as complete!")


def view_progress(tasks):
    """Display task progress."""
    print("\n--- Task Progress ---")
    
    if not tasks:
        print("No tasks to track.")
        return
    
    progress = get_progress(tasks)
    
    print(f"Total tasks: {progress['total']}")
    print(f"Completed: {progress['completed']}")
    print(f"Pending: {progress['pending']}")
    print(f"Progress: {progress['percentage']}%")
    
    # Display progress bar
    bar_length = 30
    filled = int((progress['percentage'] / 100) * bar_length)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"\n[{bar}] {progress['percentage']}%\n")


def main():
    """Main program loop."""
    tasks = []
    
    print("Welcome to the Task Management System!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_task_menu(tasks)
        elif choice == '2':
            view_all_tasks(tasks)
        elif choice == '3':
            view_pending_tasks(tasks)
        elif choice == '4':
            mark_complete_menu(tasks)
        elif choice == '5':
            view_progress(tasks)
        elif choice == '6':
            print("\nThank you for using Task Management System. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
