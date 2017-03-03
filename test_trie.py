import unittest
from trie import Trie


class TrieTest(unittest.TestCase):

    def test_add(self):
        t = Trie()
        t.add('hello')
        self.assertEquals(t.trie, {'h': {'e': {'l': {'l': {'o': {'$': None}}}}}})
        t.add('hell')
        self.assertEquals(t.trie, {'h': {'e': {'l': {'l': {'o': {'$': None}, '$': None}}}}})
