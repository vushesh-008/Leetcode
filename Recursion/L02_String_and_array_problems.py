from typing import List

def reverse_an_array(index: int, arr: List) -> None:
    """
    Reverses an array in-place using recursion.
    
    :param index: Current index from the start
    :param arr: Array to reverse
    :return: None (modifies array in-place)
    """
    if index == len(arr) //2:
        return 
    
    # Swap the elements
    arr[index], arr[len(arr) - index - 1] = arr[len(arr) - index - 1], arr[index]
    reverse_an_array(index + 1, arr)


def is_palindrome_string(s: str, left: int, right: int) -> bool:
    """
    Checks if a string is a palindrome using recursion.
    
    :param s: String to check
    :param left: Left pointer index
    :param right: Right pointer index
    :return: True if palindrome, False otherwise
    """
    # Base case: pointers meet or cross
    if left >= right:
        return True
    
    # If characters don't match, not a palindrome
    if s[left] != s[right]:
        return False
    
    # Check remaining substring
    return is_palindrome_string(s, left + 1, right - 1)


def is_palindrome_list(arr: List, index: int) -> bool:
    """
    Checks if a list/array is a palindrome using recursion.
    
    :param arr: List to check
    :param index: Current index from the start
    :return: True if palindrome, False otherwise
    """
    # Base case: reached middle
    if index >= len(arr) // 2:
        return True
    
    # If elements don't match, not a palindrome
    if arr[index] != arr[len(arr) - index - 1]:
        return False
    
    # Check remaining elements
    return is_palindrome_list(arr, index + 1)


if __name__ == "__main__":
    print("\n ----- Reverse an Array ------- \n")
    array = [1, 2, 3, 4, 5]
    print("Original Array:", array)
    reverse_an_array(0, array)
    print("Reversed Array:", array)
    
    array = ['a', 'b', 'c', 'd']
    print("Original Array:", array)
    reverse_an_array(0, array)
    print("Reversed Array:", array)
    
    print("\n ----- Check if String is Palindrome ------- \n")
    test_strings = ["racecar", "hello", "madam", "python", "noon"]
    for s in test_strings:
        result = is_palindrome_string(s, 0, len(s) - 1)
        print(f"'{s}' is palindrome: {result}")
    
    print("\n ----- Check if List is Palindrome ------- \n")
    test_lists = [
        [1, 2, 3, 2, 1],
        [1, 2, 3, 4, 5],
        ['a', 'b', 'a'],
        ['x', 'y', 'z']
    ]
    for lst in test_lists:
        result = is_palindrome_list(lst, 0)
        print(f"{lst} is palindrome: {result}")