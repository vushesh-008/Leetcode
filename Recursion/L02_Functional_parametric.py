def sum_of_numbers_parameterized(n: int, sum: int) -> None:
    """Sum of numbers from 1 to n using recursion technique with functional parameterization

        - Time complexity: O(n)
        - Space complexity: O(n)
        - Top-down approach

    Args:
        n (int): Number to sum from 1 to n

    Returns:
        None (print the sum of numbers from 1 to n)
    """

    if n == 0:
        print(f"sum: {sum}")
        return

    return sum_of_numbers_parameterized(n - 1, sum + n)


def sum_of_n_numbers(n: int) -> int:
    """Sum of numbers from 1 to n using recursion technique

        - Time complexity: O(n)
        - Space complexity: O(n)
        - Top-down approach

    Args:
        n (int): Number to sum from 1 to n

    Returns:
        int: Sum of numbers from 1 to n
    """

    if n == 0:
        return 0

    return n + sum_of_n_numbers(n - 1)


def fibonacci(n: int) -> int:
    """Fibonacci series using recursion technique

        - Time complexity: O(2^n)
        - Space complexity: O(n)
        - Top-down approach

    Args:
        n (int): Number to find fibonacci series

    Returns:
        int: Fibonacci series of n
    """

    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print(sum_of_numbers_parameterized(n=5, sum=0))  # Output: 15

    print(sum_of_n_numbers(n=5))  # Output: 15

    print(fibonacci(n=10))  # Output: 55
