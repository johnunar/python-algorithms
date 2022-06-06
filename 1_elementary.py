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


def sum_numbers(num):
    result = 0
    for number in range(1, num + 1):
        result += number

    return result


def sum_numbers_py(num):
    return sum(range(1, num + 1))


def get_numbers(num, type):
    result = []
    for number in range(1, num + 1):
        if type == "odd" and number % 2 != 0:
            result.append(number)
        if type == "even" and number % 2 == 0:
            result.append(number)

    return result


def is_prime(num):
    result = True
    for number in range(2, num):
        if num % number == 0:
            result = False

    return result


def get_primes(num):
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
    print(sum_numbers(100000000))
    end = time.time()
    print("For loop: ", end - start)
    start = time.time()
    print(sum_numbers_py(10000))
    end = time.time()
    print("Sum Function: ", end - start)
    print("----------------")
    print(get_numbers(100, "even"))
    print(get_numbers(100, "odd"))
    print(sum(get_numbers(100, "even")))
    print(sum(get_numbers(100, "odd")))
    print("----------------")
    print(get_primes(50000))
