import math
import time


def hello() -> None:
    """Prints 'Hello, World!'"""
    print("Hello, World!")


def hello_name(name: str) -> None:
    """
    Prints 'Hello, {name}'

    :param name: Name to be printed with the greeting
    """
    #  Alternatives:
    #  print("Hello,", name)
    #  print("Hello, " + name)
    #  print("Hello, {}".format(name))
    #  print("Hello, {name}".format(name=name))
    #  print("Hello, %s" % name)
    print(f"Hello, {name}")


def hello_six_names(name1, name2, name3, name4, name5=None, name6=None):
    print(f"Hello, {name1}, {name2}, {name3}, {name4}, {name5}, {name6}")


def hello_names(*names):
    """
    Prints 'Hello, {names}'

    :param names:
    :return:
    """
    for name in names:
        hello_name(name)


def shopping_list(**kwargs):
    """
    Prints a shopping list

    :param kwargs:
    :return:
    """
    print("Shopping list:")
    item_count = 0
    for item_name, item_quantity in kwargs.items():
        item_count += item_quantity
        print(f"- {item_name} {item_quantity} kg")

    print("Total:", item_count, "kg")


def sum_numbers(num: int) -> int:
    """
    Sums all numbers below given number (incl.)

    :param num: Number to process the sum for
    """
    result = 0
    for number in range(1, num + 1):
        result += number

    return result


def sum_numbers_py(num: int) -> int:
    """Same as sum_numbers() but using a Python built-in function"""
    return sum(range(1, num + 1))


def get_numbers_by_parity(num: int, parity: str) -> list:
    """
    Generated a list of odd or even numbers below given number

    :param num: All numbers will be below this number
    :param parity: "odd" or "even"
    :return: List with odd or even numbers below given number
    """
    result = []
    for number in range(1, num + 1):
        if parity == "odd" and number % 2 != 0:
            result.append(number)
        if parity == "even" and number % 2 == 0:
            result.append(number)

    return result


def is_prime(num: int) -> bool:
    """
    Checks whether the given integer is prime

    :param num: Integer to check
    :return: True if prime, False if not
    """
    # IDEA: Check the 'sieve of Eratosthenes' for further optimisation
    result = True
    for number in range(2, math.floor(math.sqrt(num))):
        if num % number == 0:
            result = False
            break

    return result


def get_primes(num: int) -> list:
    """
    Generates prime numbers below given number

    :param num: All numbers will be below this number
    :return: List with prime numbers below given number
    """
    result = []
    for number in range(1, num + 1):
        if is_prime(number):
            result.append(number)

    return result


if __name__ == "__main__":
    hello()
    print("----------------")

    hello_name("Alice")
    print("----------------")

    hello_six_names("Alice", "Bob", "Pepa", "Kaja", name6="Pavel", name5="Petr")
    print("----------------")

    hello_names("Franta", "Petr", "Max")
    print("----------------")

    shopping_list(bananas=5, strawberries=15, apples=66, yogurt=2)
    print("----------------")

    print(sum_numbers(10))
    start = time.time()
    print(sum_numbers(10000))
    end = time.time()
    print("For loop: ", end - start)
    start = time.time()
    print(sum_numbers_py(10000))
    end = time.time()
    print("Sum Function: ", end - start)
    print("----------------")

    print(get_numbers_by_parity(100, "even"))
    print(get_numbers_by_parity(100, "odd"))
    print(sum(get_numbers_by_parity(100, "even")))
    print(sum(get_numbers_by_parity(100, "odd")))
    print("----------------")

    # With no optimisations (no break, no sqrt()): ~ 20 000 under 10s
    # With break upon finding a divisor: ~ 60 000 under 10s
    # With break and a limitation of checked numbers: ~ 2 500 000 under 10s
    start = time.time()
    get_primes(2500000)
    end = time.time()
    print("2500000: ", end - start)
    print("----------------")
