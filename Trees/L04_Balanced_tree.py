"""
Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of the 
two subtrees of every node never differs by more than 1.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
Explanation: 
       3
      / \
     9  20
       /  \
      15   7
Heights differ by at most 1 at every node.

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Explanation:
         1
        / \
       2   2
      / \
     3   3
    / \
   4   4
The subtrees of node with value 2 differ in height by 2.

Example 3:
Input: root = []
Output: true

Constraints:
- The number of nodes in the tree is in the range [0, 5000]
- -10^4 <= Node.val <= 10^4
"""

from typing import Optional
from collections import deque


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    # ========================================================================
    # APPROACH 1: Naive - Check height at every node (INEFFICIENT)
    # ========================================================================
    def isBalanced_Naive(self, root: Optional[TreeNode]) -> bool:
        """
        Naive approach: For each node, calculate left and right heights
        
        Time Complexity: O(n²) - for each node, we calculate height (O(n) each)
        Space Complexity: O(h) - recursion stack
        
        ❌ This approach works but is inefficient!
        """
        def height(node):
            """Helper to calculate height of a tree"""
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        # Base case
        if not root:
            return True
        
        # Check if current node is balanced
        left_height = height(root.left)
        right_height = height(root.right)
        
        if abs(left_height - right_height) > 1:
            return False
        
        # Recursively check left and right subtrees
        return self.isBalanced_Naive(root.left) and self.isBalanced_Naive(root.right)
    
    
    # ========================================================================
    # APPROACH 2: Optimized - Calculate height and check balance together ✓
    # ========================================================================
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Optimized approach: Check balance while calculating height
        
        Time Complexity: O(n) - visit each node once
        Space Complexity: O(h) - recursion stack
        
        ✓ This is the OPTIMAL solution!
        
        Key Idea: Return -1 if subtree is unbalanced, else return height
        """
        def check_height(node):
            """
            Returns:
                - Height of tree if balanced
                - -1 if unbalanced
            """
            # Base case: empty tree has height 0 and is balanced
            if not node:
                return 0
            
            # Check left subtree
            left_height = check_height(node.left)
            if left_height == -1:  # Left subtree is unbalanced
                return -1
            
            # Check right subtree
            right_height = check_height(node.right)
            if right_height == -1:  # Right subtree is unbalanced
                return -1
            
            # Check if current node is balanced
            if abs(left_height - right_height) > 1:
                return -1  # Current node is unbalanced
            
            # Return height of current tree
            return 1 + max(left_height, right_height)
        
        return check_height(root) != -1
    
    
    # ========================================================================
    # YOUR CODE - BUGGY VERSION (for comparison)
    # ========================================================================
    def isBalanced_BUGGY(self, root: Optional[TreeNode]) -> bool:
        """
        This shows YOUR code with the bugs
        """
        def height(self, root):  # ❌ BUG 1: Nested function should NOT have 'self'
            if root is None:
                return 0
            return 1 + max(self.height(root.left), self.height(root.right))  # ❌ BUG 2: self.height() is wrong

        if root is None:
            return True

        left_height = height(root.left)  # ← This will crash!
        right_height = height(root.right)

        if abs(left_height-right_height) > 1:
            return False

        return self.isBalanced_BUGGY(root.left) and self.isBalanced_BUGGY(root.right)
    
    
    # ========================================================================
    # YOUR CODE FIXED - Naive approach (still O(n²) but works)
    # ========================================================================
    def isBalanced_YourCodeFixed(self, root: Optional[TreeNode]) -> bool:
        """
        Your code FIXED - removed 'self' from nested function
        
        Time: O(n²) - this works but is inefficient
        """
        def height(root):  # ✓ FIX 1: Remove 'self' parameter
            if root is None:
                return 0
            return 1 + max(height(root.left), height(root.right))  # ✓ FIX 2: Just height(), no self

        if root is None:
            return True

        left_height = height(root.left)
        right_height = height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.isBalanced_YourCodeFixed(root.left) and self.isBalanced_YourCodeFixed(root.right)
    
    
    # ========================================================================
    # APPROACH 3: Using class variable to track balance status
    # ========================================================================
    def isBalanced_WithFlag(self, root: Optional[TreeNode]) -> bool:
        """
        Alternative: Use instance variable to track if tree is balanced
        
        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        self.balanced = True
        
        def height(node):
            if not node or not self.balanced:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            
            if abs(left_height - right_height) > 1:
                self.balanced = False
            
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.balanced


