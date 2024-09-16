# Subsequence : A subsequence is a sequence that can be derived from another sequence by deleting some or no elements
# without changing the order of the remaining elements.

# Problem: Print all subsequences of a string


def print_subsequences(s: str, index: int, output: list):
    """Print all subsequences of a string

    Args:
        s (str): Input string
        index (int): Current index
        output (list): Output list
    """
    if index == len(s):
        print("".join(output))
        return

    # Pick the character
    output.append(s[index])
    print_subsequences(s, index + 1, output)
    output.pop()
    # Do not pick the character
    print_subsequences(s, index + 1, output)


def print_subsequences_with_sum_k(s: list, index: int, output: list, k: int) -> None:
    """Print all subsequences of a list with sum k

    Args:
        s (list): Input list
        index (int): Current index
        output (list): Output list
        k (int): Sum

    Returns:
        None
    """
    if index == len(s):
        if sum(output) == k:
            print(output)
        return

    # Pick the character
    output.append(s[index])
    print_subsequences_with_sum_k(s, index + 1, output, k)
    output.pop()
    # Do not pick the character
    print_subsequences_with_sum_k(s, index + 1, output, k)


def print_any_subsequence_with_sum_k(s: list, index: int, output: list, k: int) -> bool:
    """Print any subsequence with sum k

    Args:
        s (list): Input list
        index (int): Current index
        output (list): Output list
        k (int): Sum

    Returns:
        bool: True if subsequence is found, False otherwise
    """
    if index == len(s):
        if sum(output) == k:
            print(output)
            return True
        return False

    # Pick the character
    output.append(s[index])
    if print_any_subsequence_with_sum_k(s, index + 1, output, k):
        return True
    output.pop()
    # Do not pick the character
    return print_any_subsequence_with_sum_k(s, index + 1, output, k)


if __name__ == "__main__":
    s = "abc"
    print_subsequences(s, 0, [])

    s = [1, 1, 2, 3, 4, 2, 3, 4, 5, 6]
    k = 6
    print_subsequences_with_sum_k(s, 0, [], k)

    s = [1, 1, 2, 3, 4, 2, 3, 4, 5, 6]
    k = 6
    print_any_subsequence_with_sum_k(s, 0, [], k)
