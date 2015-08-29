#!/usr/bin/env python

'''
input a seq of k-mers pattern1, pattern2, ..., patternn such that the last k - 1 symbols of patterni are equal to the first k - 1 symbols
of patterni+1 for 1 <= i <= n - 1
output a string text of length k + n - 1 such that the i-th k-mers in text is equal to patterni
'''


def buildIndex(seq, k):
    kmersIndex = {}
    for each in seq:
        if each in kmersIndex.keys():
            kmersIndex[each]['occur'] += 1
        else:
            kmersIndex[each] = {}
            '''
            'sonIndex' is the id to find son, consists of last k - 1 pattern in each
            '''
            kmersIndex[each]['sonIndex'] = each[1: k]
            '''
            'fatherIndex' is the id to find father, consists of first k - 1 pattern in each
            '''
            kmersIndex[each]['fatherIndex'] = each[0: k - 1]
            '''
            'father' and 'son' is the node to store the compaired pattern according to the index
            '''
            kmersIndex[each]['father'] = []
            kmersIndex[each]['son'] = []
            kmersIndex[each]['occur'] = 1
    return kmersIndex


def mapping(pattern, seq, k):
    '''
    input a pattern, scan other pattern in seq
    if pattern[fatherIndex] == currentseq[sonIndex]
        pattern[father] = currentseq
        currentseq[son] = pattern
    if there is no other pattern's sonIndex in seq equals to pattern[fatherIndex]
        tag the pattern as head
    if pattern[sonIndex] == currentseq[fatherIndex]
        pattern[son] = currentseq
        currentseq[father] = pattern
    if there is no other pattern's fatherIndex in seq equals to pattern[sonIndex]
        tag the pattern as tail
    '''
    for eachseq in seq:
        if pattern != eachseq:
            if seq[pattern]['sonIndex'] == seq[eachseq]['fatherIndex']:
                    seq[eachseq]['father'].append(pattern)
                    if seq[eachseq]['occur'] > 1:
                        i = 1
                        while i <= seq[eachseq]['occur']:
                            seq[pattern]['son'].append(eachseq)
                            i += 1
                    else:
                        seq[pattern]['son'].append(eachseq)
        else:
            continue
    return seq


def main():
    with open('test.txt', 'r') as inputData:
        for line in inputData:
            line = line.strip()
            seq = line
    # print seq
    allKmers = []
    k = 12
    for i in xrange(len(seq) - k + 1):
        allKmers.append(seq[i: i + k])
    print allKmers
    kmersIndex = buildIndex(allKmers, k)
    pathTree = kmersIndex
    for each in kmersIndex:
        pathTree = mapping(each, pathTree, k)
    # print pathTree
    exist = []
    for each in pathTree:
        if pathTree[each]['father'] != [] or pathTree[each]['son'] != []:
            if len(pathTree[each]['son']) > 0:
                cache = pathTree[each]['son'][0][1: k]
                for i in range(1, len(pathTree[each]['son'])):
                    cache = cache + ',' + pathTree[each]['son'][i][1: k]
            if pathTree[each]['son'] != [] and each[1: k] not in exist:
                # print (each[1: k] + ' ' + '->' + ' ' + cache)
                exist.append(each[1: k])


if __name__ == '__main__':
    main()
