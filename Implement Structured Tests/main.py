def calculate_average(numbers):
    """
    Returns the average of a list of numbers.
    """

    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    if len(numbers) == 0:
        raise ValueError("List cannot be empty")

    for n in numbers:
        if not isinstance(n, (int, float)):
            raise TypeError("All elements must be numbers")

    return sum(numbers) / len(numbers)