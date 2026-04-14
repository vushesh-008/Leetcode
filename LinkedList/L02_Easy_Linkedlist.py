# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        list3 = ListNode()
        head = list3

        while list1 and list2 :
            if list1.val < list2.val:
                list3.next = list1
                list1 = list1.next
            else:
                list3.next = list2
                list2 = list2.next
            list3 = list3.next
            
        list3.next = list1 or list2 

        return head.next
        
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head

        if temp is None:
            return temp

        while temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head


# ============================================================================
# Linked List Cycle Detection - Floyd's Cycle Detection Algorithm
# ============================================================================
class SolutionCycle:
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """CORRECT VERSION - Floyd's Cycle Detection (Tortoise and Hare)
        
        Time: O(n) - at most 2n steps if there's a cycle
        Space: O(1) - only two pointers
        
        Key Idea:
        - Slow pointer moves 1 step at a time
        - Fast pointer moves 2 steps at a time
        - If there's a cycle, fast will eventually catch up to slow
        - If there's no cycle, fast will reach the end (None)
        """
        slow = head
        fast = head
        
        # ✓ CORRECT: Check fast and fast.next BEFORE accessing fast.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False


def create_cycle(values, pos):
    """Helper to create linked list with cycle at position pos"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    nodes = [head]
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        nodes.append(current)
    
    # Create cycle if pos >= 0
    if pos >= 0:
        current.next = nodes[pos]
    
    return head


if __name__ == "__main__":
    solution = SolutionCycle()
    
    print("="*70)
    print("LINKED LIST CYCLE DETECTION")
    print("="*70)
    
    # Test 1: Cycle at position 1
    print("\nTest 1: [3,2,0,-4], pos=1 (cycle exists)")
    head1 = create_cycle([3, 2, 0, -4], 1)
    print(f"Has cycle: {solution.hasCycle(head1)}")  # True
    
    # Test 2: Cycle at position 0
    print("\nTest 2: [1,2], pos=0 (cycle exists)")
    head2 = create_cycle([1, 2], 0)
    print(f"Has cycle: {solution.hasCycle(head2)}")  # True
    
    # Test 3: No cycle
    print("\nTest 3: [1], pos=-1 (no cycle)")
    head3 = create_cycle([1], -1)
    print(f"Has cycle: {solution.hasCycle(head3)}")  # False
    
    # Test 4: Empty list
    print("\nTest 4: [], pos=-1 (empty list)")
    head4 = None
    print(f"Has cycle: {solution.hasCycle(head4)}")  # False
    
    # Test 5: Two nodes, no cycle
    print("\nTest 5: [1,2], pos=-1 (no cycle)")
    head5 = create_cycle([1, 2], -1)
    print(f"Has cycle: {solution.hasCycle(head5)}")  # False
    
    print("\n" + "="*70)
    print("THE BUG IN YOUR CODE:")
    print("="*70)
    print("""
❌ WRONG:
    while slow.next and fast.next.next:
    
    Problem: If fast.next is None, accessing fast.next.next crashes!
    
✓ CORRECT:
    while fast and fast.next:
    
    Why:
    1. Check 'fast' exists before accessing fast.next
    2. Check 'fast.next' exists before doing fast.next.next
    3. This handles all edge cases: empty list, single node, two nodes
    
    No need to check 'slow' because fast always moves faster,
    so if fast is valid, slow is definitely valid.
    """)

        
        