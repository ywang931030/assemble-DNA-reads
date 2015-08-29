#!/usr/bin/env python

'''
input a seq of sorted k-mers pattern1, pattern2, ..., patternn such that the last k - 1 symbols of patterni are equal to the first k - 1 symbols
of patterni+1 for 1 <= i <= n - 1
output a string text of length k + n - 1 such that the i-th k-mers in text is equal to patterni
'''


def main():
    with open('test.txt', 'r') as inputData:
        seq = []
        for line in inputData:
            line = line.strip()
            seq.append(line)
    # print seq
    k = len(seq[0])
    fullSeq = [seq[0]]
    i = 1
    while i <= len(seq) - 1:
        fullSeq += seq[i][k - 1]
        i += 1
    print ''.join(fullSeq)

if __name__ == '__main__':
    main()
