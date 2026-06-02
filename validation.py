"""
Validation module for task management system.
Handles input validation for tasks and user inputs.
"""


def validate_task_name(task_name):
    """
    Validate that a task name is not empty and meets minimum length requirements.
    
    Args:
        task_name (str): The task name to validate
        
    Returns:
        tuple: (is_valid: bool, message: str)
    """
    if not task_name:
        return False, "Error: Task name cannot be empty."
    
    if len(task_name) < 1:
        return False, "Error: Task name must have at least 1 character."
    
    if len(task_name) > 200:
        return False, "Error: Task name cannot exceed 200 characters."
    
    return True, "Task name is valid."


def validate_task_id(task_id, tasks):
    """
    Validate that a task ID exists in the tasks list.
    
    Args:
        task_id (int): The task ID to validate
        tasks (list): List of task dictionaries
        
    Returns:
        tuple: (is_valid: bool, message: str)
    """
    if not isinstance(task_id, int):
        return False, "Error: Task ID must be an integer."
    
    if task_id < 1:
        return False, "Error: Task ID must be greater than 0."
    
    task_exists = any(task['id'] == task_id for task in tasks)
    if not task_exists:
        return False, f"Error: Task with ID {task_id} does not exist."
    
    return True, "Task ID is valid."


def validate_input_not_empty(user_input, field_name="Input"):
    """
    Validate that user input is not empty.
    
    Args:
        user_input (str): The user input to validate
        field_name (str): Name of the field being validated
        
    Returns:
        tuple: (is_valid: bool, message: str)
    """
    if not user_input or not user_input.strip():
        return False, f"Error: {field_name} cannot be empty."
    
    return True, "Input is valid."
