# Given the root of a binary tree, find and return the root nodes of all duplicate subtrees.
# Time Complexity = O(n), Space Complexity = O(n²)
# Leetcode = 652

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Input
values = input("Enter the values: ").split()

values = [None if x == "null" else int(x) for x in values]


# Build tree
if not values or values[0] is None:
    root = None
else:
    root = TreeNode(values[0])
    queue = deque([root])

    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        # Left child
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)

        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)

        i += 1


# Find duplicate subtrees
seen = {}
result = []


def traverse(root):

    if root is None:
        return "#"

    left = traverse(root.left)
    right = traverse(root.right)

    subtree = str(root.val) + "," + left + "," + right

    if subtree not in seen:
        seen[subtree] = 1
    else:
        seen[subtree] += 1

        if seen[subtree] == 2:
            result.append(root)

    return subtree


traverse(root)


# Convert a subtree to LeetCode-style list
def subtree_to_list(root):

    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        current = queue.popleft()

        if current is None:
            result.append(None)
            continue

        result.append(current.val)

        queue.append(current.left)
        queue.append(current.right)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


# Print answer
answer = []

for node in result:
    answer.append(subtree_to_list(node))

print("Output:", answer)
