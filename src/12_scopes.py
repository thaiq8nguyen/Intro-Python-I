# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12


def change_x(x):
    x = 99
    return x


# This prints 12. What do we have to modify in changeX() to get it to print 99?
print(change_x(x))


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        y = 999
        return y

    # return inner
    # inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999? Google "python nested function scope".
    print(inner())


outer()
