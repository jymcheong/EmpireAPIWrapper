"""This module performs technique1 on TARGET_HOST   """


def run(targethost="127.0.0.1"):
    """run(targethost="127.0.0.1")

    Executes the technique with targethost address as input. """
    print(targethost)
    return "completed on " + targethost


if __name__ == '__main__':
    run()