import networkx as nx
import community  # Make sure you have the correct library, sometimes it's 'python-louvain'
import matplotlib.pyplot as plt
import itertools

# Read the edge list from a file and create a graph
G = nx.read_edgelist("email-Eu-core.txt")

# Perform the Girvan-Newman algorithm to detect communities
comm = community.girvan_newman(G)

# Specify the index of the partition to retrieve (0 for the first partition)
index = 0

# Retrieve the desired partition using itertools.islice
partition = next(itertools.islice(comm, index, None))

# Print the type of the partition to confirm the structure
print("Type of partition:", type(partition))

# Print each partition (community) detected
for i in partition:
    print("Nodes in community:", i)

# Function to draw the communities (assuming draw_communities is a predefined function)
def draw_communities(partition):
    # Assign colors to nodes based on their partition
    colors = ['red', 'blue', 'green', 'yellow', 'purple']  # Adjust the color list as needed
    pos = nx.spring_layout(G)
    for i, part in enumerate(partition):
        nx.draw_networkx_nodes(G, pos, nodelist=part, node_color=colors[i % len(colors)])
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
