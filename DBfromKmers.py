#!/usr/bin/env python
'''
Construct de bruijn graph from a set of given k-mers
'''
__author__ = 'Yue Wang'


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
	construct adjacency list of the de bruijn graph (pattern)
	'''
	nodes = {}
	for kmer in seq:
		# nodes not exist
		if kmer[0: k - 1] not in nodes.keys():
			nodes[kmer[0: k - 1]] = []
			# update the node.sons
			nodes[kmer[0: k - 1]].append(kmer[1: k])

		# nodes exist
		else:
			nodes[kmer[0: k - 1]].append(kmer[1: k])

	return nodes


def readFile(filename):
	'''
	Read kmers from choosed file.
	'''
	seq = []
	with open(filename, 'r') as f:
		for line in f:
			line = line.strip()
			seq.append(line)
	return seq


def main():

	# readfile
	seq = readFile('test.txt')
	k = len(seq[0])
	graph = buildGraph(seq, k)
	printGraph(graph)


if __name__ == '__main__':
	main()
