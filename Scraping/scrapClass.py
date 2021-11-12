# def fact(n):
#     # Base Case:
#     if n == 1:
#         return 1
#     elif n == 0:
#         return 0
#     # Recursive Case
#     else:
#         return n * fact(n-1)
#
#
# print(fact(5))


def collatz(n):
    # Base Case
    if n == 1:
        return 0
    # Recursive Case 1
    elif n % 2 == 0:
        return 1 + collatz(n/2)
    # Recursive Case 2
    else:
        return 1 + collatz((3*n)+1)


print(collatz(10000000))
