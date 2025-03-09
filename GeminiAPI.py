###############################################
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


###############################################
def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    Args:     numbers: A list of numbers.
    Returns:  The average of the numbers in the list, or None if the list is empty.
    """
    if not numbers:
        return None

    total = sum(numbers)
    average = total / len(numbers)
    print(f' Average={average}')
    return average


###############################################

def main():
    print("-- Start --")
    print_hi('PyCharm')
    print("-- End --")


###############################################
if __name__ == "__main__":
    main()
