def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    :param n: The position in the Fibonacci sequence.
    :return: The nth Fibonacci number.
    """
    if n<= 1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    n = 10
    print(f"Fibonacci of {n} is {fibonacci(n)}")