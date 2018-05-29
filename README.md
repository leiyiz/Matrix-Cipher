## A simple cipher based on linear algebra
### Discription
This is just a simple cipher program that uses hill ciper to cipher plain english with
**only alphabet supported** being non-capitalized english letters so far. (with support of spaces, period and comma in the future possible)  
The main purpose of this code is just to showcase how to generate a inversable matrix and its **multiplicative INTEGER inverse** of a matrix that only contains numbers from 0 to "the size of the vocabulary supported - 1" for the use of [Hill Cipher](https://en.wikipedia.org/wiki/Hill_cipher) only, and this program is not designed to be used to encript long string, and due to the use of numpy on chooing a **"inversable** matrix, this program could possibly give faulty answers once the size of matrix it's generating surpasses 5.

### Use of program.
this program requires user to put in a waiting-to-be-encripted string with a length equal to the dimension of the matrix that is to be generated. Failing to do so will cause the program crashing.
