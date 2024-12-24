import heapq
from collections import defaultdict, Counter

# Node class to build the Huffman tree
class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        
    # Define comparison operators for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequency):
    # Priority queue to store nodes of the Huffman tree
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        # Pop two nodes with the lowest frequency
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create a new node with these two nodes as children and push it back to the heap
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

def build_codes(node, prefix="", codebook={}):
    if node.char is not None:
        codebook[node.char] = prefix
    else:
        build_codes(node.left, prefix + "0", codebook)
        build_codes(node.right, prefix + "1", codebook)
    return codebook

def huffman_encode(data):
    frequency = Counter(data)
    huffman_tree = build_huffman_tree(frequency)
    codebook = build_codes(huffman_tree)
    
    encoded_data = "".join(codebook[char] for char in data)
    return encoded_data, codebook

def huffman_decode(encoded_data, codebook):
    inverse_codebook = {v: k for k, v in codebook.items()}
    current_code = ""
    decoded_output = []
    
    for bit in encoded_data:
        current_code += bit
        if current_code in inverse_codebook:
            decoded_output.append(inverse_codebook[current_code])
            current_code = ""
    
    return "".join(decoded_output)

# Example usage
input_data = "huffman coding"
encoded_data, codebook = huffman_encode(input_data)
print(f"Encoded: {encoded_data}")
decoded_data = huffman_decode(encoded_data, codebook)
print(f"Decoded: {decoded_data}")
