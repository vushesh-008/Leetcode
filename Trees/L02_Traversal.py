from collections import deque

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def pre_order(self, node):

        if node is None:
            return 
        
        print(node.value, end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):

        if node is None:
            return
        
        self.in_order(node.left)
        print(node.value, end=" ")
        self.in_order(node.right)

    def post_order(self, node):
        
        if node is None:
            return
        
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.value, end=" ")


    def level_order(self, head):
        if head is None:
            return []

        traversal = []
        queue = deque([root])

        while queue:
            n = len(queue)
            each_level = []
            
            for i in range(n):
                current_node = queue.popleft()
                each_level.append(current_node.value)

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)


            traversal.append(each_level)

        return traversal
    
    def pre_order_iterative(self, head):
        if head is None:
            return []
        
        traversal = []
        stack = [head]

        while stack:
            current_node = stack.pop()
            traversal.append(current_node.value)

            # Push right first so that left is processed first
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

        return traversal
    
    
if __name__ == "__main__":
    root = Tree(5)
    root.left = Tree(12)
    root.right = Tree(13)
    root.left.left = Tree(7)
    root.left.left.left = Tree(17)
    root.left.left.right = Tree(23)

    root.right.left = Tree(14)
    root.right.right = Tree(2)
    root.right.left.left = Tree(27)
    root.right.left.right = Tree(3)
    root.right.right.left = Tree(8)
    root.right.right.right = Tree(11)

    print("Pre-order Traversal: ", end="")
    root.pre_order(root)
    print("\nIn-order Traversal: ", end="")
    root.in_order(root)
    print("\nPost-order Traversal: ", end="")
    root.post_order(root)

    print("\nLevel-order Traversal: ", end="")
    print(root.level_order(root))

    print("\nPre-order Iterative Traversal: ", end="")
    print(root.pre_order_iterative(root))