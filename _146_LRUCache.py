"""
146. LRU Cache
https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
  - LRUCache(int capacity)  Initialize the LRU cache with positive size capacity.
  - int get(int key)         Return the value of the key if it exists, otherwise return -1.
  - void put(int key, int value)  Update the value of the key if it exists. Otherwise, add
    the key-value pair to the cache. If the number of keys exceeds the capacity, evict the
    least recently used key.

Both get and put must run in O(1) average time complexity.

=========================================================================
Idea:
  Use a Hash Map + Doubly Linked List.

  - Hash map (dict): key -> Node, gives O(1) lookup.
  - Doubly linked list: maintains usage order. The node right after the
    dummy head is the MOST recently used; the node right before the dummy
    tail is the LEAST recently used.

  get(key):
    1. If key not in dict, return -1.
    2. Otherwise, move the node to the head (most recent) and return its value.

  put(key, value):
    1. If key already in dict, update its value and move it to the head.
    2. Otherwise, create a new node, add it to the head, and put it in the dict.
    3. If size exceeds capacity, remove the node at the tail (LRU) and delete
       its key from the dict.

  Time:  O(1) for both get and put.
  Space: O(capacity)
=========================================================================
"""


class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head and tail so we never deal with None edge cases
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Unlink a node from the doubly linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node: Node):
        """Insert a node right after the dummy head (most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_head(node)
        return node.val

    def put(self, key: int, value: int):
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_head(node)

            if len(self.cache) > self.capacity:
                # Evict the least recently used (node before dummy tail)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]


## Run Tests
import unittest

class TestLRUCache(unittest.TestCase):

    def test_basic_put_and_get(self):
        cache = LRUCache(2)
        cache.put(1, 10)
        cache.put(2, 20)
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(2), 20)

    def test_eviction_on_capacity_overflow(self):
        cache = LRUCache(2)
        cache.put(1, 10)
        cache.put(2, 20)
        cache.put(3, 30)          # evicts key 1
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 30)

    def test_update_existing_key(self):
        cache = LRUCache(2)
        cache.put(1, 10)
        cache.put(2, 20)
        cache.put(1, 100)         # update key 1, also refreshes it
        self.assertEqual(cache.get(1), 100)
        cache.put(3, 30)          # evicts key 2 (not 1, because 1 was refreshed)
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 100)

    def test_get_missing_key_returns_negative_one(self):
        cache = LRUCache(2)
        self.assertEqual(cache.get(99), -1)

    def test_get_refreshes_recency(self):
        cache = LRUCache(2)
        cache.put(1, 10)
        cache.put(2, 20)
        cache.get(1)              # key 1 is now most recently used
        cache.put(3, 30)          # evicts key 2 (LRU), not key 1
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(3), 30)

    def test_capacity_one(self):
        cache = LRUCache(1)
        cache.put(1, 10)
        self.assertEqual(cache.get(1), 10)
        cache.put(2, 20)          # evicts key 1
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 20)

    def test_leetcode_example(self):
        """
        LeetCode example:
        ["LRUCache","put","put","get","put","get","put","get","get","get"]
        [[2],       [1,1],[2,2],[1],  [3,3],[2],  [4,4],[1],  [3],  [4]]
        Expected: [null, null, null, 1, null, -1, null, -1, 3, 4]
        """
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)           # evicts key 2
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)           # evicts key 1
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)


if __name__ == '__main__':
    unittest.main()
