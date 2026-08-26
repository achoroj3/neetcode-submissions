class LRUCache:
    # node class
    class Node:
        def __init__(self, key, value):
            self.left = self.right = None
            self.key = key
            self.val = value

    # insert node at head
    def insert(self, node: Node):
        node.right = self.head
        node.left = None

        if self.head:
            self.head.left = node
        else:
            # first node
            self.tail = node

        self.head = node

    # remove node from linked list
    def remove(self, node: Node):
        if node.left:
            node.left.right = node.right
        else:
            # node is head
            self.head = node.right

        if node.right:
            node.right.left = node.left
        else:
            # node is tail
            self.tail = node.left

    # move node to head
    def move(self, node: Node):
        self.remove(node)
        self.insert(node)

    # remove least recently used node
    def evict(self):
        node = self.tail

        self.remove(node)
        del self.cache[node.key]

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = self.tail = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.move(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move(node)
            return

        # If full, remove LRU node first
        if len(self.cache) == self.cap:
            self.evict()

        node = self.Node(key, value)
        self.cache[key] = node
        self.insert(node)