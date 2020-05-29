import random
from numpy.random import choice
import networkx as nx
from itertools import combinations
import matplotlib.pyplot as plt
import collections

def ba_end(g):
	prob_degree = []
	nodes = g.nodes()
	n_edges = len(g.edges())
	for n in nodes:
		prob_n = float(g.degree(n)) / float((2 * n_edges))
		prob_degree.append(prob_n)
	endpoint = choice(nodes, p = prob_degree)
	return endpoint

def ba_graph(n, l):
	g = nx.Graph()
	g.add_node(0)

	if n > l+1:
		g.add_nodes_from(range(1, l+1))
		nodes = g.nodes()
		for n1, n2 in combinations(nodes, 2):
			g.add_edge(n1, n2)

		for i in range(l+1, n):											# adding the other nodes
			g.add_node(i)
			for j in range(l):											# choose endpoint randomly proportional to Pv=degree(v)/sum(degree)
				endpoint = ba_end(g)
				edges = g.edges()
				while (i, endpoint) in edges:
					endpoint = ba_end(g)
				g.add_edge(i, endpoint)

	if n <= l:
		g.add_nodes_from(range(1, l+1))
		nodes = g.nodes()
		for n1, n2 in combinations(nodes, 2):
			g.add_edge(n1, n2)

	return g

def info_graph(g, info):
	print(info)
	# connectivity
	if nx.is_connected(g):
		print("The graph is connected")
	else:
		print("The graph is not connected")

	# clustering coefficient
	cc = nx.average_clustering(g)
	print("Clustering coefficient: " + str(cc))
	
	# diameter
	d = nx.diameter(g)
	print("Diameter: " + str(d))

	# size biggest connected component
	largest_cc = max(nx.connected_component_subgraphs(g), key=len)
	size_cc = largest_cc.size()
	print("Size largest component: " + str(size_cc))

def print_degree(g, name, i):
	plt.figure(i)

	degree_sequence = sorted([d for n,d in g.degree()], reverse=True)
	degreeCount = collections.Counter(degree_sequence)
	deg, cnt = zip(*degreeCount.items())

	fig, ax = plt.subplots()
	plt.bar(deg, cnt, width = 0.80, color = '#468BFB', alpha = 0.5)

	plt.title("Degree Histogram " + name)
	plt.ylabel("Count")
	plt.xlabel("Degree")
	ax.set_xticks([d + 0.4 for d in deg])
	ax.set_xticklabels(deg)

def print_graph(g, info, i):
	plt.figure(i)
	plt.title(info)
	pos = nx.spring_layout(g)
	nx.draw_networkx_nodes(g, pos, node_size = 5, node_color = '#FF7F00')
	nx.draw_networkx_edges(g, pos, edge_color = '#4F4F4F', alpha = 0.2)

def main():
	#n = 15k
	g1 = ba_graph(15000, 4)
	g2 = ba_graph(15000, 10)
	info_graph(g1, "Barabasi-Albert n=15k, l=4")
	info_graph(g2, "Barabasi-Albert n=15k, l=10")
	print_degree(g1, "Barabasi-Albert n=15k, l=4", 0)
	print_degree(g2, "Barabasi-Albert n=15k, l=10", 1)
	
	#n = 10k
	g3 = ba_graph(10000, 4)
	g4 = ba_graph(10000, 10)
	info_graph(g3, "Barabasi-Albert n=10k, l=4")
	info_graph(g4, "Barabasi-Albert n=10k, l=10")
	print_degree(g3, "Barabasi-Albert n=10k, l=4", 2)
	print_degree(g4, "Barabasi-Albert n=10k, l=10", 3)
	#print_graph(g3, "Barabasi-Albert n=10k, l=4", 0)
	
	#n = 5k
	g5 = ba_graph(5000, 4)
	g6 = ba_graph(5000, 10)
	info_graph(g5, "Barabasi-Albert n=5k, l=4")
	info_graph(g6, "Barabasi-Albert n=5k, l=10")
	print_degree(g5, "Barabasi-Albert n=5k, l=4", 4)
	print_degree(g6, "Barabasi-Albert n=5k, l=10", 5)
	
	plt.show()

main()