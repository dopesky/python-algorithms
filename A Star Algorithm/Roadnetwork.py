import networkx as nx
import matplotlib.pyplot as plt
from classes.astaralgo import AStarTraverser

G = nx.Graph()
nodes = [
    'karen', 'gitaru', 'loresho', 'lavington', 'parklands', 'kilimani', 'langata', 'CBD', 'donholm', 'hill view',
    'kasarani', 'kahawa', 'imara daima', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'j8', 'j9', 'j10', 'j11', 'j12',
    'j13'
]
G.add_nodes_from(nodes)
G.nodes()  # confirm nodes
# Add Edges and their weights
G.add_edge("gitaru", "j6", weight="10")
G.add_edge("gitaru", "j7", weight="6")
G.add_edge("CBD", "j12", weight="1.5")
G.add_edge("CBD", "j13", weight="5.5")
G.add_edge("donholm", "imara daima", weight="10.4")
G.add_edge("donholm", "hill view", weight="20")
G.add_edge("hill view", "kasarani", weight="1.7")
G.add_edge("kahawa", "kasarani", weight="11.5")
G.add_edge("imara daima", "j13", weight="3.9")
G.add_edge("j1", "j2", weight="6")
G.add_edge("j1", "j4", weight="2.6")
G.add_edge("j1", "karen", weight="2.8")
G.add_edge("j2", "j3", weight="5.4")
G.add_edge("j2", "langata", weight="2.6")
G.add_edge("j3", "j4", weight="9")
G.add_edge("j3", "j12", weight="6.7")
G.add_edge("j3", "j13", weight="6.2")
G.add_edge("j4", "j5", weight="9.7")
G.add_edge("j4", "j6", weight="6")
G.add_edge("j5", "kilimani", weight="0.5")
G.add_edge("j6", "karen", weight="4")
G.add_edge("j6", "j7", weight="6")
G.add_edge("j7", "j8", weight="7")
G.add_edge("j8", "loresho", weight="2")
G.add_edge("j8", "j9", weight="3")
G.add_edge("j9", "lavington", weight="7")
G.add_edge("j9", "j10", weight="4")
G.add_edge("j10", "parklands", weight="3")
G.add_edge("j10", "j11", weight="7")
G.add_edge("j11", "lavington", weight="0.5")
G.add_edge("j11", "kilimani", weight="0.5")
G.add_edge("j12", "kilimani", weight="2.3")
# position the nodes to resemble Nairobis map
G.node["karen"]['pos'] = (0, 0)
G.node["loresho"]['pos'] = (8, 32)
G.node["lavington"]['pos'] = (16, 12)
G.node["parklands"]['pos'] = (32, 28)
G.node["kilimani"]['pos'] = (32, 4)
G.node["langata"]['pos'] = (8, -20)
G.node["CBD"]['pos'] = (40, 0)
G.node["donholm"]['pos'] = (44, 4)
G.node["hill view"]['pos'] = (44, 16)
G.node["gitaru"]['pos'] = (-4, 16)
G.node["kasarani"]['pos'] = (44, 24)
G.node["kahawa"]['pos'] = (48, 32)
G.node["imara daima"]['pos'] = (44, -16)
G.node["j1"]['pos'] = (4, -4)
G.node["j2"]['pos'] = (8, -12)
G.node["j3"]['pos'] = (20, -12)
G.node["j4"]['pos'] = (12, -4)
G.node["j5"]['pos'] = (24, -4)
G.node["j6"]['pos'] = (0, 8)
G.node["j7"]['pos'] = (0, 20)
G.node["j8"]['pos'] = (8, 20)
G.node["j9"]['pos'] = (16, 20)
G.node["j10"]['pos'] = (28, 20)
G.node["j11"]['pos'] = (32, 16)
G.node["j12"]['pos'] = (36, 0)
G.node["j13"]['pos'] = (40, -8)
# store all positions in a variable
node_pos = nx.get_node_attributes(G, 'pos')
# call BFS to return set of all possible routes to the goal
route_bfs = AStarTraverser()
routes = route_bfs.a_star(G, "karen", 'imara daima')
print(route_bfs.visited)
route_list = route_bfs.visited
# color the nodes in the route_bfs
node_col = ['darkturquoise' if node not in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list, route_list[1:]))
# color the edges as well
# print(peru_colored_edges)
edge_col = ['darkturquoise' if edge not in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx(G, node_pos, node_color=node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos, width=2, edge_color=edge_col)
nx.draw_networkx_edge_labels(G, node_pos, edge_color=edge_col, edge_labels=arc_weight)
plt.axis('off')
plt.show()
