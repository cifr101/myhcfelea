def reverse_text(text):
    """Reverses the input string."""
    return text[::-1]

def calculator(a, b, operator):
    """Performs basic arithmetic operations."""
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operator"
