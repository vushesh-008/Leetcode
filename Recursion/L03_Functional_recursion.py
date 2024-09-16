def revserse_array(arr: list, index: int) -> None:
    """Reverses the array using recursion

    Args:
        arr (list): Input array
        index (int): Index to start reversing from

    Returns:
        None: None
    """
    if index == len(arr) // 2:
        return

    swap_index = len(arr) - index - 1
    arr[index], arr[swap_index] = arr[swap_index], arr[index]

    revserse_array(arr, index + 1)


def check_palindrome(arr: list, index: int) -> bool:
    """Check if the array is palindrome or not

    Args:
        arr (list): Input array
        index (int): Index to start checking from

    Returns:
        bool: Boolean value indicating if the array is palindrome or not
    """
    if index == len(arr) // 2:
        return True

    if arr[index] != arr[len(arr) - index - 1]:
        return False

    return check_palindrome(arr, index + 1)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 13, 6, 7, 8, 9, 10]
    revserse_array(arr, 0)
    print(arr)

    arr = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    print(check_palindrome(arr, 0))

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(check_palindrome(arr, 0))
