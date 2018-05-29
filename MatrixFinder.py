import sys
import numpy
from random import randint as ri


VOCAB = 29


# print out usage info
def usage():
    print("Usage: need one argument as matrix length", file=sys.stderr)


# find the modular multiplicative inverse of 'a' under modulo 'm'
def mod_inverse(a, m):
    a = a % m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return 1


# generate an identity matrix
def identity(dimension):
    matrix = []
    for i in range(dimension):
        new = [0] * dimension
        new[i] = 1
        matrix.append(new)
    return matrix


# generate a random matrix based on VOCAB
def randomize(dimension):
    matrix = []
    for i in range(dimension):
        new = []
        for j in range(dimension):
            new.append(ri(0, VOCAB - 1))
        matrix.append(new)
    return matrix


# inverse an n*n matrix with modular
def inverse(matrix, result, dimension):
    print(matrix)
    print(result)
    print('*' * 33)
    for i in range(dimension):
        multi = mod_inverse(matrix[i][i], VOCAB)
        matrix[i] = list(map(lambda x: (x * multi) % VOCAB, matrix[i]))
        result[i] = list(map(lambda x: (x * multi) % VOCAB, result[i]))

    print(matrix)
    print(result)
    return result


# use modular arithmetic to reverse negative numbers
def de_negative (m):
    while m < 0:
        m += VOCAB
    return m


# main method
def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(0)
    dimension = int(sys.argv[1])
    matrix = randomize(dimension)
    print("our matrix of choice is:")
    print(matrix)
    while numpy.linalg.matrix_rank(matrix) != dimension:
        matrix = randomize(dimension)
    result = identity(dimension)
    inverted_matrix = inverse(matrix, result, dimension)


if __name__ == '__main__':
    main()
