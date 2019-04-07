#! /usr/bin/python


def compute(path_lydia):
    path = ""
    for c in path_lydia:
        if c == "E":
            path += "S"
        else:
            path += "E"
    return path


def main():
    tries = int(input())
    for i in range(tries):
        size = int(input())
        path_lydia = input()
        path = compute(path_lydia)
        print("Case #{}: {}".format(i + 1, path))


main()
