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


if __name__ == "__main__":
    hello()
    hello_name("Alice")