# ============================================================================
# Helper Functions for Testing
# ============================================================================

def build_tree(values):
    """Build tree from level-order list (LeetCode format)"""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


def visualize_tree(root, level=0, prefix="Root: "):
    """Pretty print tree structure"""
    if root is None:
        return
    print(" " * (level * 4) + prefix + str(root.val))
    if root.left or root.right:
        if root.left:
            visualize_tree(root.left, level + 1, "L--- ")
        else:
            print(" " * ((level + 1) * 4) + "L--- None")
        if root.right:
            visualize_tree(root.right, level + 1, "R--- ")
        else:
            print(" " * ((level + 1) * 4) + "R--- None")


def get_height(root):
    """Helper to get height for visualization"""
    if not root:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))


def check_balance_detailed(root, name="Root"):
    """Show detailed balance info for each node"""
    if not root:
        return 0, True
    
    left_height, left_balanced = check_balance_detailed(root.left, f"{name}.left")
    right_height, right_balanced = check_balance_detailed(root.right, f"{name}.right")
    
    is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
    
    print(f"{name}({root.val}): L_height={left_height}, R_height={right_height}, "
          f"Diff={abs(left_height - right_height)}, Balanced={'✓' if is_balanced else '✗'}")
    
    return 1 + max(left_height, right_height), is_balanced


# ============================================================================
# Test Cases
# ============================================================================

