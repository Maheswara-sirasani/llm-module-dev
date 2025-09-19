## write a function to find the maximum number in a list
def find_maximum(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number   


# Example usage
numbers = [3, 5, 1, 8, 2]       
max_number = find_maximum(numbers)
if max_number is not None:  
    print(f"The maximum number is: {max_number}")       
else:
    print("The list is empty, no maximum number found.")

