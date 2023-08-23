import random


def challenge_function():
    A = random.randint(1, 9)
    B = random.randint(1, 9)
    C = A*B
    print("A =", A, "C =", C)
    while(C != 4):
        A = random.randint(1, 9)
        B = random.randint(1, 9)
        C = A * B
        print("A =", A, "C =", C)
    print("Success!", "A =", A, ", B =", B)
    return


challenge_function()