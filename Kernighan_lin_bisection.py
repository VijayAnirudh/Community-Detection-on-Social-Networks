import networkx as nx
import community  # Make sure you have the correct library, sometimes it's 'python-louvain'
import matplotlib.pyplot as plt

# Read the edge list from a file and create a graph
G = nx.read_edgelist("email-Eu-core.txt")

# Perform the Kernighan-Lin bisection algorithm to partition the graph
partition = community.kernighan_lin_bisection(G)
print("Partition:", partition)

# Print each partition
for i in partition:
    print("Nodes in partition:", i)

# Function to draw the communities (assuming draw_communities is a predefined function)
def draw_communities(partition):
    # Assign colors to nodes based on their partition
    colors = ['red', 'blue']  # Assuming two partitions for simplicity
    pos = nx.spring_layout(G)
    for i, part in enumerate(partition):
        nx.draw_networkx_nodes(G, pos, nodelist=part, node_color=colors[i])
    nx.draw_networkx_edges(G, pos)
    plt.show()

# Draw the communities
draw_communities(partition)

# Calculate and print the modularity of the partition
mod = community.modularity(G, partition)
print("Modularity:", mod)

# Calculate and print the partition quality
partition_quality = community.partition_quality(G, partition)
print("Partition Quality:", partition_quality)
