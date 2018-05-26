import sys
import numpy
from random import randint as ri


VOCAB = 29


# print out usage info
def usage():
    print("Usage: need one argument as matrix length", file=sys.stderr)


# find the modulor multiplicative inverse of 'a' under modulo


# generate a random matrix based on VOCAB
def randomize(dimension):
    matrix = []
    for i in range(dimension):
        new = []
        for j in range(dimension):
            new.append(ri(0, VOCAB - 1))
        matrix.append(new)
    return matrix


# main method
def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(0)
    dimension = int(sys.argv[1])
    matrix = randomize(dimension)
    print(matrix)
    while numpy.linalg.matrix_rank(matrix) != dimension:
        matrix = randomize(dimension)
    print(matrix)


if __name__ == '__main__':
    main()
