
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def count_nodes(self, head):
        count = 0
        temp = head

        while temp is not None:
            count += 1
            temp = temp.next

        return count
    
    def print_list(self, head):

        temp = head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


    def count_nodes_recursive(self, head):

        if head is None:
            return 0
        
        return 1 + self.count_nodes_recursive(head.next)

    def searchKey(self, head, key):
        
        temp = head
        while temp is not None:
            if temp.data == key:
                return True
            temp = temp.next
            
        return False
    
    def insertAtEnd(self, head, x):
        """Insert node at end of linked list
        
        Time: O(n) - traverse to end
        Space: O(1)
        """
        new_node = Node(x)
        
        # ✓ Must handle empty list case!
        if head is None:
            return new_node
        
        # Traverse to the last node
        temp = head
        while temp.next is not None:
            temp = temp.next
        
        # Attach new node
        temp.next = new_node
        
        return head
    
    def insert_after(self, head, key, new_data):

        temp = head
        while temp is not None:
            if temp.data == key:
                break
            temp = temp.next

        # ✓ Must handle case where key is not found (temp becomes None)
        if temp is None:
            print(f"Key {key} not found in the list.")
            return head

        new_node = Node(new_data)
        new_node.next = temp.next
        temp.next = new_node

        return head 



if __name__ == "__main__":

    head = Node(10)

    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)

    print(f"Number of nodes in the linked list: {head.count_nodes(head)}")
    print(f"Number of nodes in the linked list (recursive): {head.count_nodes_recursive(head)}")

    print("\nLinked List: ", end="")
    head.print_list(head)
    
    # Test insertAtEnd
    print("\n" + "="*50)
    print("Testing insertAtEnd()")
    print("="*50)
    
    # Test 1: Insert into non-empty list
    print("\nTest 1: Insert 50 into [10, 20, 30, 40]")
    head = head.insertAtEnd(head, 50)
    print("Result: ", end="")
    head.print_list(head)
    
    # Test 2: Insert into empty list (this would crash without if check!)
    print("\nTest 2: Insert 100 into empty list")
    empty_head = None
    node = Node(0)  # Need instance to call method
    empty_head = node.insertAtEnd(empty_head, 100)
    print("Result: ", end="")
    node.print_list(empty_head)

    # Test insert_after
    print("\n" + "="*50)
    print("Testing insert_after()")
    print("="*50)
    # Test 1: Insert after existing key
    print("\nTest 1: Insert 25 after 20 in [10, 20, 30, 40, 50]")
    head = head.insert_after(head, 20, 25)
    print("Result: ", end="")
    head.print_list(head)