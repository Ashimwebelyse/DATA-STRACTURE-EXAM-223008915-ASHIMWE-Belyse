class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_node):
        
        self.children.append(child_node)

    def remove_child(self, child_name):
        
        self.children = [child for child in self.children if child.name != child_name]

    def display(self, level=0):
        
        print(" " * (level * 4) + f"- {self.name}")
        for child in self.children:
            child.display(level + 1)


# Example Usage
if __name__ == "__main__":
    # Create the root node for the product hierarchy
    root = TreeNode("Products")

    # Add main categories
    electronics = TreeNode("Electronics")
    fashion = TreeNode("Fashion")
    groceries = TreeNode("Groceries")

    root.add_child(electronics)
    root.add_child(fashion)
    root.add_child(groceries)

    # Add subcategories for Electronics
    electronics.add_child(TreeNode("Mobiles"))
    electronics.add_child(TreeNode("Laptops"))
    electronics.add_child(TreeNode("Accessories"))

    # Add subcategories for Fashion
    fashion.add_child(TreeNode("Men"))
    fashion.add_child(TreeNode("Women"))
    fashion.add_child(TreeNode("Kids"))

    # Add subcategories for Groceries
    groceries.add_child(TreeNode("Fruits"))
    groceries.add_child(TreeNode("Vegetables"))
    groceries.add_child(TreeNode("Beverages"))

    # Display the hierarchical structure
    print("E-commerce Product Categories:")
    root.display()

