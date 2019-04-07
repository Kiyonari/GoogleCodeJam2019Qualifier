#! /usr/bin/python


def compute(nb, complementary):
    if "4" in str(nb):
        multiplier = len(str(nb)) - str(nb).index("4") - 1
        complementary += pow(10, multiplier)
        nb -= pow(10, multiplier)
        return compute(nb, complementary)
    return nb, complementary


def main():
    tries = int(input())
    for i in range(tries):
        nb = int(input())
        result, complementary = compute(nb, 0)
        print("Case #{}:".format(i + 1), result, complementary)


main()

