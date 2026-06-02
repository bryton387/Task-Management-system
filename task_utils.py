"""
Task utilities module for task management system.
Handles task operations: add, complete, view pending, and progress tracking.
"""


def add_task(tasks, task_name, task_description=""):
    """
    Add a new task to the tasks list.
    
    Args:
        tasks (list): List of task dictionaries
        task_name (str): Name of the task
        task_description (str): Description of the task (optional)
        
    Returns:
        dict: The newly created task
    """
    task_id = len(tasks) + 1 if tasks else 1
    
    new_task = {
        'id': task_id,
        'name': task_name,
        'description': task_description,
        'completed': False
    }
    
    tasks.append(new_task)
    return new_task


def mark_task_complete(tasks, task_id):
    """
    Mark a task as complete by task ID.
    
    Args:
        tasks (list): List of task dictionaries
        task_id (int): The ID of the task to mark complete
        
    Returns:
        dict or None: The completed task, or None if not found
    """
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            return task
    
    return None


def get_pending_tasks(tasks):
    """
    Get all pending (incomplete) tasks.
    
    Args:
        tasks (list): List of task dictionaries
        
    Returns:
        list: List of pending task dictionaries
    """
    return [task for task in tasks if not task['completed']]


def get_completed_tasks(tasks):
    """
    Get all completed tasks.
    
    Args:
        tasks (list): List of task dictionaries
        
    Returns:
        list: List of completed task dictionaries
    """
    return [task for task in tasks if task['completed']]


def get_progress(tasks):
    """
    Calculate and return task completion progress.
    
    Args:
        tasks (list): List of task dictionaries
        
    Returns:
        dict: Dictionary with total, completed, pending, and percentage
    """
    total = len(tasks)
    completed = len(get_completed_tasks(tasks))
    pending = len(get_pending_tasks(tasks))
    
    if total == 0:
        percentage = 0.0
    else:
        percentage = (completed / total) * 100
    
    return {
        'total': total,
        'completed': completed,
        'pending': pending,
        'percentage': round(percentage, 2)
    }


def display_tasks(tasks):
    """
    Display all tasks in a formatted manner.
    
    Args:
        tasks (list): List of task dictionaries
    """
    if not tasks:
        print("No tasks found.")
        return
    
    print("\n" + "="*60)
    print(f"{'ID':<5} {'Status':<10} {'Task Name':<30}")
    print("="*60)
    
    for task in tasks:
        status = "✓ Complete" if task['completed'] else "○ Pending"
        task_name = task['name'][:27] + "..." if len(task['name']) > 30 else task['name']
        print(f"{task['id']:<5} {status:<10} {task_name:<30}")
    
    print("="*60 + "\n")


def display_pending_tasks(tasks):
    """
    Display all pending tasks in a formatted manner.
    
    Args:
        tasks (list): List of task dictionaries
    """
    pending = get_pending_tasks(tasks)
    
    if not pending:
        print("No pending tasks.")
        return
    
    print("\n" + "="*60)
    print(f"{'ID':<5} {'Pending Tasks':<50}")
    print("="*60)
    
    for task in pending:
        task_name = task['name'][:47] + "..." if len(task['name']) > 50 else task['name']
        print(f"{task['id']:<5} {task_name:<50}")
    
    print("="*60 + "\n")
