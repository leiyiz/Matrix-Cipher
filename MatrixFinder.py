import sys
import numpy
from random import randint as ri
from copy import deepcopy

VOCAB = 29


# print out usage info
def usage():
    print("Usage: need 2 argument as matrix length and message", file=sys.stderr)


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
def inverse(my_matrix, my_result, dimension):
    matrix = deepcopy(my_matrix)
    result = deepcopy(my_result)
    # inverse using only multiplication and modular
    for col in range(dimension):
        multi = mod_inverse(matrix[col][col], VOCAB)
        matrix[col] = list(map(lambda x: (x * multi) % VOCAB, matrix[col]))
        result[col] = list(map(lambda x: (x * multi) % VOCAB, result[col]))
        for row in range(dimension):
            if row == col:
                continue
            if matrix[row][col] == 0:
                continue
            tmp_m_row = list(map(lambda x: (x * matrix[row][col]) % VOCAB, matrix[col]))
            tmp_r_row = list(map(lambda x: (x * matrix[row][col]) % VOCAB, result[col]))
            matrix[row] = [de_negative(a - b) for a, b in zip(matrix[row], tmp_m_row)]
            result[row] = [de_negative(a - b) for a, b in zip(result[row], tmp_r_row)]
    return result


# use modular arithmetic to reverse negative numbers
def de_negative(m):
    while m < 0:
        m += VOCAB
    return m


def check0(matrix, dimension):
    for i in range(dimension):
        if matrix[i][i] == 0:
            return True
    return False


def encode(vector, matrix):
    a = numpy.array(matrix)
    b = numpy.array(vector)
    result = numpy.dot(a, b).tolist()
    return list(map(lambda x: x % VOCAB, result))


# main method
def main():
    if len(sys.argv) != 3:
        usage()
        sys.exit(0)
    dimension = int(sys.argv[1])
    message = [ord(c) for c in sys.argv[2]]

    # randomly generate a matrix
    matrix = randomize(dimension)
    print("our matrix of choice is:")
    print(matrix)
    while numpy.linalg.matrix_rank(matrix) != dimension or check0(matrix, dimension):
        matrix = randomize(dimension)
    result = identity(dimension)

    # invert a matrix.
    inverted_matrix = inverse(matrix, result, dimension)
    print('inverted matrix is: ')
    print(inverted_matrix)

    # begin showing of encoding and decoding
    print('the message is: ' + ''.join(chr(i) for i in message))
    message = list(map(lambda x: x - 97, message))
    print('enc key is :' + str(matrix))
    cipher = encode(message, matrix)
    ciphered_message = list(map(lambda x: x + 97, cipher))
    print('ciphered message is: ' + ''.join(chr(i) for i in ciphered_message))
    back_message = encode(cipher, inverted_matrix)
    back_message = list(map(lambda x: x + 97, back_message))
    print('deciphered message is: ' + ''.join(chr(i) for i in back_message))


if __name__ == '__main__':
    main()
