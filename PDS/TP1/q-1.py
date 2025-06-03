import matplotlib.pyplot as plt
import networkx as nx
from collections import Counter
import heapq

# Define the Huffman tree node
class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Build the Huffman tree from text
def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(freq=left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(heap, parent)

    return heap[0]

# Generate Huffman codes
def generate_codes(node, prefix="", code_map={}):
    if node is not None:
        if node.char is not None:
            code_map[node.char] = prefix
        generate_codes(node.left, prefix + "0", code_map)
        generate_codes(node.right, prefix + "1", code_map)
    return code_map

# Build the graph with Huffman codes in node labels
def add_edges(graph, node, label, pos, codes, x=0, y=0, dx=1.0):
    if node is None:
        return
    node_id = id(node)
    if node.char is not None:
        label[node_id] = f"'{node.char}'\n{node.freq}\n{codes[node.char]}"
    else:
        label[node_id] = f"{node.freq}"
    pos[node_id] = (x, y)
    if node.left:
        left_id = id(node.left)
        graph.add_edge(node_id, left_id)
        add_edges(graph, node.left, label, pos, codes, x - dx, y - 1, dx / 2)
    if node.right:
        right_id = id(node.right)
        graph.add_edge(node_id, right_id)
        add_edges(graph, node.right, label, pos, codes, x + dx, y - 1, dx / 2)

# Main
text_input = "compilar código em python"
root = build_huffman_tree(text_input)
codes = generate_codes(root)

G = nx.DiGraph()
labels = {}
positions = {}
add_edges(G, root, labels, positions, codes)

plt.figure(figsize=(14, 8))
nx.draw(G, pos=positions, with_labels=False, arrows=False, node_size=2000, node_color="lightblue")
nx.draw_networkx_labels(G, pos=positions, labels=labels, font_size=9)
plt.title("Árvore de Huffman com códigos para cada caractere")
plt.axis("off")
plt.show()

# Print the dictionary of Huffman codes
print("Dicionário de códigos de Huffman:")
for char, code in sorted(codes.items()):
    print(f"'{char}': {code}")
