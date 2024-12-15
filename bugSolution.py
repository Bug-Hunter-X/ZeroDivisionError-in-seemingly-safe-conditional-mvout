def function_with_uncommon_error_solution(a, b):
    if a == 0 and b == 0:
        return float('inf') # Or handle the case as appropriate
    elif a == 0:
        raise ZeroDivisionError("Division by zero")
    else:
        return a / b