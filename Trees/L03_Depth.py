"""
Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
- The number of nodes in the tree is in the range [0, 10^4]
- -100 <= Node.val <= 100
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
    # APPROACH 1: BFS (Level Order Traversal) - YOUR SOLUTION ✓
    # ========================================================================
    def maxDepth_BFS(self, root: Optional[TreeNode]) -> int:
        """
        BFS approach: Count levels while doing level-order traversal
        
        Time Complexity: O(n) - visit each node once
        Space Complexity: O(w) - where w is max width of tree (queue size)
        
        YOUR SOLUTION IS CORRECT! This is a solid approach.
        """
        if root is None:
            return 0
        
        level = 0
        queue = deque([root])
        
        while queue:
            # KEY: Process all nodes at current level before moving to next
            for i in range(len(queue)):
                current_node = queue.popleft()
                
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            
            level += 1  # After processing entire level, increment depth
        
        return level
    
    
    # ========================================================================
    # APPROACH 2: DFS Recursive - SIMPLEST & MOST ELEGANT ✓
    # ========================================================================
    def maxDepth_DFS(self, root: Optional[TreeNode]) -> int:
        """
        DFS recursive: Depth = 1 + max(left depth, right depth)
        
        Time Complexity: O(n) - visit each node once
        Space Complexity: O(h) - recursion stack (h = height)
        
        This is THE STANDARD solution most interviewers expect!
        Much more concise than BFS for this problem.
        """
        # Base case: empty tree has depth 0
        if root is None:
            return 0
        
        # Recursive case: get depth of left and right subtrees
        left_depth = self.maxDepth_DFS(root.left)
        right_depth = self.maxDepth_DFS(root.right)
        
        # Current depth = 1 (for root) + max of subtree depths
        return 1 + max(left_depth, right_depth)
    
    
    # One-liner version (same logic)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Most concise - preferred in interviews"""
        return 0 if not root else 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        )
    
    
    # ========================================================================
    # APPROACH 3: DFS Iterative (using stack)
    # ========================================================================
    def maxDepth_DFS_Iterative(self, root: Optional[TreeNode]) -> int:
        """
        DFS iterative: Use stack to track (node, depth) pairs
        
        Time Complexity: O(n)
        Space Complexity: O(h) - stack height
        """
        if not root:
            return 0
        
        stack = [(root, 1)]  # (node, current_depth)
        max_depth = 0
        
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            
            # Push children with incremented depth
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        
        return max_depth


# ============================================================================
# Helper Functions for Testing
# ============================================================================

def build_tree(values):
    """Build tree from level-order list (LeetCode format with None for null)"""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Add left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Add right child
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


# ============================================================================
# Test Cases
# ============================================================================

if __name__ == "__main__":
    solution = Solution()
    
    print("=" * 70)
    print("MAXIMUM DEPTH OF BINARY TREE - Comparing Approaches")
    print("=" * 70)
    
    # Test 1: [3,9,20,null,null,15,7]
    print("\n📌 Test 1: [3,9,20,null,null,15,7]")
    print("\nTree Structure:")
    tree1 = build_tree([3, 9, 20, None, None, 15, 7])
    visualize_tree(tree1)
    
    print(f"\nResults:")
    print(f"  BFS (Your Solution):  {solution.maxDepth_BFS(tree1)}")
    print(f"  DFS Recursive:        {solution.maxDepth_DFS(tree1)}")
    print(f"  DFS Iterative:        {solution.maxDepth_DFS_Iterative(tree1)}")
    print(f"  Expected: 3 ✓")
    
    
    # Test 2: [1,null,2]
    print("\n" + "-" * 70)
    print("\n📌 Test 2: [1,null,2]")
    print("\nTree Structure:")
    tree2 = build_tree([1, None, 2])
    visualize_tree(tree2)
    
    print(f"\nResults:")
    print(f"  BFS (Your Solution):  {solution.maxDepth_BFS(tree2)}")
    print(f"  DFS Recursive:        {solution.maxDepth_DFS(tree2)}")
    print(f"  DFS Iterative:        {solution.maxDepth_DFS_Iterative(tree2)}")
    print(f"  Expected: 2 ✓")
    
    
    # Test 3: Empty tree
    print("\n" + "-" * 70)
    print("\n📌 Test 3: []")
    tree3 = None
    
    print(f"\nResults:")
    print(f"  BFS (Your Solution):  {solution.maxDepth_BFS(tree3)}")
    print(f"  DFS Recursive:        {solution.maxDepth_DFS(tree3)}")
    print(f"  DFS Iterative:        {solution.maxDepth_DFS_Iterative(tree3)}")
    print(f"  Expected: 0 ✓")
    
    
    # Test 4: Single node
    print("\n" + "-" * 70)
    print("\n📌 Test 4: [1]")
    print("\nTree Structure:")
    tree4 = build_tree([1])
    visualize_tree(tree4)
    
    print(f"\nResults:")
    print(f"  BFS (Your Solution):  {solution.maxDepth_BFS(tree4)}")
    print(f"  DFS Recursive:        {solution.maxDepth_DFS(tree4)}")
    print(f"  DFS Iterative:        {solution.maxDepth_DFS_Iterative(tree4)}")
    print(f"  Expected: 1 ✓")
    
    
    # Test 5: Deeper tree
    print("\n" + "-" * 70)
    print("\n📌 Test 5: [1,2,3,4,5]")
    print("\nTree Structure:")
    tree5 = build_tree([1, 2, 3, 4, 5])
    visualize_tree(tree5)
    
    print(f"\nResults:")
    print(f"  BFS (Your Solution):  {solution.maxDepth_BFS(tree5)}")
    print(f"  DFS Recursive:        {solution.maxDepth_DFS(tree5)}")
    print(f"  DFS Iterative:        {solution.maxDepth_DFS_Iterative(tree5)}")
    print(f"  Expected: 3 ✓")
    
    
    # Summary
    print("\n" + "=" * 70)
    print("WHAT I MEANT - Comparison:")
    print("=" * 70)
    print("""
YOUR BFS SOLUTION:
✓ CORRECT - works perfectly!
✓ Intuitive: literally counts levels
✓ Good for: level-related problems
- More lines of code (8-10 lines)
- Space: O(width) - can be large for wide trees

DFS RECURSIVE (Recommended):
✓ SIMPLEST - just 3 lines or even 1 line!
✓ Natural for tree problems
✓ Elegant formula: depth = 1 + max(left, right)
✓ Space: O(height) - usually better for balanced trees
✓ Most interviewers prefer this for its simplicity

BOTH ARE O(n) time and correct!

Code Comparison:
───────────────────────────────────────────────────────
BFS (Your way):                DFS (Simpler):
───────────────────────────────────────────────────────
if root is None:               if not root:
    return 0                       return 0
                               
level = 0                      return 1 + max(
queue = deque([root])              maxDepth(root.left),
while queue:                       maxDepth(root.right)
    for i in range(len(queue)):)
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    level += 1
return level
───────────────────────────────────────────────────────
10 lines                       3 lines (or 1 line!)
───────────────────────────────────────────────────────

Both solve the problem correctly, but DFS is more concise! 🎯
    """)
