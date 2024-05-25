import networkx as nx
import community as community_louvain  # Make sure this is the correct library, sometimes it's 'python-louvain'
import matplotlib.pyplot as plt
from collections import defaultdict

# Read the edge list from a file and create a graph
G = nx.read_edgelist("email-Eu-core.txt")

# Perform the Louvain method to find the best partition
partition = community_louvain.best_partition(G)
print("Initial partition:", partition)

# Group nodes by community labels
res = defaultdict(list)
for key, val in sorted(partition.items()):
    res[val].append(key)

# Convert the result to a list of sets
final_partition = []
for nodes in res.values():
    final_partition.append(set(nodes))

print('Final partition:', tuple(final_partition))

# Calculate and print the partition quality
partition_quality = community_louvain.partition_quality(G, final_partition)
print("Partition Quality:", partition_quality)

# Calculate and print the modularity of the partition
mod = community_louvain.modularity(G, partition)
print("Modularity:", mod)

# Function to draw the communities
def draw_communities(partition):
    # Assign colors to nodes based on their partition
    colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown']  # Adjust the color list as needed
    pos = nx.spring_layout(G)
    for i, part in enumerate(partition):
        nx.draw_networkx_nodes(G, pos, nodelist=part, node_color=colors[i % len(colors)])
    nx.draw_networkx_edges(G, pos)
    plt.show()

# Draw the communities
draw_communities(final_partition)
