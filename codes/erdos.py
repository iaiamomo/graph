import random
from numpy.random import choice
import networkx as nx
from itertools import combinations
import matplotlib.pyplot as plt
import collections

def er_graph(n,p):
	g = nx.Graph()

	nodes = range(n)
	g.add_nodes_from(nodes)

	if p <= 0:
		return g

	for n1, n2 in combinations(nodes, 2):
	  if random.random() < p:
	    g.add_edge(n1, n2)

	return g

def info_graph(g, info):
	print("Erdos-Renyi graph with " + info)
	# connectivity
	if nx.is_connected(g):
		print("The graph is connected")
	else:
		print("The graph is not connected")

	# clustering coefficient
	cc = nx.average_clustering(g)
	print("Clustering coefficient: " + str(cc))
	
	# diameter
	d = 0
	largest_cc = max(nx.connected_component_subgraphs(g), key=len)
	if nx.is_connected(g) == False:
		d_max = 0
		list_conn_comp = [g.subgraph(c).copy() for c in nx.connected_components(g)]
		for sg in list_conn_comp:
			d_conn_comp = nx.diameter(sg)
			if d_conn_comp > d_max:
				d_max = d_conn_comp
		d = d_max
	else:
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
	nx.draw(g, pos, node_size = 5, node_color = '#FF7F00', edge_color = '#4F4F4F')
	'''
	nx.draw_networkx_nodes(g, pos, node_size = 5, node_color = '#FF7F00')
	nx.draw_networkx_edges(g, pos, edge_color = '#4F4F4F', alpha = 0.2)
	'''

def main():
	
	#n = 15k
	g0 = er_graph(15000, 0.00005)
	g1 = er_graph(15000, 0.00009)
	g2 = er_graph(15000, 0.0007)
	g3 = er_graph(15000, 0.002)
	info_graph(g0, "n=15k, p=0.00005")
	info_graph(g1, "n=15k, p=0.00009")
	info_graph(g2, "n=15k, p=0.0007")
	info_graph(g3, "n=15k, p=0.002")
	print_degree(g0, "Erdos-Renyi n=15k, p=0.00005", 0)
	print_degree(g1, "Erdos-Renyi n=15k, p=0.00009", 1)
	print_degree(g2, "Erdos-Renyi n=15k, p=0.0007", 2)
	print_degree(g3, "Erdos-Renyi n=15k, p=0.002", 3)
	
	#n = 10k
	g4 = er_graph(10000, 0.00008)
	g5 = er_graph(10000, 0.0004)
	g6 = er_graph(10000, 0.0009)
	g7 = er_graph(10000, 0.002)
	g8 = er_graph(10000, 0.005)
	info_graph(g4, "n=10k, p=0.00008")
	info_graph(g5, "n=10k, p=0.0004")
	info_graph(g6, "n=10k, p=0.0009")
	info_graph(g7, "n=10k, p=0.002")
	info_graph(g8, "n=10k, p=0.005")
	print_degree(g4, "Erdos-Renyi n=10k, p=0.00008", 4)
	print_degree(g5, "Erdos-Renyi n=10k, p=0.0004", 5)
	print_degree(g6, "Erdos-Renyi n=10k, p=0.0009", 6)
	print_degree(g7, "Erdos-Renyi n=10k, p=0.002", 7)
	print_degree(g8, "Erdos-Renyi n=10k, p=0.005", 8)
	#print_graph(g6, "Erdos-Renyi n=10k, p=0.0009", 0)
	
	#n = 5k
	g9 = er_graph(5000, 0.0002)
	g10 = er_graph(5000, 0.0008)
	g11 = er_graph(5000, 0.002)
	g12 = er_graph(5000, 0.005)
	info_graph(g9, "n=5k, p=0.0002")
	info_graph(g10, "n=5k, p=0.0008")
	info_graph(g11, "n=5k, p=0.002")
	info_graph(g12, "n=5k, p=0.005")
	print_degree(g9, "Erdos-Renyi n=5k, p=0.0002", 9)
	print_degree(g10, "Erdos-Renyi n=5k, p=0.0008", 10)
	print_degree(g11, "Erdos-Renyi n=5k, p=0.002", 11)
	print_degree(g12, "Erdos-Renyi n=5k, p=0.005", 12)
	#print_graph(g11, "Erdos-Renyi n=5k, p=0.002", 0)
	
	plt.show()
	
main()