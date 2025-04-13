#!/usr/bin/python3
"""Module that defines the MyList class, extending the base list class"""

class MyList(list):
    """A class that inherits from the built-in list class"""

    def print_sorted(self):
        """Prints the list in sorted order

        >>> my_list = MyList([3, 1, 2])
        >>> my_list.print_sorted()
        [1, 2, 3]
        """
        print(sorted(self))

# Example to show doctests running with the command
if __name__ == "__main__":
    import doctest
    doctest.testmod()
