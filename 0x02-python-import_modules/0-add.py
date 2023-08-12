#!/usr/bin/python3
def add(a, b):
    from add_0 import add

    if __name__ == "__main__":
        a = 1
        b = 2
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

        Args:
            a: first integer
            b: second integer

        Returns:
            The return value. a + b
            def add(a, b)
            return (a + b)

