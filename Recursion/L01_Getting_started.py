def print_name(count: int, n: int) -> None:
    """Prints the name 5 times using recursion

    Args:
        count (int): Variable to keep track of the number of times the name is printed
        n (int): Number of times the name should be printed

    Returns:
        None
    """
    print("vushesh")
    if count == n:  # base case
        return

    count += 1
    print_name(count, n)  # recursive call


def print_numbers_from_n_to_1(count: int) -> None:
    """Prints numbers in descending order from n to 1 using recursion

    Args:
        count (int): _description_

    Returns:
        None
    """
    print(count)
    if count == 1:  # base case
        return

    print_numbers_from_n_to_1(count - 1)  # recursive call


def print_numbers_from_1_to_n(count: int, n: int) -> None:
    """Prints numbers in ascending order from 1 to n using recursion

    Args:
        count (int): Count variable to keep track of the number of times the number is printed
        n (int): Number till which the numbers should be printed

    Returns:
        None
    """

    print(count)
    if count == n:  # base case
        return

    print_numbers_from_1_to_n(count + 1, n)  # recursive call


if __name__ == "__main__":
    print("\n ----- Print Name 5 times ------- \n")
    print_name(1, 5)  # Print Name 5 times

    print("\n ----- Print Numbers in descending order from n to 1 ------- \n")
    print_numbers_from_n_to_1(5)  # Print numbers from n to 1

    print("\n ----- Print Numbers in ascending order from 1 to n ------- \n")
    print_numbers_from_1_to_n(1, 5)  # Print numbers from 1 to n
