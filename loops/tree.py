#!/usr/bin/python3


def create_node(name):
    return {"name": name, "children": []}

def add_child(root, child_name):
    child = create_node(child_name)  # Create a proper node dictionary
    root["children"].append(child)
    return root

def print_tree(node, level=0):
    
      # Corrected spacing
    for child in node["children"]:
        print_tree(child, level + 1)

# Initialize root correctly
root = create_node("Pictures")

# Add children to root
add_child(root, "photos")
add_child(root, "cameras")
add_child(root, "movies")
add_child(root, "dumps")

# Print the tree structure
print_tree(root)
