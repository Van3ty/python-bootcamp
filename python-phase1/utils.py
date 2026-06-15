def calculate_statistics(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    avg_num = sum(numbers) / len(numbers)
    count = len(numbers)
    return {
        "max": max_num,
        "min": min_num,
        "average": avg_num,
        "count": count
    }

def is_even(num):
    return num % 2 == 0

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."