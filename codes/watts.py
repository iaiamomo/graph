import random
from numpy.random import choice
import networkx as nx
from itertools import combinations
import matplotlib.pyplot as plt
import collections

def ws_graph(n, k, beta):
	g = nx.Graph()

	if k == 0:
		g.add_nodes_from(range(n))
		return g
	
	for i in range(n):
		for j in range(i+1, i+k//2+1):
			g.add_edge(i, j % n)

	#considerin only k/2 neighbors on the right
	if beta > 0 and beta <= 1:
		for i in range(n):
			neighbors = range(i+1, i+k//2+1)
			for j in range(k//2):
				if neighbors[j] >= n:
					neighbors[j] = neighbors[j]%n
			node = [i]*(k//2)
			for n1,n2 in zip(node, neighbors):
				if random.random() < beta:
					new_end = random.randint(0, n-1)
					while new_end == n1 or g.has_edge(n1, new_end):
						new_end = random.randint(0, n-1)
					g.remove_edge(n1, n2)
					g.add_edge(n1, new_end)

	return g

def info_graph(g, info):
	print("Watts-Strogatz graph with " + info)
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
	g1 = ws_graph(15000, 25, 0.0002)
	g2 = ws_graph(15000, 25, 0.003)
	g3 = ws_graph(15000, 25, 0.05)
	g4 = ws_graph(15000, 25, 0.1)
	g5 = ws_graph(15000, 25, 0.5)
	g6 = ws_graph(15000, 25, 0.8)
	info_graph(g1, "n=15k, k=25, beta=0.0002")
	info_graph(g2, "n=15k, k=25, beta=0.003")
	info_graph(g3, "n=15k, k=25, beta=0.05")
	info_graph(g4, "n=15k, k=25, beta=0.1")
	info_graph(g5, "n=15k, k=25, beta=0.5")
	info_graph(g6, "n=15k, k=25, beta=0.8")
	print_degree(g1, "Watts-Strogatz n=15k, k=25, beta=0.0002", 0)
	print_degree(g2, "Watts-Strogatz n=15k, k=25, beta=0.003", 1)
	print_degree(g3, "Watts-Strogatz n=15k, k=25, beta=0.05", 2)
	print_degree(g4, "Watts-Strogatz n=15k, k=25, beta=0.1", 3)
	print_degree(g5, "Watts-Strogatz n=15k, k=25, beta=0.5", 4)
	print_degree(g6, "Watts-Strogatz n=15k, k=25, beta=0.8", 5)

	#n = 10k
	g7 = ws_graph(10000, 25, 0.0002)
	g8 = ws_graph(10000, 25, 0.003)
	g9 = ws_graph(10000, 25, 0.05)
	g10 = ws_graph(10000, 25, 0.1)
	g11 = ws_graph(10000, 25, 0.5)
	g12 = ws_graph(10000, 25, 0.8)
	info_graph(g7, "n=10k, k=25, beta=0.0002")
	info_graph(g8, "n=10k, k=25, beta=0.003")
	info_graph(g9, "n=10k, k=25, beta=0.05")
	info_graph(g10, "n=10k, k=25, beta=0.1")
	info_graph(g11, "n=10k, k=25, beta=0.5")
	info_graph(g12, "n=10k, k=25, beta=0.8")
	print_degree(g7, "Watts-Strogatz n=10k, k=25, beta=0.0002", 6)
	print_degree(g8, "Watts-Strogatz n=10k, k=25, beta=0.003", 7)
	print_degree(g9, "Watts-Strogatz n=10k, k=25, beta=0.05", 8)
	print_degree(g10, "Watts-Strogatz n=10k, k=25, beta=0.1", 9)
	print_degree(g11, "Watts-Strogatz n=10k, k=25, beta=0.5", 10)
	print_degree(g12, "Watts-Strogatz n=10k, k=25, beta=0.8", 11)
	#print_graph(g9, "Watts-Strogatz n=10k, k=25, beta=0.05", 0)
	#print_graph(g12, "Watts-Strogatz n=10k, k=25, beta=0.8", 0)

	#n = 5k
	g13 = ws_graph(5000, 25, 0.0002)
	g14 = ws_graph(5000, 25, 0.003)
	g15 = ws_graph(5000, 25, 0.05)
	g16 = ws_graph(5000, 25, 0.1)
	g17 = ws_graph(5000, 25, 0.5)
	g18 = ws_graph(5000, 25, 0.8)
	info_graph(g13, "n=5k, k=25, beta=0.0002")
	info_graph(g14, "n=5k, k=25, beta=0.003")
	info_graph(g15, "n=5k, k=25, beta=0.05")
	info_graph(g16, "n=5k, k=25, beta=0.1")
	info_graph(g17, "n=5k, k=25, beta=0.5")
	info_graph(g18, "n=5k, k=25, beta=0.8")
	print_degree(g13, "Watts-Strogatz n=5k, k=25, beta=0.0002", 12)
	print_degree(g14, "Watts-Strogatz n=5k, k=25, beta=0.003", 13)
	print_degree(g15, "Watts-Strogatz n=5k, k=25, beta=0.05", 14)
	print_degree(g16, "Watts-Strogatz n=5k, k=25, beta=0.1", 15)
	print_degree(g17, "Watts-Strogatz n=5k, k=25, beta=0.5", 16)
	print_degree(g18, "Watts-Strogatz n=5k, k=25, beta=0.8", 17)

	plt.show()

main()