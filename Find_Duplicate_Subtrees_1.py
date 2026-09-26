# Given the root of a binary tree, find and return the root nodes of all duplicate subtrees.
# Time Complexity = O(n), Space Complexity = O(n)
# Leetcode = 652

from collections import deque, defaultdict

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
seen = defaultdict(int)
subtree_ids = {}
result = []

next_id = 1


def traverse(root):
    global next_id

    if root is None:
        return 0

    left_id = traverse(root.left)
    right_id = traverse(root.right)

    # Representation of this subtree
    key = (root.val, left_id, right_id)

    # Assign an ID to this unique subtree
    if key not in subtree_ids:
        subtree_ids[key] = next_id
        next_id += 1

    subtree_id = subtree_ids[key]

    seen[subtree_id] += 1

    # Only add the second occurrence
    if seen[subtree_id] == 2:
        result.append(root)

    return subtree_id


traverse(root)


# Convert subtree to LeetCode-style list
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
