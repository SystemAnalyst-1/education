from sys import argv


def wage(hours, bid, prize):
    return hours * bid + prize


print(wage(int(argv[1]), int(argv[2]), int(argv[3])))
