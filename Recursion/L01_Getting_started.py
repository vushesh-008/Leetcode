from typing import List

def print_name_ntimes(count: int) -> None:
    """
    Prints the name "Vushesh" 5 times using recursion.
    
    :param count: Current count of how many times the name has been printed.
    :type count: int
    :return: None
    """
    if count == 5:
        return 

    print("Vushesh") 
    print_name_ntimes(count + 1)


def print_numbers_from_1_to_n(count: int, n: int) -> None:
    """
    Prints numbers from 1 to n using recursion.

    :param count: Current number to print.
    :type count: int
    :param n: Upper limit of numbers to print.
    :type n: int
    :return: None
    """
    if count > n:
        return

    print(count, end= " ")
    print_numbers_from_1_to_n(count + 1, n)

def print_numbers_from_n_to_1(count: int) -> None:
    """
    Docstring for print_numbers_from_n_to_1
    
    :param count: Current number to print.
    :type count: int
    :return: None
    """
    if count ==0:
        return 
    
    print(count, end= " ")
    print_numbers_from_n_to_1(count - 1)


def print_numbers_from_1_to_n_using_backtracking(count: int, n:int) -> None:
    """
    Docstring for print_numbers_from_1_to_n_using_backtracking
    
    :param count: Current number to print.
    :type count: int
    :param n: Upper limit of numbers to print.
    :type n: int
    """
    if count < 1:
        return 
    
    print_numbers_from_1_to_n_using_backtracking(count - 1, n )
    print(count, end= " ")

def print_numbers_from_n_to_1_using_backtracking(count: int, n: int) -> None:
    """
    Docstring for print_numbers_from_n_to_1_using_backtracking
    
    :param count: Current number to print.
    :type count: int
    :param n: Upper limit of numbers to print.
    :type n: int
    """
    if count > n:
        return 
    
    print_numbers_from_n_to_1_using_backtracking(count + 1, n)
    print(count, end= " ")


def sum_of_first_n_natutal_numbers(count: int, sum: int, n: int) -> None:
    """
    Docstring for sum_of_first_n_natutal_numbers
    
    :param count: Current count of natural numbers.
    :type count: int
    :param sum: Current sum of natural numbers.
    :type sum: int
    :param n: Upper limit of natural numbers.
    :type n: int
    """
    if count > n:
        print("sum : ", sum)
        return 
    
    sum += count
    sum_of_first_n_natutal_numbers(count + 1, sum, n)
    

def sum_of_first_n_natutal_numbers_in_place(count: int, sum: int, n: int, sum_array: List) -> None:
    """
    Docstring for sum_of_first_n_natutal_numbers_in_place
    
    :param count: Current count of natural numbers.
    :type count: int
    :param sum: Current sum of natural numbers.
    :type sum: int
    :param n: Upper limit of natural numbers.
    :type n: int
    :param sum_array: List to store the sum.
    :type sum_array: List
    """
    if count > n:
        sum_array.append(sum)
        return 
    
    sum += count
    sum_of_first_n_natutal_numbers_in_place(count + 1, sum, n, sum_array)


def sum_of_first_n_natutal_numbers_parametrized(count: int, sum: int, n: int) -> int:
    """
    Docstring for sum_of_first_n_natutal_numbers_parametrized
    
    :param count: Current count of natural numbers.
    :type count: int
    :param sum: Current sum of natural numbers.
    :type sum: int
    :param n: Upper limit of natural numbers.
    :type n: int
    :return: Sum of first n natural numbers.
    :rtype: int
    """
    if count > n:
        return sum
    
    sum += count
    return sum_of_first_n_natutal_numbers_parametrized(count + 1, sum, n)

if __name__ == "__main__":
    print("\n ----- Print Name 5 times ------- \n")
    print_name_ntimes(0)  # Print Name 5 times

    print("\n ----- Print Numbers in ascending order from 1 to n ------- \n")
    print_numbers_from_1_to_n(1, 5)  # Print numbers from 1 to n

    print("\n ----- Print Numbers in descending order from n to 1 ------- \n")
    print_numbers_from_n_to_1(5)  # Print numbers from n to 1

    print("\n ----- Print Numbers in ascending order from 1 to n using backtracking ------- \n")
    print_numbers_from_1_to_n_using_backtracking(5, 5)  # 

    print("\n ----- Print Numbers in descending order from n to 1 using backtracking ------- \n")
    print_numbers_from_n_to_1_using_backtracking(1, 5)  #

    print("\n ----- Sum of first n natural numbers ------- \n")
    sum_of_first_n_natutal_numbers(1, 0, 5)

    print("\n ----- Sum of first n natural numbers in place ------- \n")
    sum_array = []
    sum_of_first_n_natutal_numbers_in_place(1, 0, 5, sum_array)
    print("Sum stored in array: ", sum_array[0])

    print("\n ----- Sum of first n natural numbers returned ------- \n")
    result = sum_of_first_n_natutal_numbers_parametrized(1, 0, 5)
    print("Sum returned: ", result)