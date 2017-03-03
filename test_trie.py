import unittest
from trie import Trie


class TrieTest(unittest.TestCase):

    def test_add(self):
        t = Trie()
        t.add('hello')
        self.assertEquals(t.trie, {'h': {'e': {'l': {'l': {'o': {'$': None}}}}}})
        t.add('hell')
        self.assertEquals(t.trie, {'h': {'e': {'l': {'l': {'o': {'$': None}, '$': None}}}}})

    def assertSameSet(self, first, second):
        self.assertEqual(set(first), set(second))

    def test_allwords(self):
        t = Trie()
        t.add('hello')
        t.add('help')
        t.add('hell')
        t.add('hall')
        self.assertSameSet(['hello', 'help', 'hell', 'hall'],
                           t.allwords())

    def test_lookup_prefix(self):
        t = Trie()
        t.add('hello')
        t.add('help')
        t.add('hell')
        t.add('hall')
        t.add('harp')
        self.assertSameSet(t.lookup('hel'),
                           ['hello', 'help', 'hell'])
