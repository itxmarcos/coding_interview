def binary_search(array, value):
    # Define the lower and upper bounds
    lower = 0
    upper = len(array) - 1

    # Loop until we find the value
    while lower <= upper:
        # Calculate the middle point
        middle = (lower + upper) // 2

        # If the middle point is our value, return True
        if array[middle] == value:
            return True

        # If the value is larger than our middle point, search
        # the left half of the array
        elif array[middle] < value:
            lower = middle + 1

        # If the value is smaller than our middle point, search
        # the right half of the array
        else:
            upper = middle - 1

    # Return False if we never find the value
    return -1

array = [1, 2, 3, 4, 5, 6, 7, 8]
value = 7
binary_search(array, value)
