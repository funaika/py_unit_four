
def even_or_odd(number):
    """
    Create a function that will tell if a number is even or odd. Use two if statements to do this.
    :param number: could be any positive or negative integer
    :return: either "x is an even number" or "x is an odd number"
    """
    if number % 2 == 0:
        return str(number) + " is an even number"

    if number % 2 != 0:
        return str(number) + " is an odd number"

def main():
    print(even_or_odd(11))


if __name__ == '__main__':
    main()