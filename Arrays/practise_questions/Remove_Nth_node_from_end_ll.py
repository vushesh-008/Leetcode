# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Remove the nth node from the end of the linked list and return the head of the linked list

            Time complexity: O(n)
            Space complexity: O(1)

        Args:
            head (Optional[ListNode]): Head of the linked list
            n (int): The nth node from the end of the linked list

        Returns:
            Optional[ListNode]: Head of the linked list after removing the nth node from the end
        """

        # Replace this placeholder return statement with your code
        start = head
        total_nodes = 0
        while start:
            total_nodes += 1
            start = start.next

        # [1,2,3] , n = 1 , total_nodes = 3
        # Output = [1,2]
        # [1,2,3] , n = 2 , total_nodes = 3
        # Output = [1,3]
        # [1,2,3] , n = 3 , total_nodes = 3
        # Output = [2,3]

        print(total_nodes)

        start = head
        count = 1
        while start:
            if count > (total_nodes - n):
                return start.next
                break
            if count == (total_nodes - n):
                start.next = start.next.next
                break
            start = start.next
            count += 1

        return head

    def removeNthFromEndTwoPointer(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """Remove the nth node from the end of the linked list and return the head of the linked list using two pointers

            Idea :
                The two-pointer technique involves using two pointers that are initially separated by n nodes.
                When the second pointer reaches the end of the list, the first pointer will be at the node just
                before the one we want to remove.

            Time complexity: O(n) , One pass
            Space complexity: O(1)

        Args:
            head (Optional[ListNode]): Head of the linked list
            n (int): The nth node from the end of the linked list

        Returns:
            Optional[ListNode]: Head of the linked list after removing the nth node from the end
        """

        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        # Move the second pointer n nodes ahead
        for _ in range(n):
            first = first.next

        if not first.next:
            return head.next

        # Move the first and second pointers simultaneously
        while first.next:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        return dummy.next


if __name__ == "__main__":
    # Example usage
    def print_list(node):
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")

    # Create a linked list [1, 2, 3, 4, 5]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print("Original linked list:")
    print_list(head)  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None

    sol = Solution()
    new_head = sol.removeNthFromEnd(head, 2)
    print("Linked list after removing 2nd node from the end:")
    print_list(new_head)  # Output: 1 -> 2 -> 3 -> 5 -> None

    print("#" * 140)
    # Create a linked list [1, 2, 3, 4, 5]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print("Original linked list:")
    print_list(head)  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None
    new_head = sol.removeNthFromEndTwoPointer(head, 2)
    print("Linked list after removing 2nd node from the end using two pointers:")
    print_list(new_head)  # Output: 1 -> 2 -> 3 -> 5 -> None
    new_head = sol.removeNthFromEndTwoPointer(head, 4)
    print("Linked list after removing 4th node from the end using two pointers:")
    print_list(new_head)  # Output: 1 -> 3 -> 4 -> 5 -> None