if __name__ == "__main__":
    solution = Solution()
    
    print("=" * 70)
    print("YOUR CODE - BUG EXPLANATION")
    print("=" * 70)
    print("""
YOUR BUGGY CODE:
────────────────────────────────────────────────────────────────────
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
    def height(self, root):  # ❌ BUG 1: Remove 'self'
        if root is None:
            return 0
        return 1 + max(self.height(root.left), ...)  # ❌ BUG 2: Remove 'self.'

THE BUGS:
─────────
1. ❌ def height(self, root):
   - Nested functions don't have 'self'
   - Only class methods have 'self' 
   - ✓ Should be: def height(root):

2. ❌ return 1 + max(self.height(root.left), ...)
   - Can't call nested function with 'self.'
   - ✓ Should be: return 1 + max(height(root.left), ...)

CORRECTED CODE:
────────────────────────────────────────────────────────────────────
def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
    def height(root):  # ✓ No 'self'
        if root is None:
            return 0
        return 1 + max(height(root.left), height(root.right))  # ✓ Just height()
    
    if root is None:
        return True
    
    left_height = height(root.left)
    right_height = height(root.right)
    
    if abs(left_height - right_height) > 1:
        return False
    
    return self.isBalanced(root.left) and self.isBalanced(root.right)

NOTE: This fixes the bugs BUT it's still O(n²) inefficient.
      For optimal O(n) solution, see the isBalanced() method below.
    """)
    
    print("\n" + "=" * 70)
    print("BALANCED BINARY TREE - Check if height-balanced")
    print("=" * 70)
    
    # Test your fixed code
    print("\n📌 Testing YOUR CODE (fixed):")
    tree_test = build_tree([3, 9, 20, None, None, 15, 7])
    print(f"Your fixed code: {solution.isBalanced_YourCodeFixed(tree_test)}")
    print(f"Optimized O(n):  {solution.isBalanced(tree_test)}")
    print("Both return True ✓")
    
    # Test 1: Balanced tree
    print("\n" + "=" * 70)
    print("\n📌 Test 1: [3,9,20,null,null,15,7]")
    tree1 = build_tree([3, 9, 20, None, None, 15, 7])
    print("\nTree Structure:")
    visualize_tree(tree1)
    print("\nBalance Check (detailed):")
    check_balance_detailed(tree1)
    print(f"\nResult: {solution.isBalanced(tree1)}")
    print(f"Expected: True ✓")
    
    
    # Test 2: Unbalanced tree
    print("\n" + "=" * 70)
    print("\n📌 Test 2: [1,2,2,3,3,null,null,4,4]")
    tree2 = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    print("\nTree Structure:")
    visualize_tree(tree2)
    print("\nBalance Check (detailed):")
    check_balance_detailed(tree2)
    print(f"\nResult: {solution.isBalanced(tree2)}")
    print(f"Expected: False ✓")
    
    
    # Test 3: Empty tree
    print("\n" + "=" * 70)
    print("\n📌 Test 3: []")
    tree3 = None
    print(f"\nResult: {solution.isBalanced(tree3)}")
    print(f"Expected: True ✓")
    
    
    # Test 4: Single node
    print("\n" + "=" * 70)
    print("\n📌 Test 4: [1]")
    tree4 = build_tree([1])
    print("\nTree Structure:")
    visualize_tree(tree4)
    print(f"\nResult: {solution.isBalanced(tree4)}")
    print(f"Expected: True ✓")
    
    
    # Test 5: Left-skewed tree (unbalanced)
    print("\n" + "=" * 70)
    print("\n📌 Test 5: [1,2,null,3] (left-skewed)")
    tree5 = build_tree([1, 2, None, 3])
    print("\nTree Structure:")
    visualize_tree(tree5)
    print("\nBalance Check (detailed):")
    check_balance_detailed(tree5)
    print(f"\nResult: {solution.isBalanced(tree5)}")
    print(f"Expected: False ✓")
    
    
    # Test 6: Perfectly balanced tree
    print("\n" + "=" * 70)
    print("\n📌 Test 6: [1,2,3,4,5,6,7] (perfect binary tree)")
    tree6 = build_tree([1, 2, 3, 4, 5, 6, 7])
    print("\nTree Structure:")
    visualize_tree(tree6)
    print("\nBalance Check (detailed):")
    check_balance_detailed(tree6)
    print(f"\nResult: {solution.isBalanced(tree6)}")
    print(f"Expected: True ✓")
    
    
    # Summary
    print("\n" + "=" * 70)
    print("APPROACH COMPARISON")
    print("=" * 70)
    print("""
DEFINITION: A tree is balanced if for EVERY node, the height difference 
between left and right subtrees is ≤ 1.

APPROACH 1 - Naive (O(n²)):
─────────────────────────────────────────────────
def isBalanced(root):
    if not root:
        return True
    
    left_height = height(root.left)    ← Calculate height: O(n)
    right_height = height(root.right)  ← Calculate height: O(n)
    
    if abs(left_height - right_height) > 1:
        return False
    
    return isBalanced(root.left) and isBalanced(root.right)

❌ Problem: Recalculates height multiple times
Time: O(n²) - height() called for each of n nodes


APPROACH 2 - Optimized (O(n)) ✓ RECOMMENDED:
─────────────────────────────────────────────────
def isBalanced(root):
    def check_height(node):
        if not node:
            return 0
        
        left = check_height(node.left)
        if left == -1:
            return -1  ← Early exit if unbalanced
        
        right = check_height(node.right)
        if right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1  ← Mark as unbalanced
        
        return 1 + max(left, right)
    
    return check_height(root) != -1

✓ Calculates height ONCE while checking balance
✓ Uses -1 as sentinel value for unbalanced
✓ Time: O(n) - each node visited once
✓ Space: O(h) - recursion stack


KEY INSIGHT:
────────────
Instead of calculating height separately, we combine:
1. Height calculation
2. Balance checking
3. Early termination (return -1 if unbalanced)

This reduces time from O(n²) to O(n)!
    """)
