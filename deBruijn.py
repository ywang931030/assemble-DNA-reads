#!/usr/bin/env python
'''
Build De Bruijn graph for input sequence.
Output formed as adjacency lists.
'''
__author__ = 'Yue Wang'


import time


def printGraph(graph):
	'''
	Print the nodes with father -> sons
	'''
	for node in graph.keys():
		buff = ''
		# add father node
		buff = node
		# add format
		buff += ' -> '
		# add the first son
		buff += graph[node][0]
		# add remains
		if len(graph[node]) > 1:
			for i in range(1, len(graph[node])):
				buff += ','
				buff += graph[node][i]

		# print the buff
		print buff

	return


def buildGraph(seq, k):
	'''
	Each node in the graph is the k - 1 mer, for k - 1 denote the overlap length between k-mers.
	In specific, the head node is its first k - 1 mer, and the tail node is its last k - 1 mer
	'''
	# scan all k-mers and create nodes
	nodes = {}
	l = len(seq)
	for i in range(l - k + 1):
		kmer = seq[i: i + k]

		# node not exist
		if kmer[0: k - 1] not in nodes.keys():
			# build the node
			nodes[kmer[0: k - 1]] = []
			# update the node.sons
			nodes[kmer[0: k - 1]].append(kmer[1: k])

		# node exist, update the node.sons
		else:
			nodes[kmer[0: k - 1]].append(kmer[1: k])

	return nodes


def readFile(filename):
	'''
	Read k and sequence from choosed file.
	'''
	with open(filename, 'r') as f:
		k = f.readline()
		seq = f.readline()
	return k, seq


def main():

	# readfile
	data = readFile('test.txt')
	k = int(data[0])
	seq = data[1]

	# build the graph
	graph = buildGraph(seq, k)

	# print the graph
	printGraph(graph)

if __name__ == '__main__':
	main()
